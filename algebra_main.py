#!/usr/bin/env python3
"""
ALGEBRA DEL TRES - Main: ejecuta datasets pequeños y MNIST reducido
"""

from algebra_01_motor_datasets import *
from algebra_02_neuronas import *
from algebra_03_redes_evolucion import *
from algebra_04_mnist import *

if __name__ == "__main__":
    print("=" * 70)
    print("EL ALGEBRA DEL TRES - REDES NEURONALES EVOLUTIVAS")
    print("=" * 70)

    print("\n[1] RED COLAPSANTE V2 (2->3->1)")
    print("-" * 50)
    random.seed(42)
    ev1 = EvolucionGenerica(lambda: RedFeedforwardDelTres(3), DATASET_SENTIMIENTO,
                            300, 400, 0.14, 5, "CV2-Sent")
    m1 = ev1.evolucionar()

    random.seed(123)
    ev2 = EvolucionGenerica(lambda: RedFeedforwardDelTres(3), DATASET_XOR,
                            300, 400, 0.14, 5, "CV2-XOR")
    m2 = ev2.evolucionar()

    random.seed(456)
    ev3 = EvolucionGenerica(lambda: RedFeedforwardDelTres(3), DATASET_MAYORIA,
                            300, 400, 0.14, 5, "CV2-May")
    m3 = ev3.evolucionar()

    print("\n--- RESUMEN COLAPSANTE V2 ---")
    print(f"Sentimiento: {ev1.mejor_fitness*100:.1f}%")
    print(f"XOR:         {ev2.mejor_fitness*100:.1f}%")
    print(f"Mayoria:     {ev3.mejor_fitness*100:.1f}%")

    print("\n[2] RED FRAGMENTADA COLAPSANTE (2->3->1)")
    print("-" * 50)
    random.seed(42)
    ev4 = EvolucionGenerica(
        lambda: RedFragmentadaColapsante(3, 3, 3), DATASET_SENTIMIENTO,
        300, 400, 0.14, 5, "FragColap-Sent")
    m4 = ev4.evolucionar()

    random.seed(123)
    ev5 = EvolucionGenerica(
        lambda: RedFragmentadaColapsante(3, 3, 3), DATASET_XOR,
        300, 400, 0.14, 5, "FragColap-XOR")
    m5 = ev5.evolucionar()

    random.seed(456)
    ev6 = EvolucionGenerica(
        lambda: RedFragmentadaColapsante(3, 3, 3), DATASET_MAYORIA,
        300, 400, 0.14, 5, "FragColap-May")
    m6 = ev6.evolucionar()

    print("\n--- RESUMEN FRAGMENTADA COLAPSANTE ---")
    print(f"Sentimiento: {ev4.mejor_fitness*100:.1f}%")
    print(f"XOR:         {ev5.mejor_fitness*100:.1f}%")
    print(f"Mayoria:     {ev6.mejor_fitness*100:.1f}%")

    print("\n[3] MNIST TERNARIZADO - Red Vectorizada")
    print("-" * 50)
    X_train, y_train, X_test, y_test = cargar_mnist(n_train=200, n_test=50)
    if X_train is not None:
        print(f"Train: {len(X_train)} | Test: {len(X_test)}")
        print(f"Balance: {Counter(y_train)}")
        random.seed(42)
        factory_mnist = lambda: RedTresMNISTVectorizada([784, 16, 10])
        ev_mnist = EvolucionMNISTVectorizada(
            factory_mnist, X_train, y_train, X_test, y_test,
            poblacion_size=10, generaciones=20, tasa_mutacion=0.12, elitismo=3)
        mejor_mnist = ev_mnist.evolucionar()
    else:
        print("MNIST no disponible. Instalar: pip install scikit-learn")

    print("\n" + "=" * 70)
    print("EJECUCION COMPLETADA")
    print("=" * 70)
