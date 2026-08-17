import random
import math
import time

# Importar clases y funciones desde fase_b2_robustez.py
from fase_b2_robustez import (
    RedFragmentada, error_fragmentada, mutar_un_parametro_fragmentada
)

# =============================================================================
# UNA CORRIDA INTERNA DE RECOCIDO (sin reinicios)
# =============================================================================

def corrida_recocido_interna(dataset, semilla, epocas=120, intentos_por_epoca=200,
                             T0=0.8, decay=0.99, T_min=0.001):
    random.seed(semilla)
    red = RedFragmentada(hidden_size=3, num_slots=3, num_steps=3)

    current = red.clone()
    current_error = error_fragmentada(current, dataset)

    best = current.clone()
    best_error = current_error

    T = T0

    for epoca in range(epocas):
        for _ in range(intentos_por_epoca):
            candidato = current.clone()
            if not mutar_un_parametro_fragmentada(candidato):
                continue

            error_candidato = error_fragmentada(candidato, dataset)

            if (error_candidato < current_error or
                random.random() < math.exp((current_error - error_candidato) / T)):
                current = candidato
                current_error = error_candidato

                if current_error < best_error:
                    best_error = current_error
                    best = current.clone()
                    if best_error == 0:
                        return best, best_error

        T = max(T_min, T * decay)

    return best, best_error

# =============================================================================
# CORRIDA EXTERNA CON REINICIOS INTERNOS
# =============================================================================

def corrida_con_restarts(dataset, semilla_externa, n_restarts=3,
                         epocas_por_restart=120, intentos_por_epoca=200,
                         T0=0.8, decay=0.99):
    mejor_red_global = None
    mejor_error_global = 9

    for r in range(n_restarts):
        semilla = semilla_externa * 100 + r
        red_best, error = corrida_recocido_interna(
            dataset, semilla,
            epocas=epocas_por_restart,
            intentos_por_epoca=intentos_por_epoca,
            T0=T0, decay=decay
        )

        if error < mejor_error_global:
            mejor_error_global = error
            mejor_red_global = red_best.clone()

        if mejor_error_global == 0:
            break

    return mejor_red_global, mejor_error_global

# =============================================================================
# EVALUACIÓN DE ROBUSTEZ CON REINICIOS
# =============================================================================

def evaluar_con_restarts(dataset, nombre, n_externas=5, n_restarts=3,
                         epocas_por_restart=120, intentos_por_epoca=200):
    exitos = 0
    errores = []
    t0 = time.time()

    for i in range(n_externas):
        semilla_externa = 5000 + i
        _, error = corrida_con_restarts(
            dataset, semilla_externa,
            n_restarts=n_restarts,
            epocas_por_restart=epocas_por_restart,
            intentos_por_epoca=intentos_por_epoca
        )
        errores.append(error)
        if error == 0:
            exitos += 1
        print(f"  Corrida externa {i+1:2d}/{n_externas} | Error: {error}/9")

    t1 = time.time()
    print(f"\n[RESUMEN {nombre} con {n_restarts} reinicios internos]")
    print(f"  Éxitos: {exitos}/{n_externas} = {100*exitos/n_externas:.0f}%")
    print(f"  Error promedio final: {sum(errores)/len(errores):.2f}")
    print(f"  Tiempo total: {t1-t0:.1f}s\n")

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("FASE B3: ROBUSTEZ CON REINICIOS INTERNOS")
    print("=" * 70)

    # Solo XOR, que era el más problemático
    DATASET_XOR = [
        (-1, -1, -1), (-1, 0, 1), (-1, 1, 1),
        (0, -1, 1), (0, 0, 0), (0, 1, -1),
        (1, -1, 1), (1, 0, -1), (1, 1, -1),
    ]

    print("\n--- XOR ternario ---")
    evaluar_con_restarts(
        DATASET_XOR,
        nombre="XOR",
        n_externas=5,
        n_restarts=3,
        epocas_por_restart=120,
        intentos_por_epoca=200
    )
