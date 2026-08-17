# ÁLGEBRA DEL TRES - MEMORIA CONSOLIDADA v2.0
# Proyecto: Dionis Iranjil Fuentes Lezcano + Qwen + Kimi + GPT + DeepSeek
# Última actualización: 2026-08-12

## 0. RESUMEN EJECUTIVO
Proyecto de aritmética ternaria {-1,0,1} para redes neuronales con abstención nativa.
Logros: RedTres-81 (sep=0.67), Release v1.1 en GitHub, Colapsante V2 (100% en 3 datasets).
Estado: Fase 3 cerrada. Transición a Fase 4 con laboratorio modular.

## 1. TEORÍA DEL ÁLGEBRA DEL TRES
P = {-1, 0, 1}
⊗ (interacción): a·b si ambos no-cero, sino 0. Doble negación → afirmación.
⊕ (co-presencia): si a=b retorna a; si uno es 0 retorna el otro; si opuestos retorna 0.
↑ (actualización): 0→1. ↓ (exclusión): 0→-1.
⊕ NO es asociativa (asociador en 4 triples). ⊗ es asociativa y distributiva sobre ⊕.
Teoremas: monoide físico |M|=17/27; memoria indeleble (-1⊕-1=-1); límite feedforward 88.89%.

## 2. ONTOLOGÍA E IDEAS DE DIONIS
- -1: no-ser, lo que no fue. 0: ser en potencia, burbuja de posibilidades. 1: ser en acto.
- Umbral de colapso = "saber" que reduce indeterminación.
- Especialización músico/matemático = umbrales aprendidos diferentes.
- Memoria contextual: slots como sueños reconstruidos según contexto.
- Personalidad temporal: yo pasado/presente/futuro.
- Islas de preservación: ética de no eliminar rareza.
- Traumaterapia como evolución, orden lingüístico, metacognición superior.

## 3. ARQUITECTURAS DESARROLLADAS
- RedTres-81 (Dionis+Qwen): 81 params, abstención sep=0.67, memoria temporal.
- Fragmentadas (replicadas de Kimi): 100% Sentimiento gen 54, 88.9% XOR.
- Colapsante V2 (Dionis idea, Kimi impl): 100% en 3 datasets, determinista, sin memoria.
- Fragmentada+Colapsante (hibridación): 100% en 3 datasets, convergencia más rápida.
- Colapsante V3 (recocido+certidumbre decayente): peor que V2 en datasets pequeños.

Ganadora para TritLM: Colapsante V2 (simple, rápida, rompe límites).

## 4. RESULTADOS EXPERIMENTALES
- RedTres-81: sep=0.67, acc=1.00, pérdida→0, memoria C1-C3 validada.
- Terapias: ⊕1 sana, ⊗-1 invierte (no sana), α*≈0.75.
- Fragmentadas: Sent 100% (g54), XOR 88.9%, May 100% (g11).
- Colapsante V2: Sent 100% (g1), XOR 100% (g38), May 100% (g16).
- Fragmentada+Colapsante: 100% en los 3, convergencia más rápida.
- MNIST ternarizado: 30% (cuello: presión global).
- Descenso vecindario + 50 reinicios: toca el techo teórico.

## 5. MÉTRICAS DEL 0 (propuesta DeepSeek)
- Tasa de ceros, tasa de colapso, tiempo medio de colapso, contradicción útil.
- Memoria de exclusión: ¿recuerda lo que NO debe hacer?
- Registro JSON por experimento.

## 6. FASES
- F1 ✅ RedTres-81 en Termux, abstención emergente.
- F2 ✅ R1-R5 (calibración, memoria, terapias, trauma, aditividad).
- F3 ✅ Paper v1.1 + Release GitHub + memoria consolidada.
- F4 🚧 TritLM con arquitectura cognitiva.

## 7. VISIÓN: TRIT ARCHITECTURE LABORATORY
Tesis (GPT/DeepSeek): ecosistema de neuronas con misma álgebra e interfaz común.
Jerarquía: sinapsis → neurona → red → metacognición → evolución → tiempo.

Catálogo TritNeuronZoo (21 tipos):
- Nivel 0: T3 (básica).
- Nivel 1: T3-NA (no asociativa), T3-O (orden).
- Nivel 2: T3-R (recurrente), T3-T (temporal).
- Nivel 3: T3-M, T3-MC, T3-ME, T3-F (memorias).
- Nivel 4: T3-FC, T3-G, T3-H (colapsantes).
- Nivel 5: T3-C (contradicción), T3-X (exclusión), T3-P (potencial), T3-D, T3-E, T3-LSTM.
- Nivel 6: M3 (metacognitiva), B3 (binaria).
- Nivel 7: H3 (híbrida), T3-NST.

Reglas:
1. Ningún modelo destruye otro (módulos independientes).
2. Arquitectura compleja reconstruible a partir de simples.
3. 60/30/10 es hipótesis, no dogma.
4. Comportamiento del 0 es métrica principal.

Estructura tritlab/: algebra/, neurons/, memory/, networks/, metacognition/, evolution/, datasets/, benchmarks/, experiments/.

## 8. PLAN DE EJECUCIÓN INMEDIATO (próximas 4 semanas)

Validado: T3, RedTres-81, Fragmentada, Colapsante V2, FragmentadaColapsante, evolución, descenso vecindario.
Hipótesis (sin validar): T3-NA, T3-R, T3-C/X/P/D/E/T/O, M3, T3-NST, 60/30/10, TritLM, MNIST >60%.

Semana 1: Crear tritlab/ mínimo (algebra/operators.py, algebra/order.py, neurons/base.py, neurons/ternary.py, neurons/non_associative.py, neurons/recurrent.py, datasets/, benchmarks/run_baseline.py).
Semana 2: Benchmark T3 vs T3-NA vs T3-R en los 3 datasets.
Semana 3: Añadir T3-G (Colapsante V2), T3-F, T3-FC. Benchmark comparativo.
Semana 4: MNIST con presión local. Objetivo >60%.

NO hacer: 21 neuronas de golpe, TritLM antes de MNIST>60%, metacognición antes de baselines, integrar ERIS antes de TritLM-mini.

## 9. VACÍOS CRÍTICOS

Resueltos: límite XOR/Sentimiento (Colapsante V2), estabilidad colapso.
Pendientes alta: presión local, escalabilidad MNIST.
Pendientes media: colapso con temperatura, slots en superposición, demostración formal, ternarización adaptativa, framework.

Errores detectados:
- Error A: colapso determinista vs ontología indeterminista.
- Error B: presión global en MNIST (sol: presión local).
- Error C: ternarización arbitraria (85, 170).
- Error D: slots sin superposición.

## 10. REPOSITORIO GITHUB
URL: https://github.com/Dionis99/algebra-del-tres
Usuario: Dionis99
Email: dionisfuenteslezcano16@gmail.com

Comandos:
  git push https://TU_TOKEN@github.com/Dionis99/algebra-del-tres.git main
  rm ~/.git-credentials  (si falla auth)
  Token en https://github.com/settings/tokens (scope repo).

Contenido: README.md, src/ (10 scripts), figures/ (4 figs), logs/, paper/, memoria.md, MODULOS_ENSAYOS/.

## 11. NOTAS IMPLEMENTACIÓN
Deps: Python 3.8+, NumPy, scikit-learn (opc MNIST).
Ejec: python3 src/tres_fase1.py 600; python3 src/validacion2.py; python3 src/algebra_tres_evolutivo.py.
Motor: ⊗ producto con 0 absorbente; ⊕ igual refuerza/0 pasa/opuestos→0.
Errores Termux: permisos git → rm ~/.git-credentials; memoria insuf → pob 100.

## 12. GLOSARIO
⊕ co-presencia, ⊗ interacción, ↑ actualización, ↓ exclusión.
sep=separación abstención, acc=accuracy, mm=|m|, α*=umbral terapias.
RedTres, Fragmentada, Colapsante V2, FragmentadaColapsante.
TritLM=LLM ternario, TritNeuronZoo=catálogo, tritlab=laboratorio.
T3=básica, B3=binaria, H3=híbrida, M3=metacognitiva, NST=sinapsis+peso+memoria+orden.

## 13. REFERENCIAS
Propio: RedTres-81, Fragmentadas, Colapsante V2, terapias ⊕1/⊗-1.
Externas: Setun (Brusentsov), Kleene/Łukasiewicz/Belnap/Priest, Hopfield, Chua/Strukov, Landauer, Zurek, Aristóteles (Metafísica Θ), Hegel (tríada dialéctica).

## 14. BRÚJULA PARA PRÓXIMA SESIÓN
FASE: Transición F3→F4. OBJETIVO: tritlab/ mínimo + benchmark T3/T3-NA/T3-R.
ACCIÓN SIGUIENTE: generar algebra/operators.py + neurons/base.py + neurons/ternary.py.
[1] v1.1 pública · Colapsante V2 validada · TritNeuronZoo aceptado
[0] tritlab mínimo · MNIST con presión local
[−1] 21 neuronas de golpe · TritLM antes MNIST>60% · mega-arquitectura

Protocolo: usuario pega brújula; asistente lee memoria.md; asistente confirma "Entiendo. Empezamos tritlab/ mínimo, sección 8 semana 1"; si asistente se desvía, usuario: "revisa memoria.md sección 8".

## 15. ATRIBUCIÓN HONESTA
Dionis: ideas y dirección (ontología aristotélica, 0 como burbuja, umbral como saber, especialización, memoria contextual, personalidad temporal, islas preservación, hibridación, trauma, binarias, metacognición).
Qwen: RedTres-81, paper v1.1, replicación Fragmentadas, memoria consolidada, evaluación crítica.
Kimi: Colapsante V2, FragmentadaColapsante, Colapsante V3, descenso vecindario, vectorización MNIST, demostración límite 88.89%.
GPT: ecosistema neuronal, zoológico, jerarquía de escalas.
DeepSeek: mapa maestro TritNeuronZoo (21 tipos, 17 redes), tritlab estructura, regla disciplina, nomenclatura, métricas del 0, 5 capas internas.

## 16. PRINCIPIO RECTOR
La inteligencia emerge no de eliminar el 0, sino de aprender:
- cuándo conservarlo (proteger la posibilidad)
- cuándo alimentarlo con contexto (buscar evidencia)
- cuándo convertirlo en -1 (exclusión, lo que no fue)
- cuándo convertirlo en +1 (actualización, lo que es)

El 0 no es fracaso. Es el espacio donde vive el devenir.

--- FIN DE MEMORIA CONSOLIDADA v2.0 ---
Próxima actualización: después de crear tritlab/ mínimo y primer benchmark.
