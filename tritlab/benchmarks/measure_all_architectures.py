"""
Análisis del comportamiento del 0 en TODAS las arquitecturas.
No descartamos ninguna: cada una tiene su valor.
"""
import sys, os
import random
import json
from datetime import datetime
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from networks.collapsing_network import RedColapsanteV2
from networks.fragmented_network import RedFragmentada
from networks.hybrid_network import RedFragmentadaColapsante
from datasets.basic import get_dataset, list_datasets

def evolucionar_red(factory, dataset, poblacion_size=300, generaciones=400, 
                    tasa_mutacion=0.14, elitismo=10):
    poblacion = [factory() for _ in range(poblacion_size)]
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

def contar_pesos_cero(red):
    """Cuenta pesos en 0 según el tipo de red."""
    total = 0
    ceros = 0
    
    if isinstance(red, RedColapsanteV2):
        # RedColapsanteV2: solo pesos
        for n in red.hidden + [red.output]:
            total += len(n.pesos)
            ceros += sum(1 for w in n.pesos if w == 0)
    
    elif isinstance(red, RedFragmentada):
        # RedFragmentada: 4 conjuntos de pesos por neurona
        for n in red.hidden + [red.output]:
            for pesos in [n.pesos_out, n.pesos_read, n.pesos_write, n.pesos_val]:
                total += len(pesos)
                ceros += sum(1 for w in pesos if w == 0)
    
    elif isinstance(red, RedFragmentadaColapsante):
        # RedFragmentadaColapsante: 4 sub-redes Colapsantes por neurona
        for n in red.hidden + [red.output]:
            for subred in [n.read, n.out, n.write, n.val]:
                total += len(subred.pesos)
                ceros += sum(1 for w in subred.pesos if w == 0)
    
    return ceros, total

def analizar_arquitectura(red, dataset, nombre):
    """Analiza el comportamiento de una arquitectura."""
    
    ceros, total = contar_pesos_cero(red)
    tasa_ceros = ceros / total if total > 0 else 0
    
    # Recolectar umbrales si existen
    umbrales = []
    if isinstance(red, RedColapsanteV2):
        for n in red.hidden + [red.output]:
            umbrales.append(n.umbral_colapso)
    elif isinstance(red, RedFragmentadaColapsante):
        for n in red.hidden + [red.output]:
            for subred in [n.read, n.out, n.write, n.val]:
                umbrales.append(subred.umbral_colapso)
    
    stats = {
        "arquitectura": nombre,
        "total_pesos": total,
        "pesos_cero": ceros,
        "tasa_ceros": tasa_ceros,
        "num_umbrales": len(umbrales),
        "umbrales_media": np.mean(umbrales) if umbrales else None,
        "umbrales_std": np.std(umbrales) if umbrales else None,
        "umbrales_rango": (np.min(umbrales), np.max(umbrales)) if umbrales else None,
    }
    
    return stats

def run_analysis():
    print("=" * 70)
    print("ANÁLISIS DE TODAS LAS ARQUITECTURAS")
    print("Ninguna se descarta: cada una tiene su valor")
    print("=" * 70)
    
    resultados = {}
    
    for dataset_name in list_datasets():
        dataset = get_dataset(dataset_name)
        print(f"\n--- Dataset: {dataset_name.upper()} ---")
        
        arquitecturas = [
            ("RedColapsanteV2", lambda: RedColapsanteV2(3)),
            ("RedFragmentada", lambda: RedFragmentada(3, 3, 3)),
            ("RedHibrida", lambda: RedFragmentadaColapsante(3, 3, 3)),
        ]
        
        for nombre, factory in arquitecturas:
            print(f"  Entrenando {nombre}...", end=" ", flush=True)
            red, fitness = evolucionar_red(factory, dataset)
            print(f"precisión = {fitness:.4f}")
            
            stats = analizar_arquitectura(red, dataset, nombre)
            stats["precision"] = fitness
            
            print(f"    Total pesos: {stats['total_pesos']}")
            print(f"    Pesos en 0: {stats['pesos_cero']} ({stats['tasa_ceros']*100:.1f}%)")
            if stats['num_umbrales'] > 0:
                print(f"    Umbrales: {stats['umbrales_media']:.3f}±{stats['umbrales_std']:.3f}")
            
            if dataset_name not in resultados:
                resultados[dataset_name] = {}
            resultados[dataset_name][nombre] = stats
    
    # Resumen comparativo
    print("\n" + "=" * 70)
    print("RESUMEN COMPARATIVO")
    print("=" * 70)
    
    for dataset_name, arqs in resultados.items():
        print(f"\n{dataset_name.upper()}:")
        print(f"  {'Arquitectura':<25} {'Precisión':<10} {'% Ceros':<10} {'Total Pesos':<12}")
        print("  " + "-" * 65)
        
        for nombre, stats in arqs.items():
            print(f"  {nombre:<25} {stats['precision']:<10.4f} "
                  f"{stats['tasa_ceros']*100:<10.1f}% {stats['total_pesos']:<12}")
    
    # Guardar
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("experiments", exist_ok=True)
    with open(f"experiments/all_architectures_{timestamp}.json", "w") as f:
        json.dump(resultados, f, indent=2)
    print(f"\nResultados guardados en experiments/all_architectures_{timestamp}.json")
    
    return resultados

if __name__ == "__main__":
    random.seed(42)
    run_analysis()
