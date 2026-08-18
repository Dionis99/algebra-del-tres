"""
Medir comportamiento del 0 en redes entrenadas.
"""
import sys, os
import random
import json
from datetime import datetime
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from networks.collapsing_network import RedColapsanteV2
from datasets.basic import get_dataset, list_datasets

def evolucionar_red(dataset, poblacion_size=300, generaciones=400, 
                    tasa_mutacion=0.14, elitismo=10):
    poblacion = [RedColapsanteV2(3) for _ in range(poblacion_size)]
    mejor_fitness = 0.0
    mejor_red = None
    
    for gen in range(generaciones):
        evaluados = [(red.evaluate(dataset), red) for red in poblacion]
        evaluados.sort(key=lambda x: x[0], reverse=True)
        
        if evaluados[0][0] > mejor_fitness:
            mejor_fitness = evaluados[0][0]
            mejor_red = evaluados[0][1].clone()
        
        if mejor_fitness >= 1.0:
            break
        
        nueva = [evaluados[i][1].clone() for i in range(elitismo)]
        while len(nueva) < poblacion_size:
            torneo = random.sample(evaluados[:100], 3)
            torneo.sort(key=lambda x: x[0], reverse=True)
            padre = torneo[0][1]
            hijo = padre.clone()
            hijo.mutate(tasa_mutacion)
            nueva.append(hijo)
        poblacion = nueva
    
    return mejor_red, mejor_fitness

def analizar_collapse(red, dataset):
    """Analiza el comportamiento del 0 en una red entrenada."""
    
    # Recolectar estadísticas de todas las neuronas
    todas_neuronas = red.hidden + [red.output]
    
    total_pesos = 0
    pesos_cero = 0
    umbrales = []
    colapsos_por_forward = []
    presiones = []
    
    # Evaluar en todo el dataset
    for entradas, _ in dataset:
        red.reset()
        
        # Capa oculta
        hidden_outs = []
        for n in red.hidden:
            presion = sum(entradas) / len(entradas)
            presiones.append(presion)
            
            # Contar colapsos en esta neurona
            colapsos = sum(1 for w in n.pesos if w == 0)
            colapsos_por_forward.append(colapsos)
            
            hidden_outs.append(n.forward(entradas))
        
        # Capa de salida
        presion = sum(hidden_outs) / len(hidden_outs)
        presiones.append(presion)
        
        colapsos = sum(1 for w in red.output.pesos if w == 0)
        colapsos_por_forward.append(colapsos)
        
        red.output.forward(hidden_outs)
    
    # Recolectar pesos y umbrales
    for n in todas_neuronas:
        for w in n.pesos:
            total_pesos += 1
            if w == 0:
                pesos_cero += 1
        umbrales.append(n.umbral_colapso)
    
    # Calcular estadísticas
    stats = {
        "total_pesos": total_pesos,
        "pesos_cero": pesos_cero,
        "tasa_ceros": pesos_cero / total_pesos,
        "tasa_no_ceros": 1 - (pesos_cero / total_pesos),
        "umbrales_media": np.mean(umbrales),
        "umbrales_std": np.std(umbrales),
        "umbrales_min": np.min(umbrales),
        "umbrales_max": np.max(umbrales),
        "colapsos_media": np.mean(colapsos_por_forward),
        "colapsos_std": np.std(colapsos_por_forward),
        "presion_media": np.mean(presiones),
        "presion_std": np.std(presiones),
        "presion_min": np.min(presiones),
        "presion_max": np.max(presiones),
    }
    
    return stats

def run_analysis():
    print("=" * 70)
    print("ANÁLISIS DEL COMPORTAMIENTO DEL 0")
    print("=" * 70)
    
    resultados = {}
    
    for dataset_name in list_datasets():
        dataset = get_dataset(dataset_name)
        print(f"\n--- Dataset: {dataset_name.upper()} ---")
        
        print(f"  Entrenando RedColapsanteV2...", end=" ", flush=True)
        red, fitness = evolucionar_red(dataset)
        print(f"precisión = {fitness:.4f}")
        
        print(f"  Analizando comportamiento del 0...")
        stats = analizar_collapse(red, dataset)
        
        print(f"\n  Estadísticas:")
        print(f"    Total pesos: {stats['total_pesos']}")
        print(f"    Pesos en 0: {stats['pesos_cero']} ({stats['tasa_ceros']*100:.1f}%)")
        print(f"    Pesos no-0: {stats['total_pesos']-stats['pesos_cero']} ({stats['tasa_no_ceros']*100:.1f}%)")
        print(f"\n    Umbrales de colapso:")
        print(f"      Media: {stats['umbrales_media']:.3f}")
        print(f"      Std: {stats['umbrales_std']:.3f}")
        print(f"      Rango: [{stats['umbrales_min']:.3f}, {stats['umbrales_max']:.3f}]")
        print(f"\n    Colapsos por forward:")
        print(f"      Media: {stats['colapsos_media']:.2f}")
        print(f"      Std: {stats['colapsos_std']:.2f}")
        print(f"\n    Presión del contexto:")
        print(f"      Media: {stats['presion_media']:.3f}")
        print(f"      Std: {stats['presion_std']:.3f}")
        print(f"      Rango: [{stats['presion_min']:.3f}, {stats['presion_max']:.3f}]")
        
        resultados[dataset_name] = {
            "precision": fitness,
            "stats": stats
        }
    
    # Resumen comparativo
    print("\n" + "=" * 70)
    print("RESUMEN COMPARATIVO")
    print("=" * 70)
    
    print(f"\n{'Dataset':<15} {'Precisión':<10} {'% Ceros':<10} {'Umbrales':<15} {'Colapsos/fw':<12}")
    print("-" * 70)
    
    for dataset_name, data in resultados.items():
        stats = data["stats"]
        print(f"{dataset_name:<15} {data['precision']:<10.4f} "
              f"{stats['tasa_ceros']*100:<10.1f}% "
              f"{stats['umbrales_media']:.3f}±{stats['umbrales_std']:.3f}  "
              f"{stats['colapsos_media']:.2f}±{stats['colapsos_std']:.2f}")
    
    # Guardar
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("experiments", exist_ok=True)
    with open(f"experiments/collapse_analysis_{timestamp}.json", "w") as f:
        json.dump(resultados, f, indent=2)
    print(f"\nResultados guardados en experiments/collapse_analysis_{timestamp}.json")
    
    return resultados

if __name__ == "__main__":
    random.seed(42)
    run_analysis()
