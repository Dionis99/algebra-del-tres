"""
ALGEBRA DEL TRES - Parte 4: Capa vectorizada y cargador MNIST
"""

import numpy as np
from algebra_01_motor_datasets import P_VALS

class CapaColapsanteVectorizada:
    def __init__(self, n_inputs, n_neuronas):
        self.n_inputs = n_inputs
        self.n_neuronas = n_neuronas
        self.pesos = np.random.choice(P_VALS, size=(n_neuronas, n_inputs)).astype(np.int8)
        self.umbrales = np.random.uniform(-0.9, 0.9, size=n_neuronas)
        self.ops = np.random.choice([0, 1, 2], size=n_neuronas)

    def forward(self, x):
        presion = float(x.mean())
        pesos_colapsados = self.pesos.copy()
        mask_cero = (pesos_colapsados == 0)
        colapso = np.where(presion > self.umbrales, 1, -1).reshape(-1, 1)
        pesos_colapsados = np.where(mask_cero, colapso, pesos_colapsados)

        terminos = np.where(
            (pesos_colapsados == 0) | (x == 0),
            0,
            pesos_colapsados * x
        )

        resultado = terminos[:, 0].copy()
        for i in range(1, self.n_inputs):
            a = resultado
            b = terminos[:, i]
            resultado = np.where(
                a == b, a,
                np.where(a == 0, b, np.where(b == 0, a, 0))
            )

        resultado = np.where(self.ops == 1, np.where(resultado == 0, 1, resultado), resultado)
        resultado = np.where(self.ops == 2, np.where(resultado == 0, -1, resultado), resultado)
        return resultado.astype(np.int8)

    def clone(self):
        c = CapaColapsanteVectorizada(self.n_inputs, self.n_neuronas)
        c.pesos = self.pesos.copy()
        c.umbrales = self.umbrales.copy()
        c.ops = self.ops.copy()
        return c

    def mutate(self, tasa=0.15):
        mask = np.random.random(self.pesos.shape) < tasa
        self.pesos[mask] = np.random.choice(P_VALS, size=mask.sum())
        mask_u = np.random.random(self.umbrales.shape) < tasa
        self.umbrales[mask_u] = np.random.uniform(-0.9, 0.9, size=mask_u.sum())
        mask_o = np.random.random(self.ops.shape) < tasa
        self.ops[mask_o] = np.random.choice([0, 1, 2], size=mask_o.sum())


class RedTresMNISTVectorizada:
    def __init__(self, arch):
        self.arch = arch
        self.capas = []
        for i in range(len(arch) - 1):
            self.capas.append(CapaColapsanteVectorizada(arch[i], arch[i + 1]))

    def forward(self, x):
        activacion = x
        for capa in self.capas:
            activacion = capa.forward(activacion)
        return activacion

    def predict(self, x):
        outs = self.forward(x)
        return int(np.argmax(outs))

    def evaluate(self, X, y):
        aciertos = sum(1 for xi, yi in zip(X, y) if self.predict(xi) == yi)
        return aciertos / len(y)

    def clone(self):
        r = RedTresMNISTVectorizada(self.arch)
        for i, capa in enumerate(self.capas):
            r.capas[i] = capa.clone()
        return r

    def mutate(self, tasa=0.15):
        for capa in self.capas:
            capa.mutate(tasa)


class EvolucionMNISTVectorizada:
    def __init__(self, factory, X_train, y_train, X_test, y_test,
                 poblacion_size=20, generaciones=50, tasa_mutacion=0.12, elitismo=3):
        self.factory = factory
        self.X_train = X_train
        self.y_train = y_train
        self.X_test = X_test
        self.y_test = y_test
        self.poblacion_size = poblacion_size
        self.generaciones = generaciones
        self.tasa_mutacion = tasa_mutacion
        self.elitismo = elitismo
        self.mejor_historico = None
        self.mejor_fitness = 0.0

    def evaluar(self, red, X, y):
        aciertos = sum(1 for xi, yi in zip(X, y) if red.predict(xi) == yi)
        return aciertos / len(y)

    def evolucionar(self):
        t0 = time.time()
        self.poblacion = [self.factory() for _ in range(self.poblacion_size)]
        for gen in range(self.generaciones):
            evaluados = [(self.evaluar(red, self.X_train, self.y_train), red) for red in self.poblacion]
            evaluados.sort(key=lambda x: x[0], reverse=True)
            mejor_f = evaluados[0][0]
            if mejor_f > self.mejor_fitness:
                self.mejor_fitness = mejor_f
                self.mejor_historico = evaluados[0][1].clone()
            if gen % 5 == 0 or gen == self.generaciones - 1:
                f_test = self.evaluar(self.mejor_historico, self.X_test, self.y_test)
                elapsed = time.time() - t0
                print(f"Gen {gen:2d} | Train: {mejor_f:.4f} | Test: {f_test:.4f} | Best: {self.mejor_fitness:.4f} | {elapsed:.1f}s")
            nueva = [evaluados[i][1].clone() for i in range(self.elitismo)]
            while len(nueva) < self.poblacion_size:
                p1 = random.choice(evaluados[:5])[1]
                p2 = random.choice(evaluados[:5])[1]
                hijo = self.factory()
                for c in range(len(p1.capas)):
                    for n in range(p1.capas[c].n_neuronas):
                        hijo.capas[c].pesos[n] = p1.capas[c].pesos[n] if random.random() < 0.5 else p2.capas[c].pesos[n]
                        hijo.capas[c].umbrales[n] = p1.capas[c].umbrales[n] if random.random() < 0.5 else p2.capas[c].umbrales[n]
                        hijo.capas[c].ops[n] = p1.capas[c].ops[n] if random.random() < 0.5 else p2.capas[c].ops[n]
                hijo.mutate(self.tasa_mutacion)
                nueva.append(hijo)
            self.poblacion = nueva
        f_final_train = self.evaluar(self.mejor_historico, self.X_train, self.y_train)
        f_final_test = self.evaluar(self.mejor_historico, self.X_test, self.y_test)
        print(f"\nFINAL | Train: {f_final_train:.4f} ({f_final_train*100:.1f}%) | Test: {f_final_test:.4f} ({f_final_test*100:.1f}%)")
        return self.mejor_historico


def ternarizar_mnist(imagen):
    flat = imagen.flatten()
    t = np.zeros(784, dtype=np.int8)
    t[flat < 85] = -1
    t[flat > 170] = 1
    return t


def cargar_mnist(n_train=1000, n_test=200):
    try:
        from sklearn.datasets import fetch_openml
        mnist_data = fetch_openml('mnist_784', version=1, parser='auto')
        x_all = mnist_data.data.values.reshape(-1, 28, 28).astype('uint8')
        y_all = mnist_data.target.astype(int).values
        x_train_full, y_train_full = x_all[:60000], y_all[:60000]
        x_test_full, y_test_full = x_all[60000:], y_all[60000:]
    except Exception as e:
        print(f"Error cargando MNIST: {e}")
        return None, None, None, None

    X_train = [ternarizar_mnist(x) for x in x_train_full[:n_train]]
    y_train = y_train_full[:n_train].tolist()
    X_test = [ternarizar_mnist(x) for x in x_test_full[:n_test]]
    y_test = y_test_full[:n_test].tolist()
    return X_train, y_train, X_test, y_test
