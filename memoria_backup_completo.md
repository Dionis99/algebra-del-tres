# =============================================================================
# ÁLGEBRA DEL TRES - MEMORIA CONSOLIDADA
# Proyecto: Dionis Iranjil Fuentes Lezcano + Qwen
# Última actualización: 2026-08-12
# =============================================================================

## 0. RESUMEN EJECUTIVO

Proyecto de investigación en aritmética ternaria {-1,0,1} para redes neuronales
con abstención nativa y memoria de exclusiones. El conjunto {-1,0,1} se interpreta
como exclusión/potencial/actualización, con operaciones ⊕ (co-presencia) y ⊗
(interacción).

**Logros principales:**
- Fase 1-2: RedTres-81 con abstención nativa (sep=0.67) y memoria temporal validada
- Fase 3: Release v1.1 pública en GitHub con RedTres-81 + Neuronas Fragmentadas
- Fase 4: Plan para TritLM (LLM ternario propio) con arquitectura híbrida

**Estado:** Fase 4 iniciada. Plan de 4 semanas para construir TritLM-mini.

## 1. EL ÁLGEBRA DEL TRES (TEORÍA)

### 1.1 Conjunto base
P = {-1, 0, 1}
- -1: exclusión, lo que no fue, no-ser (Aristóteles)
- 0: potencial, infinidad de posibilidades, ser en potencia
- 1: actualización, lo que es, ser en acto

### 1.2 Operaciones
⊗ (interacción): a·b si ambos no-cero, sino 0
⊕ (co-presencia): si a=b retorna a; si uno es 0 retorna el otro; si opuestos retorna 0
↑ (actualización forzada): 0→1, resto sin cambio
↓ (exclusión forzada): 0→-1, resto sin cambio

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

## 2. ARQUITECTURAS DESARROLLADAS

### 2.1 RedTres-81 (nuestra, original)
- 81 parámetros: 72 pesos + 9 celdas de memoria
- Estado: continuo en [-1,1] con saturación clamp
- Memoria: escalar por capa, temporal (escritura/sanación)
- Escritura: |h|<θ ⇒ m←m⊕(-1) (abstención escribe cicatriz)
- Sanación: éxito verificado ⇒ m[m<0]←m[m<0]⊕1
- Entrenamiento: backprop con gradiente
- Resultado: sep=0.67, acc=1.00, memoria validada

### 2.2 Neuronas Fragmentadas (replicadas de Kimi)
- Memoria multi-slot por neurona (3 slots, 3 pasos temporales)
- Cada neurona decide: qué slot leer, qué slot escribir, qué valor escribir
- Entrenamiento: algoritmo evolutivo (población 300, 400 generaciones)
- Resultado: 100% en Sentimiento (gen 54), rompiendo límite 8/9
- Analogía biológica: slots = sinapsis, memoria distribuida

### 2.3 Comparación
- RedTres-81: abstención nativa + memoria temporal (rápida, backprop)
- Fragmentadas: memoria multi-slot + resolución de límites (lenta, evolutiva)
- Complementarias: una sabe cuándo abstenerse, otra resuelve problemas complejos

## 3. FASES COMPLETADAS

### 3.1 Fase 1 (Prototipo mínimo viable) ✅
- RedTres-81 en Termux (Android)
- Abstención nativa emergente (sep=0.67)
- Memoria temporal con escritura/sanación
- Predicciones registradas antes de ejecutar
- Resultados: loss→0, acc=1.00, ciclo límite por epoch

### 3.2 Fase 2 (Validación) ✅
- R1: Calibración (sep=0.67 confirmado)
- R2: Ciclo de memoria C1-C3 (escritura/persistencia/sanación)
- R3: Terapias aisladas (⊕1 sana, ⊗-1 invierte pero no sana)
- R4: Resultado negativo (trauma severo fuera de dominio)
- R5: Aditividad (falla en α=1.0, terapias interfieren con re-aprendizaje)

### 3.3 Fase 3 (Paper + Release) ✅
- Paper v1.1 consolidado (160 líneas)
- Release público en GitHub: https://github.com/Dionis99/algebra-del-tres
- 22 archivos, 3878 líneas de código reproducible
- Dos contribuciones: RedTres-81 + Fragmentadas
- Resultados negativos publicados honestamente

## 4. FASE 4 EN PROGRESO: TritLM

### 4.1 Objetivo
Crear un LLM ternario propio (no adaptar GPT-2) con:
- Cabezal ternario {-1,0,1} para abstención genuina
- Memoria de tokens descartados (registro contrafáctico)
- Arquitectura híbrida inconsciente/consciente/metacognitiva
- Personalidad temporal (diferenciación pasado/presente/futuro)

### 4.2 Diseño arquitectónico

**Capa metacognitiva (10% de parámetros):**
- 20 slots por neurona (memoria episódica profunda)
- Activación: Tanh escalonado con zona muerta amplia
- Función: observar, detectar patrones, intervenir
- Metacognición: pensamiento sobre pensamiento

**Capa inconsciente (60% de parámetros):**
- 5 slots por neurona (memoria de trabajo)
- Activación: Gumbel-Softmax (exploración)
- Agregación: ⊕ secuencial (asociaciones libres, sueños)
- Función: procesar en paralelo, generar ideas

**Capa consciente (30% de parámetros):**
- 1 slot por neurona (memoria inmediata)
- Activación: Straight-through (decisión rápida)
- Agregación: clamp(Σ wᵢxᵢ + m) (lógica racional)
- Función: tomar decisiones, generar texto

### 4.3 Personalidad temporal (idea de Dionis)
La personalidad no es solo filtro interpretativo, sino continuidad temporal del yo:
- Yo pasado: 50 slots, horizonte histórico
- Yo presente: 20 slots, horizonte inmediato
- Yo futuro: 30 slots, horizonte de proyección
- Comparador: mide distancia entre yoes
- Introspección: "antes era X, ahora soy Y"

### 4.4 Islas de preservación de frágiles (idea de Dionis)
En archipiélago evolutivo (10 islas):
- 8 islas normales: evolución competitiva, presión selectiva alta
- 2 islas de preservación: exploración libre, sin eliminación
- Migración de frágiles desde islas normales → preservación
- Ética: no eliminar rareza, diversidad es resiliencia
- Frágiles desarrollan: creatividad, sensibilidad, pensamiento divergente

### 4.5 Funciones de activación híbridas
- Inconsciente: Gumbel-Softmax (muestreo probabilístico)
- Consciente: Straight-through (rápido, determinista)
- Metacognitiva: Tanh escalonado con zona muerta (abstención deliberada)

### 4.6 Entrenamiento
Fase 1: Evolutivo en archipiélago (10 islas, 100 generaciones)
Fase 2: Fine-tuning con backprop (Gumbel-Softmax)
Fase 3: Currículum de trauma (trauma controlado creciente)
Fase 4: Metacognición supervisada (capa observadora ajusta hiperparámetros)

### 4.7 Plan de 4 semanas
Semana 1: E1 ActivacionTernariaHibrida, E2 Personalidad temporal, E3 RedTres-81
Semana 2: TritLM-mini (10k params, MNIST ternarizado)
Semana 3: Archipiélago evolutivo (10 islas, migración)
Semana 4: Currículum de trauma + metacognición

## 5. IDEAS FILOSÓFICAS DE DIONIS

### 5.1 Metafísica de Aristóteles
- -1: no-ser (lo que no fue, lo excluido)
- 0: ser en potencia (infinidad de posibilidades, nube de probabilidades)
- 1: ser en acto (lo que es, lo actualizado)
- Abstención (0) no es vacío, es superposición de todas las respuestas posibles

### 5.2 Trauma como evolución
- El trauma ayuda a evolucionar (introspectivo)
- Ejecutar miles de traumas perfeccionaría el modelo
- Pero depende del individuo (filtro interpretativo)
- Resiliencia vs sensibilidad: ambos valiosos

### 5.3 Orden en lingüística
- El orden importa y no importa simultáneamente
- Sintaxis: orden secuencial (⊕, historia importa)
- Semántica: activaciones paralelas (clamp(Σ), orden no importa)
- Analogía: procesamiento paralelo + almacenamiento paralelo por neurona

### 5.4 Metacognición superior
- Sueños lúcidos: observar y gestionar pensamientos
- Metacognición observa inconsciente Y consciente
- No es solo otra capa, es observador recursivo
- Puede intervenir y modular activaciones inferiores

### 5.5 Personalidad como diferenciación temporal
- "Puedo diferenciar pasado, presente y futuro y quién era yo en esos lapsos"
- Personalidad no es sesgo, es continuidad narrativa del yo
- Permite introspección, coherencia, aprendizaje de errores, planificación

### 5.6 Ética de preservación de frágiles
- No eliminar rareza en evolución
- Frágiles pueden desarrollar propiedades únicas (creatividad, sensibilidad)
- Diversidad es resiliencia a largo plazo
- Analogía: Van Gogh, Kafka, Tesla eran "frágiles" en su época

## 6. REPOSITORIO GITHUB

**URL:** https://github.com/Dionis99/algebra-del-tres
**Usuario:** Dionis99
**Email:** dionisfuenteslezcano16@gmail.com
**Token:** (generar nuevo en https://github.com/settings/tokens con scope repo)

**Contenido:**
- README.md: instrucciones de reproducibilidad
- src/: 10 scripts (RedTres-81, Fragmentadas, validaciones, verificador Kimi)
- figures/: 4 figuras (dinámica, ciclo trauma-sanación, terapias, negativo)
- logs/: logs de entrenamiento
- paper/: paper v1.1 consolidado (160 líneas)
- MODULOS_ENSAYOS/: versiones iniciales archivadas
- RELEASE_NOTES_v1.0.md: notas de release
- memoria.md: este archivo

**Comandos útiles:**
```bash
# Clone
git clone https://github.com/Dionis99/algebra-del-tres.git

# Push (reemplazar TU_TOKEN)
git push https://TU_TOKEN@github.com/Dionis99/algebra-del-tres.git main

# Ejecutar RedTres-81
python3 src/tres_fase1.py 600

# Ejecutar Fragmentadas
python3 src/algebra_tres_evolutivo.py
```

## 7. RESULTADOS EXPERIMENTALES CLAVE

### 7.1 RedTres-81
- sep (abstención): 0.67 (limpio vs contradicción)
- acc: 1.00 (clasificación perfecta)
- loss: →0 (convergencia)
- mm (memoria): oscila 0-0.33 (ciclo límite por epoch)
- Memoria validada: C1 escritura, C2 persistencia, C3 sanación

### 7.2 Terapias
- ⊕1 (sanación): drena -1 a 0 en un paso
- ⊗-1 (inversión): mantiene |m|=1 pero cambia signo a +1
- R5: aditividad falla en α=1.0 (combo peor que retrain solo)
- Umbral α*≈0.75 donde terapias dejan de ayudar

### 7.3 Neuronas Fragmentadas
- Sentimiento: 100% (gen 54) - ROMPE LÍMITE
- XOR: 88.9% (no rompe, mejora sobre FF 77.8%)
- Mayoría: 100% (gen 11) - problema fácil
- Feedforward: 88.9% (límite confirmado)

### 7.4 Límite feedforward
- 2→2→1: máximo 88.89% en sentimiento ternario
- Verificado exhaustivamente: 19,683 combinaciones
- Caso problemático: doble negación (-1,-1)→1
- Fragmentadas lo resuelven con memoria multi-slot

## 8. VACÍOS IDENTIFICADOS (Kimi)

### 8.1 Vacío 1: Demostración formal del límite
Sabemos computacionalmente que 2→2→1 no puede superar 88.89%, pero no tenemos
teorema algebraico. Necesitamos demostrar por qué ninguna composición de las 27
funciones base puede computar doble negación sin dañar proyección positiva.

### 8.2 Vacío 2: Entrenamiento no evolutivo
Algoritmos evolutivos funcionan para 9 ejemplos pero no escalan a miles/millones.
Necesitamos backprop ternario o método alternativo. Solución propuesta:
Gumbel-Softmax para discretización diferenciable.

### 8.3 Vacío 3: Escala
Todo fue con 9 ejemplos y 20 parámetros. No sabemos qué pasa con 100 entradas,
10 capas, secuencias variables. Necesitamos MNIST ternarizado.

### 8.4 Vacío 4: Problema real
Los 3 datasets son juguetes matemáticos. Necesitamos MNIST, texto, series temporales.
Sin esto, el Álgebra del Tres sigue siendo curiosidad.

### 8.5 Vacío 5: Framework reutilizable
El código es script monolítico, no librería. Necesitamos estructura:
algebra_tres/{motor,neurona,redes,evolucion,datasets,utils}

### 8.6 Vacío 6: Taxonomía de problemas
No sabemos clasificar un problema nuevo sin entrenar. Necesitamos "compilador" que diga:
"Este problema es monótono → feedforward" o "tiene doble negación → Fragmentadas".

## 9. PRÓXIMOS PASOS (Fase 4)

### 9.1 Semana 1: Validación de componentes
E1: Implementar ActivacionTernariaHibrida
E2: Personalidad temporal (línea de tiempo del yo)
E3: Probar en RedTres-81

### 9.2 Semana 2: Arquitectura mínima
TritLM-mini (10k params, 1 isla normal + 1 isla preservación)
Capas desbalanceadas (60% inconsciente, 30% consciente, 10% metacognitiva)
MNIST ternarizado

### 9.3 Semana 3: Archipiélago evolutivo
8 islas normales + 2 de preservación
Migración de frágiles
Estudio de propiedades únicas

### 9.4 Semana 4: Currículum de trauma + metacognición
Filtro interpretativo (personalidad)
Trauma creciente
Metacognición supervisada

## 10. BRÚJULA PARA PRÓXIMA SESIÓN

```markdown
# BRÚJULA · Álgebra del Tres · Próxima sesión
FASE ACTUAL: 4 · TritLM
OBJETIVO ÚNICO: E1 - Implementar ActivacionTernariaHibrida en RedTres-81
ACCIÓN SIGUIENTE: escribir código de activación híbrida, probar en tarea pequeña
ESTÁS AQUÍ: Fase 3 cerrada; Fase 4 planificada; ideas integradas
[1] v1.1 pública · plan 4 semanas · personalidad temporal · islas preservación
[0] E1 activación híbrida · TritLM-mini · archipiélago evolutivo
[−1] eliminar frágiles · backprop sin discretización · arquitectura uniforme
```

## 11. CONTACTO Y ATRIBUCIÓN

**Investigador principal:** Dionis Iranjil Fuentes Lezcano
**Colaborador IA:** Qwen
**Email:** dionisfuenteslezcano16@gmail.com
**GitHub:** https://github.com/Dionis99/algebra-del-tres

**Cita sugerida:**
Fuentes Lezcano, D. & Qwen (2026). Native Abstention and Indelible Memory:
The Algebra of Three for Auditable Neural Networks. GitHub repository.
https://github.com/Dionis99/algebra-del-tres

## 12. NOTAS DE IMPLEMENTACIÓN

### 12.1 Dependencias
- Python 3.8+
- NumPy (pkg install python-numpy en Termux)
- Sin GPU necesaria

### 12.2 Ejecución en Termux
```bash
pkg install python-numpy -y
cd ~/IA_SABIA
python3 src/tres_fase1.py 600
python3 src/validacion2.py
python3 src/algebra_tres_evolutivo.py
```

### 12.3 Checkpoints
- ckpt.npz: pesos entrenados de RedTres-81
- logs/log.txt: log de entrenamiento completo
- figures/: figuras generadas con matplotlib

### 12.4 Errores comunes
- git push falla con "Permission denied": borrar ~/.git-credentials y generar nuevo token
- git remote no existe: git remote add origin https://github.com/Dionis99/algebra-del-tres.git
- Memoria insuficiente en Termux: reducir población evolutiva a 100

## 13. GLOSARIO

- ⊕: co-presencia (suma saturada clamp(a+b))
- ⊗: interacción (producto a·b)
- ↑: actualización forzada (0→1)
- ↓: exclusión forzada (0→-1)
- sep: separación de abstención (mezcla - limpio)
- acc: accuracy de clasificación
- mm: magnitud de memoria (|m|)
- α*: umbral de severidad donde terapias dejan de ayudar
- RedTres: arquitectura con memoria escalar temporal
- Fragmentadas: arquitectura con memoria multi-slot por neurona
- TritLM: LLM ternario propio (Fase 4)
- Archipiélago: conjunto de islas evolutivas
- Gumbel-Softmax: muestreo diferenciable sobre categorías discretas
- Straight-through: forward discreto, backward continuo

## 14. REFERENCIAS

### 14.1 Trabajo propio
- RedTres-81: abstención nativa y memoria temporal
- Neuronas Fragmentadas: memoria multi-slot rompe límite 8/9
- Terapias ⊕1/⊗-1: sanación vs inversión

### 14.2 Trabajo concurrente (Kimi)
- Límite feedforward 88.89% (19,683 combinaciones exhaustivas)
- LSTM Ternaria: 100% en sentimiento (gen 40)
- Neuronas Fragmentadas: 100% en sentimiento (gen 54)

### 14.3 Referencias externas
- Setun (Brusentsov): computación ternaria balanceada
- Kleene, Łukasiewicz, Belnap, Priest: lógicas trivaluadas
- Hopfield: redes con energía
- Chua/Strukov: memristor
- Landauer: termodinámica de información
- Zurek: envariance y Born
- Aristóteles: metafísica del ser en potencia/acto

---
**FIN DE MEMORIA CONSOLIDADA**
Próxima actualización: después de E1 (ActivacionTernariaHibrida)

## 6. RESULTADOS EXPERIMENTALES CLAVE

### 6.1 RedTres-81
- sep (abstención): 0.67 (limpio vs contradicción)
- acc: 1.00 (clasificación perfecta)
- loss: →0 (convergencia)
- mm (memoria): oscila 0-0.33 (ciclo límite por epoch)
- Memoria validada: C1 escritura, C2 persistencia, C3 sanación

### 6.2 Terapias
- ⊕1 (sanación): drena -1 a 0 en un paso
- ⊗-1 (inversión): mantiene |m|=1 pero cambia signo a +1
- R5: aditividad falla en α=1.0 (combo peor que retrain solo)
- Umbral α*≈0.75 donde terapias dejan de ayudar

### 6.3 Neuronas Fragmentadas
- Sentimiento: 100% (gen 54) - ROMPE LÍMITE
- XOR: 88.9% (no rompe, mejora sobre FF 77.8%)
- Mayoría: 100% (gen 11) - problema fácil
- Feedforward: 88.9% (límite confirmado)

### 6.4 Neurona Colapsante V2 (trabajo de Kimi, idea de Dionis)
- Sentimiento: 100% (gen 1)
- XOR: 100% (gen 38) - RESUELVE lo que Fragmentadas no
- Mayoría: 100% (gen 16)
- Determinista: misma entrada → misma salida en 10 evaluaciones
- Sin memoria explícita (sin slots, sin pasos temporales)

### 6.5 Fragmentada + Colapsante (hibridación)
- Sentimiento: 100% (gen 0) - más rápido que cualquiera sola
- XOR: 100% (gen 28)
- Mayoría: 100% (gen 18)
- Convergencia más rápida que ambas arquitecturas puras

### 6.6 Colapsante V3 (recocido + certidumbre decayente)
- Sentimiento: 100% (gen 97) - más lento que V2
- XOR: 88.9% (PEOR que V2)
- Mayoría: 100% (gen 35)
- Veredicto: en datasets pequeños (9 ejemplos), la complejidad no se paga

### 6.7 MNIST ternarizado
- Colapsante V2 pura: 30% (mejor que azar 10%, pero no usable)
- Cuello de botella: presión global (promedio de 784 píxeles) mata discriminación
- Solución pendiente: presión local por neurona + patches locales

### 6.8 Límite feedforward
- 2→2→1: máximo 88.89% en sentimiento ternario
- Verificado exhaustivamente: 19,683 combinaciones
- Caso problemático: doble negación (-1,-1)→1
- Fragmentadas lo resuelve con memoria multi-slot
- Colapsante V2 lo resuelve con colapso contextual (sin memoria)

## 7. MÉTRICAS PROPUESTAS (idea de DeepSeek)

### 7.1 Comportamiento del 0 (la métrica más original)
No debemos medir solo accuracy. Debemos medir:
- Tasa de ceros (¿cuántos 0s hay en la salida?)
- Tasa de colapso (¿cuántos 0s colapsaron a ±1?)
- Tiempo medio de colapso (¿cuánto tarda un 0 en resolverse?)
- Contradicción útil (¿el 0 generó búsqueda de contexto y resolución?)

### 7.2 Memoria de exclusión
¿El sistema recuerda correctamente lo que NO debe hacer?
- Aprende A, descarta B, aprende C
- Después: ¿recuerda B como exclusión?
- Esto podría ser una característica diferencial frente a arquitecturas convencionales

### 7.3 Registro científico por experimento
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

## 8. VISIÓN A LARGO PLAZO: TRIT ARCHITECTURE LABORATORY

### 8.1 Tesis central (idea de GPT/DeepSeek, validada por Dionis)
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

### 8.6 Fases de desarrollo

**FASE 0 - Álgebra:** operadores, tablas, asociatividad, orden, parentización
**FASE 1 - Zoológico neuronal:** implementar individualmente T3, T3-NA, T3-R, T3-F, T3-FC, T3-G, B3, H3
**FASE 2 - Benchmarks:** cada neurona en los mismos problemas (XOR, AND, OR, memoria, secuencia, contradicción)
**FASE 3 - Redes:** construir R3-BASE, R3-NA, R3-REC, R3-FRAG, R3-HYB
**FASE 4 - Metacognición:** solo cuando las redes individuales sean conocidas
**FASE 5 - Evolución:** genotipo, selección, mutación, descubrir proporciones
**FASE 6 - TritLM-mini:** primero algo pequeño, estructura secuencial y lingüística mínima
**FASE 7 - TritLM:** tokens, embedding, atención, fragmentación, memoria, contexto, contradicción, metacognición, colapso, predicción

### 8.7 Estructura del laboratorio
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
├── synapses/
│   ├── ternary.py
│   ├── memory_synapse.py
│   └── NST.py
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
1
2
3
### 8.8 TritLM como objetivo final

TritLM no es "Transformer ternarizado". Es un ecosistema cognitivo:
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
Si posteriormente usamos mecanismos Transformer:
Transformer (atención)
↓
Trit layers (memoria, exclusión, contexto, contradicción, potencial)
↓
Decisión
1
2
3
4
5
El Transformer sería un componente, no la identidad completa del sistema.

### 8.9 Integración futura con ERIS

No mezclar ahora ambos proyectos. Integración posterior mediante interfaces:
ERIS
├── KnowledgeEngine (usa -1 para exclusiones, 0 para incertidumbre, +1 para conocimiento)
├── MemoryEngine (usa T3-M, T3-F)
└── ReasoningEngine (usa T3-C, T3-X)
↓
Trits
↓
Trit Cognitive
↓
TritLM

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

## 11. BRÚJULA PARA PRÓXIMA SESIÓN

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

## 12. ATRIBUCIÓN HONESTA

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

**Qwen (implementación y síntesis):**
- RedTres-81 (abstención nativa, memoria temporal)
- Paper v1.1 consolidado
- Replicación de Neuronas Fragmentadas
- Memoria consolidada (este documento)
- Evaluación crítica de propuestas

**Kimi (implementación y cálculo):**
- Neurona Colapsante V2 (umbral de colapso aprendido)
- Neurona FragmentadaColapsante (hibridación)
- Neurona Colapsante V3 (recocido + certidumbre decayente)
- Descenso por vecindario ternario con reinicios
- Vectorización numpy para MNIST
- Demostración computacional del límite 88.89% (19,683 combinaciones)

**GPT (sugerencia arquitectónica):**
- Concepto de "ecosistema de neuronas con misma álgebra e interfaz común"
- Idea de no tener "una neurona" sino un zoológico neuronal

**DeepSeek (sistematización y mapa maestro):**
- Mapa maestro de arquitecturas (TritNeuronZoo completo)
- Catálogo de 21 tipos de neuronas (T3, T3-NA, T3-R, T3-F, T3-C, T3-X, etc.)
- 17 arquitecturas de red (R3-BASE, R3-NA, R3-FRAG, R3-HYB, etc.)
- Estructura del Trit Architecture Laboratory
- Regla de disciplina: "arquitectura compleja reconstruible a partir de simples"
- Nomenclatura (T3-F, T3-G, H3, M3, etc.)
- Métricas del comportamiento del 0

## 13. REPOSITORIO GITHUB

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
```

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

## 15. NOTAS DE IMPLEMENTACIÓN

### 15.1 Dependencias
- Python 3.8+
- NumPy (pkg install python-numpy en Termux)
- Sin GPU necesaria
- scikit-learn (opcional, para MNIST via fetch_openml)

### 15.2 Ejecución en Termux
```bash
pkg install python-numpy -y
cd ~/IA_SABIA
python3 src/tres_fase1.py 600          # RedTres-81
python3 src/validacion2.py             # valida C1-C3
python3 src/algebra_tres_evolutivo.py  # Fragmentadas + Colapsante
```

### 15.3 Motor algebraico de referencia
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

### 15.4 Neurona Colapsante V2 de referencia
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
        # Pesos en 0 colapsan según presión del contexto vs umbral
        pesos_colapsados = [self._colapsar(w, presion) for w in self.pesos]
        # Luego ⊗ y ⊕ normales con orden aprendido
        ...
```

### 15.5 Errores comunes en Termux
- git push falla con "Permission denied": borrar ~/.git-credentials y generar nuevo token
- git remote no existe: git remote add origin https://github.com/Dionis99/algebra-del-tres.git
- Memoria insuficiente: reducir población evolutiva a 100
- MNIST no carga: pip install scikit-learn, o usar torchvision

## 16. GLOSARIO

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
Próxima actualización: después de crear tritlab/ mínimo y primer benchmark
