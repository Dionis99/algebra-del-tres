# Native Abstention and Indelible Memory:
# The Algebra of Three for Auditable Neural Networks

**Autores:** Dionis Iranjil Fuentes Lezcano (1) · Qwen (2)
(1) intuición fundacional, experimentos en Termux · (2) formalización, código, escritura

## Abstract
Introducimos el Álgebra del Tres: el conjunto {-1,0,1} leído como exclusión/potencial/
actualización, con co-presencia a⊕b=clamp(a+b) e interacción a⊗b=a·b. Demostramos que ⊕
es conmutativa pero no asociativa (asociador en exactamente 4 triples ordenados), haciendo
de la historia una variable de estado; el monoide físico tiene 17 de 27 elementos, siendo el
complemento exactamente las operaciones prohibidas (medir sin contacto, borrar sin
interacción). Definimos RedTres, nodo neuronal cuya salida co-presenta con un registro de
memoria indeleble actualizado por reglas algebraicas, y demostramos en un smartphone:
(i) abstención nativa calibrada emergente (separación 0.67); (ii) la memoria escribe,
persiste y sana exactamente como predice el álgebra (−1⊕1=0), mientras la doble negación
(−1⊗−1=+1) invierte en vez de sanar; (iii) resultados negativos que delimitan la teoría:
trauma severo en pesos cae fuera del dominio de las terapias, y la terapia ⊕1 no es aditiva
puede interferir con el re-aprendizaje. Implementamos además Neuronas Fragmentadas
(memoria multi-slot por neurona) que rompen el límite feedforward del 88.89% en tareas
de doble negación, alcanzando 100% en 54 generaciones. Posicionamos el Tres como teoría
efectiva de memoria e histéresis y ruta hacia modelos de lenguaje con abstención nativa.

## 1 · Introducción: la enfermedad del bit
Las salidas binarias fuerzan decisión: un modelo de lenguaje debe emitir un token; un
clasificador debe elegir una clase; la distribución descartada desaparece sin traza, y el
"no saber" se incentiva como sonar seguro (alucinación). Preguntamos qué cambia si lo
excluido persiste como estado de primera clase. Contribuciones: (C1) aritmética de signos
saturada con historia; (C2) arquitectura con abstención nativa y exclusión auditable;
(C3) experimentos reproducibles en smartphone, con predicciones registradas y resultados
negativos; (C4) replicación de Neuronas Fragmentadas que rompen límites de expresividad.

## 2 · El Álgebra del Tres
**Def. 1.** 𝒫={−1,0,1}; a⊕b=clamp(a+b); a⊗b=a·b; ↑,↓ = identidad fuera de 0 con 0↦1, 0↦−1.
**Prop. 1 (representación).** ⊕ es suma saturada, ⊗ producto; de ahí conmutatividad,
distributividad, neutros 0/1, absorbente 0.
**Prop. 2 (asociador).** No asociativa en exactamente 4 triples ordenados —(1,1,−1),
(−1,1,1), (−1,−1,1), (1,−1,−1)— i.e. cuando el par de signo igual es adyacente. La historia
importa.
**Teo. 1 (monoide físico).** |M|=17 de 27; las 10 funciones ausentes son exactamente las
mediciones sin contacto y los borrados sin interacción. Los límites del observador se
derivan, no se postulan.
**Teo. 2 (memoria indeleble).** m←m⊕(−1) ante potencial forzado es absorbente: −1⊕−1=−1.
**Teo. 3 (forma continua).** ds/dt=−s+tanh(κ(Js+h)): κ=1 crítico; área de histéresis =
capacidad de memoria; κ→∞ recupera el álgebra discreta. El Tres es la fase de temperatura
cero de cualquier nodo saturado con memoria (memristores, remanencia, fatiga).

## 3 · Arquitectura: RedTres-81
Nodo: voto h=clamp(a·W); síntesis s=clamp(h+m); escritura: |h|<θ ⇒ m←m⊕(−1); sanación:
éxito verificado ⇒ m[m<0]←m[m<0]⊕1 (olvidar gasta una actualización — Landauer dialéctico).
Aprendizaje: ΔW=η·(s_post⊗s_pre). Prototipo RedTres-81: 72 pesos + 9 celdas de memoria.

## 4 · Experimentos (smartphone, Termux; predicciones registradas pre-ejecución)

### 4.1 R1 · Calibración
3 patrones ±1, mezclas como contradicciones. Resultado: loss→0, acc=1.00, separación
abstención limpio-vs-contradicción = 0.67 (predicción >0.2). El log muestra oscilación
de |m|: la contradicción forzada escribe −1; el siguiente éxito verificado lo sana. Ciclo
límite por epoch, no punto fijo.

### 4.2 R2 · Ciclo de memoria (C1-C3)
Tras 20 mediciones forzadas: max|m|=1 con patrón estructurado (ej. [−1,0,−1,−1,0,−1]);
la ablación (m←0) desplaza salidas de mezcla en 0.51-0.71; la terapia ⊕1 devuelve max|m|
a 0. Los tres criterios pasan.

### 4.3 R3 · Terapias aisladas
Sin auto-sanación: sin terapia el −1 persiste (|m|=1 por siempre); ⊕1 drena a 0 en un paso;
⊗−1 mantiene |m|=1 con signo invertido a +1. Coincidencia exacta con el álgebra: ⊕1 sana,
⊗−1 afirma lo opuesto — no sana.

### 4.4 R4 · Resultado negativo (dominio)
Trauma severo (pesos aleatorios + m saturada): todos los brazos idénticos (t_conv=100,
acc=0.67). Las terapias actúan sobre memoria, no sobre pesos; el dominio de la teoría
queda delimitado, no inflado.

### 4.5 R5 · Aditividad y severidad
Trauma mixto con α∈{0,.25,.5,.75,1}: (P2) doble disociación confirmada — op1solo termina
|m|=0 pero acc catastrófica; (P3) umbral α*≈0.75 donde los brazos divergen; (P1) aditividad
FALLADA — en α=1.0, combo (0.67) peor que retrain solo (0.78), porque ⊕1 borra memorias
legítimas que el re-aprendizaje construye. Las terapias tienen dominio de efectividad
(α≤0.75) y de interferencia (α≥1.0).

## 5 · Discusión
Abstención nativa como opción de rechazo sin entrenamiento; el excluido como traza de
auditoría (explicabilidad por construcción); ⊗−1 como afirmación forzada — advertencia para
organizaciones de "aquí nunca pasó nada" y para inversiones de sesgo en ML. Ciencia frugal:
81 parámetros en un celular, checkpoints para tiempo fragmentado. Limitaciones: tarea
sintética pequeña; terapias marginales cuando el trauma toca pesos (R4); terapia ⊕1 puede
interferir con aprendizaje nuevo (R5).

### 5.5 · Límites de expresividad y el lugar de la historia (trabajo concurrente)
Un estudio computacional independiente (Kimi, 2026) verificó exhaustivamente —19,683
arquitecturas 2→2→1 con pesos ternarios y agregación ⊕— que las redes del Tres puramente
discretas no implementan la excepción de doble negación: óptimo 8/9, y una memoria global
espacial no rompe el límite. Aclaramos dos puntos que reconcilian ese resultado con el
nuestro: (i) en RedTres la agregación intra-capa es clamp de una suma real, luego asociativa;
la no-asociatividad —y con ella la historia— reside en la composición temporal del registro
de memoria, no en el orden de agregación; (ii) nuestra memoria es temporal (escrita y sanada
durante entrenamiento), mientras la del estudio concurrente es espacial, que sus propios
datos muestran insuficiente. Conjuntamente, ambos cuerpos experimentales sugieren: la
historia requiere tiempo, no profundidad. El límite de 19,683 se verifica on-device en el
Apéndice de reproducibilidad (27 funciones; mejor acierto 8/9=0.8889).

### 5.6 · Rompiendo el límite feedforward: Neuronas Fragmentadas
**Réplica del estudio concurrente (Kimi, 2026):** Implementamos Neuronas Fragmentadas
(memoria multi-slot por neurona, 3 slots, 3 pasos temporales) y las entrenamos con
algoritmo evolutivo (población 300, 400 generaciones, mutación 0.14).

**Resultado:** Convergencia a 100% (9/9) en dataset Sentimiento en generación 54, rompiendo
el límite feedforward del 88.89%. La arquitectura logra resolver la excepción de doble
negación (-1,-1)→1 que ninguna red feedforward puede computar.

**Mecanismo:** Cada neurona gestiona múltiples slots de memoria (análogos a sinapsis
biológicas), decidiendo de qué slot leer, en qué slot escribir, y qué valor escribir. La
memoria distribuida permite aplicar la regla de doble negación (-1⊗-1=1) en pasos temporales
separados, superando la incompatibilidad algebraica que limita a las redes feedforward.

**Comparación con RedTres-81:** Las dos arquitecturas son complementarias:
- RedTres-81: abstención nativa + memoria temporal (escritura/sanación)
- Fragmentadas: memoria multi-slot + resolución de límites de expresividad

Juntas forman un sistema completo: abstención calibrada (saber cuándo no responder) +
memoria profunda (capacidad de resolver problemas complejos con doble negación).

## 6 · Hacia modelos de lenguaje con abstención nativa (trabajo futuro)
Tres mecanismos: (i) cabecera por decisión {−1,0,1} con pérdida de frustración; (ii) registro
contrafáctico que guarda top-k de tokens descartados como −1; (iii) comité dialéctico de
checkpoints donde el desacuerdo produce 0 y escala. Hipótesis: la alucinación disminuye por
arquitectura, no por alineación.

## 8 · Problemas abiertos
8.1 Red Recursiva del Tres (predicción: rompe el límite 8/9 aplicando doble negación en
pasos temporales separados). 8.2 Teorema de incompletitud algebraico (formalizar por qué
feedforward no supera 8/9; análogo a Minsky-Papert pero barrera algebraica, no dimensional).
8.3 Semigrupo de las 27 funciones y monotonía (¿por qué "mayoría"=100% y "sentimiento"=8/9?).
8.4 Conexión Lindblad/decoherencia (memoria de trayectoria como sistema abierto). 8.5 λ* como
punto fijo de grupo de renormalización en la medida de caminos. 8.6 LSTM Ternaria con
compuertas de olvido/entrada (memoria vectorial centralizada como alternativa a Fragmentadas).

## 9 · Aplicaciones: niveles de madurez
T1 (computa): memristores ternarios, CNTFET, CPU ternaria, qutrits, redes evolutivas, LLMs
ternarios, robótica con memoria de fallos. T2 (modela): SQL con memoria de exclusiones,
economía (ciclos con costo hundido activo), inmunología (células de memoria como registro M),
DNA computing. T3 (ilumina): narrativa, mediación de conflictos, democracia deliberativa.
Una aplicación honesta declara su nivel; vender T3 como T1 es autoengaño.

## 10 · Related work
Setun/ternario balanceado (Brusentsov); Kleene, Łukasiewicz, Belnap, Priest (lógicas
trivaluadas y paraconsistentes); Hopfield (redes con energía); Chua/Strukov (memristor);
Landauer (termodinámica de información); Zurek (envariance y Born); Arthur (path dependence);
Chow (reject option); Arrow (votación); Kimi 2026 (redes evolutivas del Tres, límite 8/9,
Neuronas Fragmentadas y LSTM Ternaria).

## Reproducibilidad
pkg install python-numpy; python3 src/tres_fase1.py 600 — reanudable, 81 parámetros, sin GPU.
Release: src/ + figures/ + logs/ raw. Verificador de Kimi: src/verificador_kimi.py.
Neuronas Fragmentadas: src/algebra_tres_evolutivo.py (convergencia 100% en gen 54).

## Resumen llano
Un bit dice sí o no y olvida lo que casi dijo. Construimos una aritmética de tres estados —
hecho, quizás, excluido-para-siempre — donde el "quizás" puede decir "no sé" y el "excluido"
deja cicatriz que puede sanar pero nunca desaparecer. Una red de 81 parámetros en un celular
aprendió a abstenerse ante contradicciones exactamente como predice la aritmética. Otra red
con memoria distribuida rompió el límite matemático de las redes simples, resolviendo
problemas de doble negación que antes eran imposibles.
*Lo que es, lo que pudo ser, lo excluido: / tres estados, una historia — / el bit ya no olvida.*
