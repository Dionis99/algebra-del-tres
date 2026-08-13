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
