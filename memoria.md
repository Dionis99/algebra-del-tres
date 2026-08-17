# =============================================================================
# ÁLGEBRA DEL TRES - MEMORIA CONSOLIDADA COMPLETA
# Proyecto: Dionis Iranjil Fuentes Lezcano + Qwen + Kimi + GPT + DeepSeek
# Última actualización: 2026-08-12
# Versión: 2.0 (reconstruida limpia)
# =============================================================================

## 0. RESUMEN EJECUTIVO

Proyecto de investigación en aritmética ternaria {-1,0,1} para redes neuronales con
abstención nativa y memoria de exclusiones. El conjunto {-1,0,1} se interpreta como
exclusión/potencial/actualización (o no-ser/ser-en-potencia/ser-en-acto según Aristóteles).

**Logros principales:**
- Fase 1-2: RedTres-81 con abstención nativa (sep=0.67) y memoria temporal validada
- Fase 3: Release v1.1 pública en GitHub con RedTres-81 + Neuronas Fragmentadas
- Trabajo concurrente (Kimi): Neurona Colapsante V2 que rompe límites sin memoria explícita
- Hibridación Fragmentada + Colapsante: convergencia más rápida en todos los datasets
- Fase 4: Plan para TritLM (LLM ternario propio) con arquitectura híbrida
- Visión aceptada: Trit Architecture Laboratory (ecosistema de neuronas)

**Estado:** Fase 3 cerrada. Transición a Fase 4 con laboratorio modular mínimo.

## 1. TEORÍA DEL ÁLGEBRA DEL TRES

### 1.1 Conjunto base
P = {-1, 0, 1}

### 1.2 Operaciones
⊗ (interacción): a·b si ambos no-cero, sino 0
  -1 ⊗ -1 = 1 (doble negación → afirmación)
   0 ⊗ x = 0 (potencialidad no interactúa sin definirse)

⊕ (co-presencia): si a=b retorna a; si uno es 0 retorna el otro; si opuestos retorna 0
  -1 ⊕ 1 = 0 (conflicto → potencialidad, tríada hegeliana)
   0 ⊕ 0 = 0 (potencialidad pura se mantiene)

↑ (actualización forzada): 0→1, resto sin cambio (téleosis)
↓ (exclusión forzada): 0→-1, resto sin cambio (vía negativa)

### 1.3 Propiedades
- ⊕ es conmutativa pero NO asociativa (asociador en 4 triples ordenados)
- ⊗ es asociativa y distributiva sobre ⊕
- Neutros: 0 para ⊕, 1 para ⊗
- Absorbente: 0 para ⊗

### 1.4 Teoremas clave
- Teo 1 (monoide físico): |M|=17 de 27 transformaciones posibles
- Teo 2 (memoria indeleble): m←m⊕(-1) es absorbente (-1⊕-1=-1)
- Teo 3 (forma continua): ds/dt=-s+tanh(κ(Js+h)), κ=1 crítico
- Teo 4 (límite feedforward): 2→2→1 máximo 88.89% en sentimiento ternario
- Teo 5 (Fragmentadas rompen límite): memoria multi-slot alcanza 100% en gen 54
- Teo 6 (Colapsante V2 rompe límite): colapso contextual alcanza 100% sin memoria explícita

## 2. ONTOLOGÍA E IDEAS FILOSÓFICAS DE DIONIS

### 2.1 Metafísica aristotélica aplicada
- **-1**: No-ser, lo que no fue, pasado negado, ausencia
- **0**: Ser en potencia, burbuja de infinitas posibilidades, devenir
- **1**: Ser en acto, lo que es, lo que ocurrió de la burbuja del 0

### 2.2 El 0 como recurso computacional (intuición clave de Dionis)
"El 0 al inicio es indeterminado e inestable porque podría ser cualquier cosa. Con el
tiempo, cuando la neurona aprende, esa elección se reduce por lo que aprende."

Esto inspiró el concepto de **umbral de colapso**: un parámetro aprendido que determina
cuándo la potencialidad (0) se actualiza como afirmación (1) o negación (-1) según el
contexto. La reducción de indeterminación es literalmente el proceso de aprendizaje.

### 2.3 Especialización y saber (intuición de Dionis)
"¿La manera de interpretar el mundo está relacionada por el tamaño del saber y conocer
de cada individuo?"

- Un músico ve patrones armónicos donde otros ven ruido
- Un matemático ve estructuras lógicas donde otros ven símbolos
- El mismo input produce outputs diferentes porque los umbrales aprendidos son diferentes
- La especialización está en los umbrales de colapso y valores de slots
- Es literalmente "ver el mundo con otros ojos"

### 2.4 Memoria contextual (intuición de Dionis)
Los slots de memoria no son archivos que recuperas idénticos. Son sueños que reconstruyes.
Cada vez que lees un slot, colapsa de manera distinta según:
- Quién pregunta (el contexto actual)
- Cómo preguntas (la presión del entorno)
- Cuándo preguntas (la certidumbre decayente)

Esto modela la memoria humana: no recuerdas lo que guardaste, recuerdas lo que la
situación actual te obliga a recordar.

### 2.5 Personalidad temporal (intuición de Dionis)
La personalidad no es solo filtro interpretativo, sino continuidad temporal del yo:
- Yo pasado: 50 slots, horizonte histórico
- Yo presente: 20 slots, horizonte inmediato
- Yo futuro: 30 slots, horizonte de proyección
- Comparador: mide distancia entre yoes
- Introspección: "antes era X, ahora soy Y"

### 2.6 Islas de preservación de frágiles (idea de Dionis)
En archipiélago evolutivo (10 islas):
- 8 islas normales: evolución competitiva, presión selectiva alta
- 2 islas de preservación: exploración libre, sin eliminación
- Migración de frágiles desde islas normales → preservación
- Ética: no eliminar rareza, diversidad es resiliencia
- Frágiles desarrollan: creatividad, sensibilidad, pensamiento divergente

### 2.7 Traumaterapia como evolución (intuición de Dionis)
"El trauma me hizo introspectivo. ¿Ejecutar miles de traumas perfeccionaría el modelo?"
- Trauma leve → sanación rápida, aprendizaje
- Trauma severo → colapso, terapias no ayudan
- Propuesta: entrenamiento con trauma controlado creciente (currículum de trauma)

### 2.8 Orden en lingüística (intuición de Dionis)
- El orden importa y no importa simultáneamente
- Sintaxis: orden secuencial (⊕, historia importa)
- Semántica: activaciones paralelas (clamp(Σ), orden no importa)
- Analogía: procesamiento paralelo + almacenamiento paralelo por neurona

### 2.9 Metacognición superior (experiencia de Dionis)
- Sueños lúcidos: observar y gestionar pensamientos
- Metacognición observa inconsciente Y consciente
- No es solo otra capa, es observador recursivo
- Puede intervenir y modular activaciones inferiores

## 3. ARQUITECTURAS DESARROLLADAS

### 3.1 RedTres-81 (Dionis + Qwen, original)
- 81 parámetros: 72 pesos + 9 celdas de memoria
- Estado: continuo en [-1,1] con saturación clamp
- Memoria: escalar por capa, temporal (escritura/sanación)
- Escritura: |h|<θ ⇒ m←m⊕(-1) (abstención escribe cicatriz)
- Sanación: éxito verificado ⇒ m[m<0]←m[m<0]⊕1
- Entrenamiento: backprop con gradiente
- Resultado: sep=0.67, acc=1.00, memoria validada
- **Ventaja:** Abstención nativa emergente, rápida inferencia
- **Limitación:** No rompe límite feedforward en problemas complejos

### 3.2 Neuronas Fragmentadas (Dionis + Qwen, replicadas de Kimi)
- Memoria multi-slot por neurona (3 slots, 3 pasos temporales)
- Cada neurona decide: qué slot leer, qué slot escribir, qué valor escribir
- Entrenamiento: algoritmo evolutivo (población 300, 400 generaciones)
- Resultado: 100% en Sentimiento (gen 54), rompiendo límite 8/9
- Analogía biológica: slots = sinapsis, memoria distribuida
- **Ventaja:** Rompe límites feedforward con memoria explícita
- **Limitación:** Lenta inferencia (3 pasos temporales), requiere reinicio de slots

### 3.3 Neurona Colapsante V2 (Dionis conceptual + Kimi implementó)
**Innovación clave de Dionis:** "El 0 es una burbuja de infinitas posibilidades que
colapsa según el contexto. El umbral de colapso es el 'saber' de la neurona."

Implementación de Kimi:
```python
class NeuronaColapsanteV2:
    def __init__(self, num_inputs):
        self.pesos = [random.choice(P) for _ in range(num_inputs)]
        self.umbral_colapso = random.uniform(-0.9, 0.9)  # "saber" aprendido
    
    def _colapsar(self, peso, presion):
        if peso != 0: return peso
        return 1 if presion > self.umbral_colapso else -1
    
    def forward(self, entradas):
        presion = sum(entradas) / len(entradas)
        pesos_colapsados = [self._colapsar(w, presion) for w in self.pesos]
        # Luego ⊗ y ⊕ normales con orden aprendido
```

- Sin memoria explícita (sin slots, sin pasos temporales)
- Determinista: misma entrada → misma salida siempre
- Resultado: 100% en Sentimiento (gen 1), XOR (gen 38), Mayoría (gen 16)
- **Ventaja:** Rompe límites sin memoria, inferencia rápida, determinista
- **Limitación:** Colapso determinista traiciona parcialmente la ontología del 0

### 3.4 Neurona Fragmentada + Colapsante (hibridación sugerida por Dionis)
**Idea de Dionis:** "¿Se puede mezclar la memoria fragmentada con la nueva teoría?"

Implementación de Kimi:
```python
class NeuronaFragmentadaColapsante:
    def __init__(self, num_inputs, num_slots=3):
        self.slots = [0] * num_slots
        self.read = NeuronaColapsanteV2(num_inputs)   # qué slot leer
        self.out = NeuronaColapsanteV2(num_inputs + 1) # qué computar
        self.write = NeuronaColapsanteV2(num_inputs)  # dónde escribir
        self.val = NeuronaColapsanteV2(num_inputs)    # qué escribir
```

- Memoria contextual: no recuerdas archivos fijos, reconstruyes sueños
- Resultado: 100% en los 3 datasets, convergencia más rápida que cualquiera sola
- **Ventaja:** Combina lo mejor de ambas (memoria + colapso contextual)
- **Limitación:** Más compleja, más parámetros

### 3.5 Neurona Colapsante V3 (Dionis conceptual + Kimi implementó)
**Idea de Dionis:** "La burbuja debe estrecharse durante el entrenamiento (temperatura
decayente), y los slots deben tener certidumbre decayente (memoria que se olvida)."

- Colapso con temperatura: alta al inicio (exploración), baja al final (explotación)
- Slots con certidumbre: 1.0 (recuerda claro) → 0.0 (olvidó todo)
- Presión local: cada neurona calcula su propio contexto
- Resultado: 100% en Sentimiento (gen 97) y Mayoría (gen 35), pero 88.9% en XOR (peor que V2)
- **Veredicto:** En datasets pequeños, la complejidad no se paga. Necesita muchos datos.

### 3.6 Comparación de arquitecturas

| Arquitectura | Sentimiento | XOR | Mayoría | Memoria | Inferencia | Complejidad |
|--------------|-------------|-----|---------|---------|------------|-------------|
| Feedforward pura | 88.9% | 77.8% | 88.9% | No | Rápida | Baja |
| RedTres-81 | 100% | - | - | Temporal | Rápida | Media |
| Fragmentadas | 100% | 88.9% | 100% | Multi-slot | Lenta | Alta |
| Colapsante V2 | 100% | 100% | 100% | No | Rápida | Baja |
| Fragmentada+Colapsante | 100% | 100% | 100% | Multi-slot | Media | Alta |
| Colapsante V3 | 100% | 88.9% | 100% | No | Rápida | Alta |

**Ganadora para TritLM:** Colapsante V2 (simple, rápida, rompe límites, determinista)

## 4. RESULTADOS EXPERIMENTALES CLAVE

### 4.1 RedTres-81
- sep (abstención): 0.67 (limpio vs contradicción)
- acc: 1.00 (clasificación perfecta)
- loss: →0 (convergencia)
- mm (memoria): oscila 0-0.33 (ciclo límite por epoch)
- Memoria validada: C1 escritura, C2 persistencia, C3 sanación

### 4.2 Terapias
- ⊕1 (sanación): drena -1 a 0 en un paso
- ⊗-1 (inversión): mantiene |m|=1 pero cambia signo a +1
- R5: aditividad falla en α=1.0 (combo peor que retrain solo)
- Umbral α*≈0.75 donde terapias dejan de ayudar

### 4.3 Neuronas Fragmentadas
- Sentimiento: 100% (gen 54) - ROMPE LÍMITE
- XOR: 88.9% (no rompe, mejora sobre FF 77.8%)
- Mayoría: 100% (gen 11) - problema fácil
- Feedforward: 88.9% (límite confirmado)

### 4.4 Neurona Colapsante V2 (idea de Dionis, implementada por Kimi)
- Sentimiento: 100% (gen 1)
- XOR: 100% (gen 38) - RESUELVE lo que Fragmentadas no
- Mayoría: 100% (gen 16)
- Determinista: misma entrada → misma salida en 10 evaluaciones
- Sin memoria explícita (sin slots, sin pasos temporales)

### 4.5 Fragmentada + Colapsante (hibridación)
- Sentimiento: 100% (gen 0) - más rápido que cualquiera sola
- XOR: 100% (gen 28)
- Mayoría: 100% (gen 18)
- Convergencia más rápida que ambas arquitecturas puras

### 4.6 Colapsante V3 (recocido + certidumbre decayente)
- Sentimiento: 100% (gen 97) - más lento que V2
- XOR: 88.9% (PEOR que V2)
- Mayoría: 100% (gen 35)
- Veredicto: en datasets pequeños (9 ejemplos), la complejidad no se paga

### 4.7 MNIST ternarizado
- Colapsante V2 pura: 30% (mejor que azar 10%, pero no usable)
- Cuello de botella: presión global (promedio de 784 píxeles) mata discriminación
- Solución pendiente: presión local por neurona + patches locales

### 4.8 Límite feedforward
- 2→2→1: máximo 88.89% en sentimiento ternario
- Verificado exhaustivamente: 19,683 combinaciones
- Caso problemático: doble negación (-1,-1)→1
- Fragmentadas lo resuelve con memoria multi-slot
- Colapsante V2 lo resuelve con colapso contextual (sin memoria)

### 4.9 Descenso por vecindario ternario
- Método determinista alternativo al backpropagation
- Con 50 reinicios aleatorios toca el techo teórico en los 3 datasets
- O(n*p*3) por época, viable para redes pequeñas
- Sin reinicios se atasca en óptimos locales

## 5. MÉTRICAS PROPUESTAS (idea de DeepSeek)

### 5.1 Comportamiento del 0 (la métrica más original)
No debemos medir solo accuracy. Debemos medir:
- Tasa de ceros (¿cuántos 0s hay en la salida?)
- Tasa de colapso (¿cuántos 0s colapsaron a ±1?)
- Tiempo medio de colapso (¿cuánto tarda un 0 en resolverse?)
- Contradicción útil (¿el 0 generó búsqueda de contexto y resolución?)

### 5.2 Memoria de exclusión
¿El sistema recuerda correctamente lo que NO debe hacer?
- Aprende A, descarta B, aprende C
- Después: ¿recuerda B como exclusión?
- Esto podría ser una característica diferencial frente a arquitecturas convencionales

### 5.3 Registro científico por experimento
```json
{
  "modelo": "...",
  "version": "...",
  "dataset": "...",
  "semilla": "...",
  "tipo_neurona": "...",
  "memoria": true,
  "contexto": 0.3,
  "temperatura": 0.7,
  "tasa_ceros": "...",
  "tasa_colapso": "...",
  "contradicciones": "...",
  "accuracy": "...",
  "loss": "...",
  "memoria_retencion": "...",
  "trauma": "...",
  "sanacion": "...",
  "tiempo": "..."
}
```

## 6. FASES COMPLETADAS

### 6.1 Fase 1 (Prototipo mínimo viable) ✅
- RedTres-81 en Termux (Android)
- Abstención nativa emergente (sep=0.67)
- Memoria temporal con escritura/sanación
- Predicciones registradas antes de ejecutar
- Resultados: loss→0, acc=1.00, ciclo límite por epoch

### 6.2 Fase 2 (Validación) ✅
- R1: Calibración (sep=0.67 confirmado)
- R2: Ciclo de memoria C1-C3 (escritura/persistencia/sanación)
- R3: Terapias aisladas (⊕1 sana, ⊗-1 invierte pero no sana)
- R4: Resultado negativo (trauma severo fuera de dominio)
- R5: Aditividad (falla en α=1.0, terapias interfieren con re-aprendizaje)

### 6.3 Fase 3 (Paper + Release) ✅
- Paper v1.1 consolidado (160 líneas)
- Release público en GitHub: https://github.com/Dionis99/algebra-del-tres
- 22 archivos, 3878 líneas de código reproducible
- Dos contribuciones: RedTres-81 + Fragmentadas
- Resultados negativos publicados honestamente

## 7. FASE 4 EN PROGRESO: TritLM

**Objetivo:** Crear un LLM ternario propio con arquitectura cognitiva avanzada.

**Plan original (4 semanas):**
- Semana 1: E1 ActivacionTernariaHibrida, E2 Personalidad temporal, E3 RedTres-81
- Semana 2: TritLM-mini (10k params, MNIST ternarizado)
- Semana 3: Archipiélago evolutivo (10 islas, migración)
- Semana 4: Currículum de trauma + metacognición

**Plan revisado (incorporando ideas de DeepSeek y visión ecosistema):**
- Semana 1: Crear tritlab/ mínimo (algebra/, neurons/, datasets/, benchmarks/)
- Semana 2: Primer benchmark (T3, T3-NA, T3-R en los 3 datasets)
- Semana 3: Añadir Colapsante V2, Fragmentada, Híbrida al laboratorio
- Semana 4: MNIST con presión local
- Semana 5-8: TritLM-mini con arquitectura cognitiva completa

**Arquitectura base para TritLM:**
Embedding de tokens (ternario)
→ Capa 1 (Local): Trit Fragmentadas (memoria fina, patrones locales)
→ Capa 2 (Intermedia): Fragmentadas Colapsantes (integración contextual)
→ Capa 3 (Global): Colapsantes Globales (síntesis de alto nivel)
→ Capa 4 (Decisión): Binarias de decisión (emisión de token)
→ Cabezal ternario {-1,0,1} (abstención, exclusión, actualización)
Metacognición global:
Observa entropía, tasa de colapso, contradicciones
Ajusta radios de contexto y temperatura de colapso
Implementa curriculum learning automáticamente
1
**TritLM no es "Transformer ternarizado".** Es un ecosistema cognitivo:
Embedding ternario
↓
Fragmentación (T3-F)
↓
Asociación no asociativa (T3-NA)
↓
Memoria (T3-M)
↓
Contexto (T3-G)
↓
Contradicción (T3-C)
↓
Metacognición (M3)
↓
Colapso (T3-G)
↓
Decisión (B3)
↓
Token
1
2
3
4
5
6
7
8
9
## 8. VISIÓN A LARGO PLAZO: TRIT ARCHITECTURE LABORATORY

### 8.1 Tesis central (idea de GPT, validada por Dionis)
"Álgebra del Tres no debería tener 'una neurona'. Debería tener un ecosistema de
neuronas compatibles con una misma álgebra, una misma interfaz y diferentes
capacidades cognitivas."

El proyecto no es "una red neuronal ternaria". Es un **ecosistema cognitivo ternario**
con jerarquía de escalas:
SINAPSIS → NEURONA → RED → METACOGNICIÓN → EVOLUCIÓN → TIEMPO
### 8.2 Catálogo de neuronas (TritNeuronZoo)

**Nivel 0 - Fundamental:**
- T3 (NeuronaDelTres): pesos ternarios, ⊗ y ⊕ secuencial, salida ternaria

**Nivel 1 - Estructura:**
- T3-NA (NoAsociativa): orden τ + árbol de parentización
- T3-O (Orden): aprende el orden de composición

**Nivel 2 - Tiempo:**
- T3-R (Recurrente): y_t = f(x_t, m_{t-1}), memoria temporal
- T3-T (Temporal): detecta secuencias, ciclos, cambios

**Nivel 3 - Memoria:**
- T3-M (MemoriaEscalar): una sola memoria
- T3-MC (MemoriaColectiva): varias neuronas comparten estado
- T3-ME (MemoriaExclusiones): guarda "esto fue probado y descartado"
- T3-F (Fragmentada): memoria multi-slot

**Nivel 4 - Contexto y Colapso:**
- T3-FC (FragmentadaColapsante): memoria + colapso contextual
- T3-G (ColapsanteGlobal): contexto amplio, síntesis
- T3-H (ColapsanteAdaptativa): umbral dinámico θ=f(contexto,memoria,error)

**Nivel 5 - Funciones cognitivas:**
- T3-C (Contradicción): detecta a⊕b=0, pregunta "¿incertidumbre o contradicción?"
- T3-X (Exclusión): especializada en -1, trabaja con KnowledgeEngine
- T3-P (Potencial): maximiza conservación de 0, anti-alucinación
- T3-D (Dendrítica): subgrupos de entradas como ramas
- T3-E (Ensemble): múltiples neuronas internas con consenso
- T3-LSTM: TritLSTM con compuertas ternarias/binarias

**Nivel 6 - Control:**
- M3 (Metacognitiva): observa entropía, tasa de 0s, contradicciones, ajusta parámetros
- B3 (Binaria): decisión {-1,+1}, ejecuta, clasifica

**Nivel 7 - Híbridas:**
- H3 (Híbrida): ternario + binario en capas alternas
- T3-NST (Neurona-Sinapsis-Ternaria): sinapsis=(w_i, m_i), separa peso/memoria/orden/activación

### 8.3 Arquitectura jerárquica de una neurona completa (TritCognitiveCell)
ENTRADAS
↓
RECEPTIVA (filtrado, atención)
↓
ASOCIATIVA (⊕ con orden y parentización)
↓
MEMORIA LOCAL + MEMORIA EXCLUSIÓN
↓
CONTEXTUAL (presión local/intermedia/global)
↓
¿COLAPSAR 0?
↙       ↘
NO        SÍ
↓         ↓
EXPRESIVA
↓
-1 / 0 / +1
↓
TERNARIA o BINARIA
METACOGNICIÓN (fuera de la neurona):
Observa entropía, tasa de 0s, contradicciones
Ajusta: radio de contexto, temperatura de colapso, activación de memoria
### 8.4 Redes principales a construir

| Red | Composición | Objetivo |
|-----|-------------|----------|
| R3-BASE | T3 → T3 → T3 | Baseline, medir aporte del álgebra pura |
| R3-NA | T3-NA con árboles | Medir aporte de la parentización |
| R3-REC | T3-R recurrente | Temporalidad, memoria |
| R3-FRAG | 60% T3-F + 30% T3-FC + 10% T3-G | Ecosistema bebé→adulto |
| R3-HYB | Ternario → Binario → Ternario → Binario | Pensar→filtrar→reinterpretar→decidir |
| R3-NST | Sinapsis con peso+memoria | Investigación central |
| R3-CONT | Detección de contradicciones | Razonamiento |
| R3-EVO | Archipiélago evolutivo | Evolución descubre proporciones |

### 8.5 Reglas fundamentales del laboratorio

1. **Ningún modelo debe destruir otro.** Cada neurona es un módulo independiente.
2. **Una arquitectura compleja debe ser reconstruible a partir de simples.** Si no, no sabemos qué produjo qué.
3. **Las arquitecturas no compiten inmediatamente.** Primero se prueban individualmente.
4. **60/30/10 es una hipótesis, no un dogma.** La evolución debe descubrir proporciones.
5. **El comportamiento del 0 es la métrica principal.** No solo accuracy.

### 8.6 Estructura del laboratorio
tritlab/
├── algebra/
│   ├── operators.py        (⊗, ⊕, ↑, ↓, tablas)
│   ├── order.py            (τ, árboles de composición)
│   └── truth_tables.py
├── neurons/
│   ├── base.py             (interfaz común: forward, update, state, diagnostics, reset)
│   ├── ternary.py          (T3)
│   ├── non_associative.py  (T3-NA)
│   ├── recurrent.py        (T3-R)
│   ├── fragmented.py       (T3-F)
│   ├── collapsing.py       (T3-G)
│   ├── hybrid.py           (T3-FC)
│   ├── binary.py           (B3)
│   ├── lstm.py             (T3-LSTM)
│   ├── contradiction.py    (T3-C)
│   ├── exclusion.py        (T3-X)
│   ├── potential.py        (T3-P)
│   ├── temporal.py         (T3-T)
│   ├── dendritic.py        (T3-D)
│   ├── ensemble.py         (T3-E)
│   └── metacognitive.py    (M3)
├── memory/
│   ├── scalar.py
│   ├── multislot.py
│   ├── collective.py
│   └── exclusions.py
├── networks/
│   ├── red_tres.py         (R3-BASE)
│   ├── non_associative.py  (R3-NA)
│   ├── recurrent.py        (R3-REC)
│   ├── fragmented.py       (R3-FRAG)
│   ├── hybrid.py           (R3-HYB)
│   ├── contradiction.py    (R3-CONT)
│   └── evolutionary.py     (R3-EVO)
├── metacognition/
│   └── regulator.py
├── evolution/
│   ├── genetic.py
│   ├── archipelago.py
│   └── neighborhood_descent.py
├── datasets/
│   ├── sentimiento.py
│   ├── xor.py
│   ├── mayoria.py
│   └── mnist.py
├── benchmarks/
│   ├── run_baseline.py
│   ├── run_all_neurons.py
│   └── compare_architectures.py
└── experiments/
└── (registros JSON de cada experimento)

## 9. PLAN DE EJECUCIÓN INMEDIATO (lo que hacemos AHORA)

### 9.1 Inventario honesto: qué está validado vs qué es hipótesis

**VALIDADO (tenemos código que funciona y resultados medidos):**
- T3 básica (NeuronaDelTres): 19,683 combinaciones, límite 88.89%
- RedTres-81: sep=0.67, acc=1.00, memoria C1-C3 validada
- Fragmentada: 100% Sentimiento (gen 54), 88.9% XOR
- Colapsante V2: 100% en los 3 datasets, determinista
- FragmentadaColapsante: 100% en los 3 datasets, convergencia rápida
- Evolución genérica: funciona con cualquier arquitectura
- Descenso por vecindario: toca el techo con 50 reinicios

**HIPÓTESIS (ideas sin código o sin validación):**
- T3-NA (no asociativa con árboles): no implementada
- T3-R (recurrente): no implementada
- T3-C, T3-X, T3-P, T3-D, T3-E, T3-T, T3-O: solo conceptos
- M3 (metacognición): solo concepto
- T3-NST: solo concepto
- Proporción 60/30/10: hipótesis, no probada
- TritLM: no existe todavía
- MNIST >60%: no logrado (actual 30%)

### 9.2 La regla de disciplina (la más importante del proyecto)

"Una arquitectura compleja debe ser reconstruible a partir de arquitecturas simples."

Esto significa:
- NO construir las 21 neuronas antes de validar ninguna en un problema real
- NO construir TritLM antes de que el laboratorio mínimo funcione
- NO añadir metacognición antes de que las redes individuales sean conocidas
- Cada componente nuevo debe justificar su existencia con un experimento

Si violamos esta regla, tendremos un monstruo que funciona (o no) y no sabremos por qué.

### 9.3 Plan inmediato (próximas 4 semanas)

**SEMANA 1: Laboratorio mínimo**
- Crear estructura tritlab/ (solo algebra/, neurons/, datasets/, benchmarks/)
- Implementar algebra/operators.py (⊗, ⊕, ↑, ↓ con tablas)
- Implementar algebra/order.py (árboles de parentización)
- Implementar neurons/base.py (interfaz común)
- Implementar neurons/ternary.py (T3 básica, ya la tenemos)
- Implementar neurons/non_associative.py (T3-NA, casi trivial sobre T3)
- Implementar neurons/recurrent.py (T3-R)
- Implementar datasets/ (sentimiento, xor, mayoria)
- Implementar benchmarks/run_baseline.py

**SEMANA 2: Primer benchmark**
- Correr T3, T3-NA, T3-R en los 3 datasets
- Medir: ¿la parentización aporta algo en XOR o Sentimiento?
- Medir: ¿la recurrencia aporta algo?
- Registrar resultados en JSON
- Decidir: ¿T3-NA justifica su existencia?

**SEMANA 3: Añadir Colapsante V2 al laboratorio**
- Implementar neurons/collapsing.py (T3-G, ya la tenemos de Kimi)
- Implementar neurons/fragmented.py (T3-F, ya la tenemos)
- Implementar neurons/hybrid.py (T3-FC, ya la tenemos)
- Correr benchmark comparativo: T3 vs T3-G vs T3-F vs T3-FC
- Medir comportamiento del 0 (tasa de ceros, tasa de colapso)

**SEMANA 4: MNIST con presión local**
- Corregir presión global → presión local por neurona
- Probar Colapsante V2 en MNIST con presión local
- Objetivo: >60% (actual 30%)
- Si funciona: el álgebra escala, procedemos a TritLM-mini
- Si no funciona: necesitamos patches locales o convolución ternaria

### 9.4 Lo que explícitamente NO hacemos todavía

- NO implementamos las 21 neuronas del zoo (solo las 6 que ya tenemos + T3-NA + T3-R)
- NO construimos TritLM hasta que MNIST pase de 60%
- NO añadimos metacognición hasta que las redes individuales estén caracterizadas
- NO integramos con ERIS hasta que TritLM-mini funcione
- NO probamos proporciones 60/30/10 hasta tener el ecosistema mínimo

### 9.5 Decisión arquitectónica: Colapsante V2 como neurona base de TritLM

**Razones:**
- Rompe límites sin memoria explícita (inferencia rápida)
- Es determinista (misma entrada → misma salida)
- Es simple (un umbral de colapso por neurona)
- Valida la ontología del 0 como burbuja contextual (idea de Dionis)

**Limitaciones reconocidas:**
- El colapso determinista traiciona parcialmente la ontología del 0 (debería ser indeterminado al inicio)
- La presión global mata discriminación en MNIST (hay que corregir a presión local)
- No tiene memoria explícita (si TritLM necesita memoria, usamos FragmentadaColapsante)

**Plan B:** Si Colapsante V2 no escala a MNIST, usamos FragmentadaColapsante (memoria + colapso).

## 10. VACÍOS CRÍTICOS Y CÓMO LLENARLOS

### 10.1 Vacíos resueltos

| Vacío | Estado | Cómo se resolvió |
|-------|--------|------------------|
| Límite feedforward en XOR | RESUELTO | Colapsante V2 alcanza 100% |
| Límite feedforward en Sentimiento | RESUELTO | Colapsante V2 alcanza 100% |
| Estabilidad del colapso | RESUELTO | Umbral determinista aprendido |
| Entrenamiento no evolutivo | PARCIAL | Descenso por vecindario + reinicios |

### 10.2 Vacíos pendientes críticos

| Vacío | Prioridad | Propuesta |
|-------|-----------|-----------|
| Presión local por neurona | ALTA | Cada neurona calcula presión sobre sus entradas activas |
| Escalabilidad a MNIST | ALTA | Red 784→64→10 con Colapsante V2 |
| Colapso con temperatura | MEDIA | Indeterminación que decrece con el entrenamiento |
| Slots en superposición | MEDIA | Los slots mismos colapsan al leerse |
| Demostración formal del poder expresivo | MEDIA | Probar que Colapsante V2 computa funciones fuera del semigrupo |
| Ternarización adaptativa | MEDIA | Aprender umbrales de discretización |
| Framework reutilizable | MEDIA | Librería pip-installable |
| Backpropagation ternario | BAJA | Descenso por vecindario es suficiente para redes pequeñas |

### 10.3 Errores detectados en implementaciones anteriores

**Error A: Colapso determinista vs ontología indeterminista**
Dijimos "0 es una burbuja de infinitas posibilidades" pero forzamos colapso determinista.
Solución: NeuronaColapsanteV3 con temperatura decayente (recocido simulado ternario).
Estado: implementada pero no mejoró en datasets pequeños. Necesita muchos datos.

**Error B: Presión global en MNIST**
presion = x.mean() promedia los 784 píxeles. Con MNIST ternarizado, la mayoría son 0,
así que presion ≈ 0 siempre. El umbral se vuelve irrelevante.
Solución: presión local por neurona (solo sobre entradas con pesos no nulos).
Estado: pendiente de implementar.

**Error C: Ternarización arbitraria**
Umbrales fijos (85, 170). Un píxel de 84 → -1, uno de 86 → 0. Discontinuidad no natural.
Solución: ternarización adaptativa (cada neurona aprende sus umbrales) o usar el píxel
flotante como presión sin discretizar.
Estado: pendiente de decidir.

**Error D: Slots en superposición no implementados**
Los slots son [0,0,0] fijos. Pero si 0 es "burbuja de posibilidades", un slot en 0 debería
colapsar según el contexto al leerse.
Solución: slots con certidumbre decayente (memoria que se olvida).
Estado: implementado en V3 pero no mejoró en datasets pequeños.

## 11. REPOSITORIO GITHUB

**URL:** https://github.com/Dionis99/algebra-del-tres
**Usuario:** Dionis99
**Email:** dionisfuenteslezcano16@gmail.com

**Contenido actual (v1.1):**
- README.md: instrucciones de reproducibilidad
- src/: 10 scripts (RedTres-81, Fragmentadas, validaciones, verificador Kimi)
- figures/: 4 figuras (dinámica, ciclo trauma-sanación, terapias, negativo)
- logs/: logs de entrenamiento
- paper/: paper v1.1 consolidado (160 líneas)
- memoria.md: este archivo
- MODULOS_ENSAYOS/: versiones iniciales archivadas

**Comandos útiles:**
```bash
# Push (reemplazar TU_TOKEN con token de GitHub)
git push https://TU_TOKEN@github.com/Dionis99/algebra-del-tres.git main

# Generar nuevo token si falla auth
# Ir a: https://github.com/settings/tokens → Generate new token (classic) → scope repo

# Borrar credenciales incorrectas del caché
rm ~/.git-credentials
```

## 12. NOTAS DE IMPLEMENTACIÓN

### 12.1 Dependencias
- Python 3.8+
- NumPy (pkg install python-numpy en Termux)
- Sin GPU necesaria
- scikit-learn (opcional, para MNIST via fetch_openml)

### 12.2 Ejecución en Termux
```bash
pkg install python-numpy -y
cd ~/IA_SABIA
python3 src/tres_fase1.py 600          # RedTres-81
python3 src/validacion2.py             # valida C1-C3
python3 src/algebra_tres_evolutivo.py  # Fragmentadas + Colapsante
```

### 12.3 Motor algebraico de referencia
```python
P = [-1, 0, 1]

def interaction(a, b):
    """⊗: interacción. 0 anula; si no, producto clásico."""
    if a == 0 or b == 0: return 0
    return a * b

def copresence(a, b):
    """⊕: co-presencia. Igual refuerza; 0 deja pasar; opuestos → 0."""
    if a == b: return a
    if a == 0: return b
    if b == 0: return a
    return 0

def up(x): return 1 if x == 0 else x      # actualización forzada
def down(x): return -1 if x == 0 else x   # exclusión forzada
```

### 12.4 Neurona Colapsante V2 de referencia
```python
class NeuronaColapsanteV2:
    def __init__(self, num_inputs):
        self.pesos = [random.choice(P) for _ in range(num_inputs)]
        self.umbral_colapso = random.uniform(-0.9, 0.9)  # el "saber" aprendido
    
    def _colapsar(self, peso, presion):
        if peso != 0: return peso
        return 1 if presion > self.umbral_colapso else -1
    
    def forward(self, entradas):
        presion = sum(entradas) / max(len(entradas), 1)
        pesos_colapsados = [self._colapsar(w, presion) for w in self.pesos]
        # Luego ⊗ y ⊕ normales con orden aprendido
```

### 12.5 Errores comunes en Termux
- git push falla con "Permission denied": borrar ~/.git-credentials y generar nuevo token
- git remote no existe: git remote add origin https://github.com/Dionis99/algebra-del-tres.git
- Memoria insuficiente: reducir población evolutiva a 100
- MNIST no carga: pip install scikit-learn, o usar torchvision

## 13. GLOSARIO

- **⊕**: co-presencia (suma saturada clamp(a+b))
- **⊗**: interacción (producto a·b, 0 es absorbente)
- **↑**: actualización forzada (0→1)
- **↓**: exclusión forzada (0→-1)
- **sep**: separación de abstención (mezcla - limpio)
- **acc**: accuracy de clasificación
- **mm**: magnitud de memoria (|m|)
- **α***: umbral de severidad donde terapias dejan de ayudar
- **RedTres**: arquitectura con memoria escalar temporal
- **Fragmentada**: arquitectura con memoria multi-slot por neurona
- **Colapsante V2**: arquitectura con colapso contextual de pesos en 0
- **FragmentadaColapsante**: hibridación memoria + colapso
- **TritLM**: LLM ternario propio (Fase 4-7)
- **TritNeuronZoo**: catálogo de neuronas con interfaz común
- **tritlab**: laboratorio modular de arquitecturas
- **Archipiélago**: conjunto de islas evolutivas
- **Gumbel-Softmax**: muestreo diferenciable sobre categorías discretas
- **Straight-through**: forward discreto, backward continuo
- **T3**: nomenclatura para neurona ternaria básica
- **B3**: neurona binaria de decisión
- **H3**: neurona híbrida ternario/binaria
- **M3**: neurona metacognitiva
- **NST**: Neurona-Sinapsis-Ternaria (peso + memoria + orden + activación)

## 14. REFERENCIAS

### 14.1 Trabajo propio del proyecto
- RedTres-81: abstención nativa y memoria temporal
- Neuronas Fragmentadas: memoria multi-slot rompe límite 8/9
- Neurona Colapsante V2: colapso contextual rompe límite sin memoria
- Terapias ⊕1/⊗-1: sanación vs inversión

### 14.2 Referencias externas
- Setun (Brusentsov): computación ternaria balanceada
- Kleene, Łukasiewicz, Belnap, Priest: lógicas trivaluadas y paraconsistentes
- Hopfield: redes con energía
- Chua/Strukov: memristor
- Landauer: termodinámica de información
- Zurek: envariance y regla de Born
- Aristóteles: metafísica del ser en potencia/acto (Metafísica Θ)
- Hegel: tríada dialéctica (tesis-antítesis-síntesis)

## 15. BRÚJULA PARA PRÓXIMA SESIÓN

```markdown
# BRÚJULA · Álgebra del Tres · Próxima sesión
FASE ACTUAL: Transición Fase 3→4 (cerrando paper, abriendo laboratorio)
OBJETIVO ÚNICO: Crear tritlab/ mínimo y correr primer benchmark (T3, T3-NA, T3-R)
ACCIÓN SIGUIENTE: generar algebra/operators.py + neurons/base.py + neurons/ternary.py
ESTÁS AQUÍ: memoria consolidada; visión ecosistema aceptada; disciplina establecida
[1] v1.1 pública · Colapsante V2 validada · visión TritNeuronZoo aceptada
[0] tritlab mínimo · benchmark T3/T3-NA/T3-R · MNIST con presión local
[−1] construir las 21 neuronas de golpe · TritLM antes de MNIST>60% · mega-arquitectura
```

**Al iniciar la próxima sesión, el asistente debe:**
1. Leer este memoria.md completo (pegar en contexto)
2. Confirmar que entiende la regla de disciplina (sección 9.2)
3. Empezar por el laboratorio mínimo (semana 1 del plan, sección 9.3)
4. NO construir TritLM ni las 21 neuronas hasta validar baselines

**Protocolo de reanudación:**
- El usuario pega la brújula al inicio
- El asistente lee memoria.md completo
- El asistente confirma: "Entiendo. Empezamos con tritlab/ mínimo, sección 9.3 semana 1."
- Si el asistente intenta construir algo fuera del plan, el usuario dice: "revisa memoria.md sección 9.2"

## 16. ATRIBUCIÓN HONESTA

Este proyecto es una colaboración multi-agente donde las ideas semilla y la dirección
filosófica son de Dionis, y la implementación/cálculo es de los asistentes.

**Dionis Iranjil Fuentes Lezcano (ideas y dirección):**
- Ontología aristotélica del {-1, 0, 1} (no-ser, ser-en-potencia, ser-en-acto)
- El 0 como "burbuja de infinitas posibilidades" (intuición central)
- El umbral de colapso como "saber" que reduce indeterminación
- Especialización músico/matemático (ver el mundo con otros ojos)
- Memoria contextual (los slots como sueños que se reconstruyen)
- Personalidad temporal (diferenciación pasado/presente/futuro del yo)
- Islas de preservación de frágiles (ética de no eliminar rareza)
- Hibridación Fragmentada + Colapsante (pregunta "¿se pueden mezclar?")
- Traumaterapia como evolución ("el trauma ayuda a evolucionar")
- Sugerencia de mezclar neuronas binarias en otra capa
- Visión de arquitectura cognitiva con metacognición reguladora

**Qwen (implementación y síntesis):**
- RedTres-81 (abstención nativa, memoria temporal)
- Paper v1.1 consolidado
- Replicación de Neuronas Fragmentadas
- Memoria consolidada (este documento)
- Evaluación crítica de propuestas
- Verificación de resultados y honestidad sobre limitaciones

**Kimi (implementación y cálculo):**
- Neurona Colapsante V2 (umbral de colapso aprendido)
- Neurona FragmentadaColapsante (hibridación)
- Neurona Colapsante V3 (recocido + certidumbre decayente)
- Descenso por vecindario ternario con reinicios
- Vectorización numpy para MNIST
- Demostración computacional del límite 88.89% (19,683 combinaciones)
- Informe completo del Álgebra del Tres

**GPT (sugerencia arquitectónica):**
- Concepto de "ecosistema de neuronas con misma álgebra e interfaz común"
- Idea de no tener "una neurona" sino un zoológico neuronal
- Visión de escalas jerárquicas (sinapsis → neurona → red → metacognición → evolución)

**DeepSeek (sistematización y mapa maestro):**
- Mapa maestro de arquitecturas (TritNeuronZoo completo)
- Catálogo de 21 tipos de neuronas (T3, T3-NA, T3-R, T3-F, T3-C, T3-X, etc.)
- 17 arquitecturas de red (R3-BASE, R3-NA, R3-FRAG, R3-HYB, etc.)
- Estructura del Trit Architecture Laboratory
- Regla de disciplina: "arquitectura compleja reconstruible a partir de simples"
- Nomenclatura (T3-F, T3-G, H3, M3, etc.)
- Métricas del comportamiento del 0
- Arquitectura de 5 capas internas de una neurona (receptiva, asociativa, mnémica, contextual, expresiva)

## 17. PRINCIPIO RECTOR DEL PROYECTO

La inteligencia emergería no de eliminar el 0, sino de aprender:
- cuándo conservarlo (proteger la posibilidad)
- cuándo alimentarlo con contexto (buscar más evidencia)
- cuándo convertirlo en -1 (exclusión, lo que no fue)
- cuándo convertirlo en +1 (actualización, lo que es)

El 0 no es fracaso. Es el espacio donde vive el devenir.

---
**FIN DE MEMORIA CONSOLIDADA**
Generado: 2026-08-12
Versión: 2.0 (reconstruida limpia)
Próxima actualización: después de crear tritlab/ mínimo y primer benchmark
