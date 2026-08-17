"""
ALGEBRA DEL TRES - Parte 3: Redes feedforward y evolucion generica
"""

from algebra_02_neuronas import *

class RedFeedforwardDelTres:
    def __init__(self, hidden_size: int = 2):
        self.hidden_size = hidden_size
        self.hidden = [NeuronaColapsanteV2(2) for _ in range(hidden_size)]
        self.output = NeuronaColapsanteV2(hidden_size)

    def forward(self, x1: int, x2: int) -> int:
        hidden_outs = [n.forward([x1, x2]) for n in self.hidden]
        return self.output.forward(hidden_outs)

    def evaluate(self, dataset):
        aciertos = sum(1 for x1, x2, esp in dataset if self.forward(x1, x2) == esp)
        return aciertos / len(dataset)

    def clone(self):
        r = RedFeedforwardDelTres(self.hidden_size)
        r.hidden = [n.clone() for n in self.hidden]
        r.output = self.output.clone()
        return r

    def mutate(self, tasa=0.15):
        for n in self.hidden:
            n.mutate(tasa)
        self.output.mutate(tasa)


class RedFragmentadaColapsante:
    def __init__(self, hidden_size=3, num_slots=3, num_steps=3):
        self.hidden_size = hidden_size
        self.num_slots = num_slots
        self.num_steps = num_steps
        self.hidden = [NeuronaFragmentadaColapsante(2, num_slots) for _ in range(hidden_size)]
        self.output = NeuronaFragmentadaColapsante(hidden_size, num_slots)

    def reset(self):
        for n in self.hidden:
            n.reset()
        self.output.reset()

    def forward(self, x1, x2):
        for _ in range(self.num_steps):
            hidden_outs = [n.forward([x1, x2]) for n in self.hidden]
            salida = self.output.forward(hidden_outs)
        return salida

    def evaluate(self, dataset):
        aciertos = 0
        for x1, x2, esp in dataset:
            self.reset()
            if self.forward(x1, x2) == esp:
                aciertos += 1
        return aciertos / len(dataset)

    def clone(self):
        r = RedFragmentadaColapsante(self.hidden_size, self.num_slots, self.num_steps)
        r.hidden = [n.clone() for n in self.hidden]
        r.output = self.output.clone()
        return r

    def mutate(self, tasa=0.15):
        for n in self.hidden:
            n.mutate(tasa)
        self.output.mutate(tasa)


class EvolucionGenerica:
    def __init__(self, factory, dataset, poblacion_size=300, generaciones=400,
                 tasa_mutacion=0.14, elitismo=5, nombre="Red"):
        self.factory = factory
        self.dataset = dataset
        self.poblacion_size = poblacion_size
        self.generaciones = generaciones
        self.tasa_mutacion = tasa_mutacion
        self.elitismo = elitismo
        self.nombre = nombre
        self.mejor_historico = None
        self.mejor_fitness = 0.0
        self.historia_mejor = []

    def inicializar(self):
        self.poblacion = [self.factory() for _ in range(self.poblacion_size)]

    def evaluar_poblacion(self):
        return [(red.evaluate(self.dataset), red) for red in self.poblacion]

    def seleccionar_torneo(self, evaluados, k=3):
        torneo = random.sample(evaluados, k)
        torneo.sort(key=lambda x: x[0], reverse=True)
        return torneo[0][1]

    def cruzar(self, p1, p2):
        hijo = self.factory()
        if hasattr(p1, 'hidden') and hasattr(p2, 'hidden'):
            for i in range(len(p1.hidden)):
                hijo.hidden[i] = p1.hidden[i].clone() if random.random() < 0.5 else p2.hidden[i].clone()
        if hasattr(p1, 'output') and hasattr(p2, 'output'):
            hijo.output = p1.output.clone() if random.random() < 0.5 else p2.output.clone()
        return hijo

    def evolucionar(self):
        self.inicializar()
        for gen in range(self.generaciones):
            evaluados = self.evaluar_poblacion()
            evaluados.sort(key=lambda x: x[0], reverse=True)
            mejor_f = evaluados[0][0]
            if mejor_f > self.mejor_fitness:
                self.mejor_fitness = mejor_f
                self.mejor_historico = evaluados[0][1].clone()
            self.historia_mejor.append(mejor_f)
            if gen % 25 == 0 or gen == self.generaciones - 1 or mejor_f >= 1.0:
                print(f"[{self.nombre}] Gen {gen:3d} | Mejor: {mejor_f:.4f} ({mejor_f*9:.0f}/9) | Hist: {self.mejor_fitness:.4f}")
            if mejor_f >= 1.0:
                print(f"\n[{self.nombre}] SOLUCION PERFECTA en gen {gen}!")
                break
            nueva = [evaluados[i][1].clone() for i in range(self.elitismo)]
            while len(nueva) < self.poblacion_size:
                p1 = self.seleccionar_torneo(evaluados, k=3)
                p2 = self.seleccionar_torneo(evaluados, k=3)
                hijo = self.cruzar(p1, p2)
                hijo.mutate(self.tasa_mutacion)
                nueva.append(hijo)
            self.poblacion = nueva
        return self.mejor_historico
