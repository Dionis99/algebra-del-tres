# Álgebra del Tres: Abstención Nativa y Memoria Indeleble

Redes neuronales con aritmética saturada de tres estados {-1, 0, 1} que exhiben
abstención calibrada emergente y memoria de exclusiones sanable.

## Reproducción rápida (Termux/Android, sin GPU)

    pkg install python-numpy -y
    python3 src/tres_fase1.py 600
    python3 src/validacion2.py
    python3 src/verificador_kimi.py

## Resultados principales

| Experimento | Resultado | Significado |
|---|---|---|
| R1 (F1) | sep=0.67, acc=1.00 | Abstención calibrada emergente |
| R2 (C1-C3) | escritura/sanación exactas | Memoria indeleble + terapia |
| R3 (F2d) | persiste / sana / invierte | Terapias distintas |
| R4 (F2b) | trauma severo sin efecto | Dominio = memoria |
| R5 (F2e) | aditividad falla en alpha=1.0 | Terapias no siempre ayudan |

## El Álgebra

- a+b = clamp(a+b)  (co-presencia, no asociativa)
- a*b = a*b         (interaccion)
- Memoria m: -1+-1=-1 (indeleble); -1+1=0 (sanacion); -1*-1=+1 (inversion)

## Autores
Dionis Iranjil Fuentes Lezcano · Qwen • Kimi
