import random, math, time

# Reutilizamos las clases definidas en fase_d_fragmentada_colapsante.py
from fase_d_fragmentada_colapsante import (
    RedFragmentadaColapsante, error_fragmentada_colapsante,
    mutar_un_parametro, corrida_recocido, corrida_con_reinicios,
    DATASET_SENTIMIENTO, DATASET_XOR, DATASET_MAYORIA
)

def evaluar_robustez(dataset, nombre, n_externas=10, n_restarts=3,
                     epocas_por_restart=150, intentos_por_epoca=200):
    exitos = 0
    errores = []
    tiempos = []
    t0 = time.time()
    for i in range(n_externas):
        semilla_base = 8000 + i * 100
        t_corr = time.time()
        _, error = corrida_con_reinicios(dataset, semilla_base=semilla_base,
                                        n_restarts=n_restarts,
                                        epocas_por_restart=epocas_por_restart,
                                        intentos_por_epoca=intentos_por_epoca)
        t_corr = time.time() - t_corr
        tiempos.append(t_corr)
        errores.append(error)
        if error == 0:
            exitos += 1
        print(f"  Corrida {i+1:2d}/{n_externas} | Error: {error}/9 | Tiempo: {t_corr:.1f}s")
    t1 = time.time()
    print(f"\n[RESUMEN {nombre}]")
    print(f"  Éxitos: {exitos}/{n_externas} = {100*exitos/n_externas:.0f}%")
    print(f"  Error promedio final: {sum(errores)/len(errores):.2f}")
    print(f"  Tiempo promedio por corrida: {sum(tiempos)/len(tiempos):.1f}s")
    print(f"  Tiempo total: {t1-t0:.1f}s\n")

if __name__ == "__main__":
    print("=" * 70)
    print("FASE D ROBUSTEZ: FRAGMENTADA COLAPSANTE")
    print("=" * 70)

    print("\n--- Sentimiento ---")
    evaluar_robustez(DATASET_SENTIMIENTO, "Sentimiento", n_externas=5)

    print("\n--- XOR ---")
    evaluar_robustez(DATASET_XOR, "XOR", n_externas=5)

    print("\n--- Mayoría ---")
    evaluar_robustez(DATASET_MAYORIA, "Mayoría", n_externas=5)
