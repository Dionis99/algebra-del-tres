import numpy as np
import random

P = [-1, 0, 1]

def copresence(a, b):
    """a ⊕ b: co-presencia (síntesis dialéctica)"""
    if a == b: return a
    if a == 0: return b
    if b == 0: return a
    return 0  # opuestos → 0

def interaction(a, b):
    """a ⊗ b: interacción (producto)"""
    return a * b if a != 0 and b != 0 else 0

def apply_op(val, op):
    """Aplica operación unaria ↑, ↓, o id"""
    if op is None: return val
    if op == 'up': return 1 if val == 0 else val
    if op == 'down': return -1 if val == 0 else val
    return val

class NeuronaTres:
    """Neurona básica del Tres con pesos ternarios"""
    def __init__(self, num_inputs, op=None):
        self.num_inputs = num_inputs
        self.pesos = [random.choice(P) for _ in range(num_inputs)]
        self.op = op
    
    def forward(self, entradas):
        resultado = 0
        for i, x in enumerate(entradas):
            term = interaction(self.pesos[i], x)
            resultado = copresence(resultado, term)
        return apply_op(resultado, self.op)

class LSTM_Tres:
    """LSTM Ternaria con compuertas de olvido/entrada"""
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        
        # Compuerta de olvido f_t: decide si mantener C anterior
        self.f_gate = NeuronaTres(input_size + hidden_size, op=None)
        
        # Compuerta de entrada i_t: decide si actualizar C
        self.i_gate = NeuronaTres(input_size + hidden_size, op=None)
        
        # Candidato para nueva memoria
        self.c_candidate = NeuronaTres(input_size + hidden_size, op=None)
        
        # Salida h_t desde C_t
        self.output_gate = NeuronaTres(hidden_size, op=None)
        
        # Estado interno
        self.C = [0] * hidden_size  # estado de celda
        self.h = [0] * hidden_size  # estado oculto
    
    def forward(self, x):
        """Procesa una entrada y actualiza estado"""
        # Concatena input con estado oculto anterior
        concat = x + self.h
        
        # Computa compuertas
        f_val = self.f_gate.forward(concat)
        i_val = self.i_gate.forward(concat)
        c_new = self.c_candidate.forward(concat)
        
        # Actualiza estado de celda C_t
        for i in range(self.hidden_size):
            # Lógica de compuerta de olvido
            if f_val == -1:
                # Mantener celda anterior
                pass
            elif f_val == 1:
                # Reemplazar con candidato
                self.C[i] = c_new
            elif f_val == 0:
                # Combinar (⊕)
                self.C[i] = copresence(self.C[i], c_new)
            
            # Lógica de compuerta de entrada
            if i_val == 1:
                # Incorporar candidato (⊕)
                self.C[i] = copresence(self.C[i], c_new)
            elif i_val == -1:
                # Invertir celda (⊗ con -1)
                self.C[i] = interaction(self.C[i], -1)
        
        # Computa salida h_t desde C_t
        self.h = [self.output_gate.forward([self.C[i]]) for i in range(self.hidden_size)]
        
        return self.h
    
    def reset(self):
        """Reinicia estado interno"""
        self.C = [0] * self.hidden_size
        self.h = [0] * self.hidden_size
    
    def get_params(self):
        """Devuelve todos los pesos como lista"""
        params = []
        params.extend(self.f_gate.pesos)
        params.extend(self.i_gate.pesos)
        params.extend(self.c_candidate.pesos)
        params.extend(self.output_gate.pesos)
        return params
    
    def set_params(self, params):
        """Carga pesos desde lista"""
        idx = 0
        n1 = self.input_size + self.hidden_size
        n2 = self.hidden_size
        
        self.f_gate.pesos = params[idx:idx+n1]; idx += n1
        self.i_gate.pesos = params[idx:idx+n1]; idx += n1
        self.c_candidate.pesos = params[idx:idx+n1]; idx += n1
        self.output_gate.pesos = params[idx:idx+n2]

# Dataset de sentimiento ternario (de Kimi)
dataset_sentimiento = [
    ([-1, -1], 1),   # Doble negación → positivo
    ([-1, 0], -1),   # Negativo + neutro → negativo
    ([-1, 1], 0),    # Negativo + positivo → conflicto
    ([0, -1], -1),   # Neutro + negativo → negativo
    ([0, 0], 0),     # Neutro + neutro → neutro
    ([0, 1], 1),     # Neutro + positivo → positivo
    ([1, -1], 0),    # Positivo + negativo → conflicto
    ([1, 0], 1),     # Positivo + neutro → positivo
    ([1, 1], 1),     # Positivo + positivo → positivo
]

def evaluar_lstm(lstm, dataset):
    """Evalúa LSTM en dataset"""
    aciertos = 0
    for x, y_true in dataset:
        lstm.reset()
        h = lstm.forward(x)
        # Decisión: signo de la suma de h
        y_pred = 1 if sum(h) > 0 else (-1 if sum(h) < 0 else 0)
        if y_pred == y_true:
            aciertos += 1
    return aciertos / len(dataset)

# Algoritmo evolutivo simple
def entrenar_evolutivo(pop_size=100, generations=200, mutation_rate=0.1):
    """Entrena LSTM con algoritmo evolutivo"""
    input_size = 2
    hidden_size = 3
    
    # Inicializa población
    poblacion = []
    for _ in range(pop_size):
        lstm = LSTM_Tres(input_size, hidden_size)
        poblacion.append(lstm)
    
    best_fitness = 0
    best_lstm = None
    
    for gen in range(generations):
        # Evalúa fitness
        fitness = [evaluar_lstm(lstm, dataset_sentimiento) for lstm in poblacion]
        
        # Encuentra mejor
        max_idx = fitness.index(max(fitness))
        if fitness[max_idx] > best_fitness:
            best_fitness = fitness[max_idx]
            best_lstm = LSTM_Tres(input_size, hidden_size)
            best_lstm.set_params(poblacion[max_idx].get_params())
        
        print(f"Gen {gen}: best={best_fitness:.2%}, avg={sum(fitness)/len(fitness):.2%}")
        
        if best_fitness >= 1.0:
            print(f"¡Convergencia en generación {gen}!")
            break
        
        # Selección y reproducción
        nueva_poblacion = []
        
        # Elitismo: mantiene los 5 mejores
        sorted_idx = sorted(range(len(fitness)), key=lambda i: fitness[i], reverse=True)
        for i in range(5):
            nueva_poblacion.append(poblacion[sorted_idx[i]])
        
        # Resto: cruza + mutación
        while len(nueva_poblacion) < pop_size:
            # Selección por torneo
            p1 = poblacion[random.choice(sorted_idx[:20])]
            p2 = poblacion[random.choice(sorted_idx[:20])]
            
            # Cruza uniforme
            params1 = p1.get_params()
            params2 = p2.get_params()
            hijo_params = [random.choice([p1, p2]) for p1, p2 in zip(params1, params2)]
            
            # Mutación
            for i in range(len(hijo_params)):
                if random.random() < mutation_rate:
                    hijo_params[i] = random.choice(P)
            
            hijo = LSTM_Tres(input_size, hidden_size)
            hijo.set_params(hijo_params)
            nueva_poblacion.append(hijo)
        
        poblacion = nueva_poblacion
    
    return best_lstm, best_fitness

if __name__ == "__main__":
    print("Entrenando LSTM Ternaria en dataset sentimiento...")
    best_lstm, best_fitness = entrenar_evolutivo(pop_size=100, generations=200)
    
    print(f"\nMejor fitness alcanzado: {best_fitness:.2%}")
    
    # Evalúa en detalle
    print("\nEvaluación detallada:")
    best_lstm.reset()
    for x, y_true in dataset_sentimiento:
        best_lstm.reset()
        h = best_lstm.forward(x)
        y_pred = 1 if sum(h) > 0 else (-1 if sum(h) < 0 else 0)
        match = "✓" if y_pred == y_true else "✗"
        print(f"  {x} → pred={y_pred}, true={y_true} {match}")
