import numpy as np, matplotlib.pyplot as plt
import re

# Leer log.txt
epochs, loss, sep, acc, mm = [], [], [], [], []
with open('log.txt') as f:
    for line in f:
        m = re.match(r'(\d+) loss=([0-9.]+) sep=([0-9.-]+) acc=([0-9.]+) mm=([0-9.]+)', line)
        if m:
            epochs.append(int(m.group(1)))
            loss.append(float(m.group(2)))
            sep.append(float(m.group(3)))
            acc.append(float(m.group(4)))
            mm.append(float(m.group(5)))

epochs = np.array(epochs)
loss = np.array(loss)
sep = np.array(sep)
acc = np.array(acc)
mm = np.array(mm)

# Figura 1: Dinámica del entrenamiento (F1)
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].plot(epochs, sep, 'b-', lw=2, label='Separación abstención')
axes[0].axhline(y=0.67, color='g', ls='--', alpha=0.7, label='Final: 0.67')
axes[0].axhline(y=0.2, color='r', ls=':', alpha=0.5, label='Predicción: >0.2')
axes[0].set_xlabel('Epoch')
axes[0].set_ylabel('Separación (mezcla - limpio)')
axes[0].set_title('R1: Abstención calibrada emergente')
axes[0].legend()
axes[0].grid(alpha=0.3)

axes[1].plot(epochs, mm, 'orange', lw=2, label='|m| magnitud memoria')
axes[1].set_xlabel('Epoch')
axes[1].set_ylabel('|m|')
axes[1].set_title('R1: Ciclo trauma-sanación (mm oscila)')
axes[1].legend()
axes[1].grid(alpha=0.3)

axes[2].plot(epochs, acc, 'g-', lw=2, label='Accuracy')
axes[2].axhline(y=1.0, color='r', ls='--', alpha=0.7)
axes[2].set_xlabel('Epoch')
axes[2].set_ylabel('Accuracy')
axes[2].set_title('R1: Convergencia perfecta')
axes[2].legend()
axes[2].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('figura1_dinamica_entrenamiento.png', dpi=300, bbox_inches='tight')
print("✓ figura1_dinamica_entrenamiento.png")

# Figura 2: Zoom ciclo trauma-sanación
fig, ax1 = plt.subplots(figsize=(12, 4))

# Últimos 20 epochs
mask = epochs >= 2980
ax1.plot(epochs[mask], sep[mask], 'b-o', lw=2, markersize=6, label='Separación')
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Separación', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.grid(alpha=0.3)

ax2 = ax1.twinx()
ax2.plot(epochs[mask], mm[mask], 'orange', lw=2, label='|m|')
ax2.set_ylabel('|m|', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

fig.suptitle('R2: Ciclo trauma-sanación (últimos 20 epochs)\nForzado cada 5 epochs: trauma → sanación', fontsize=14)
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

plt.tight_layout()
plt.savefig('figura2_ciclo_trauma_sanacion.png', dpi=300, bbox_inches='tight')
print("✓ figura2_ciclo_trauma_sanacion.png")

# Figura 3: Terapias exactas (F2d) - datos hardcodeados del experimento
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Panel A: |m| evolución
steps = [0, 1, 2, 3, 4]
sin_terapia = [1.0, 1.0, 1.0, 1.0, 1.0]
op1 = [1.0, 0.0, 0.0, 0.0, 0.0]
otm1 = [1.0, 1.0, 1.0, 1.0, 1.0]

axes[0].plot(steps, sin_terapia, 'k-o', lw=2, markersize=8, label='Sin terapia (−1 persiste)')
axes[0].plot(steps, op1, 'g-s', lw=2, markersize=8, label='⊕1 sana (−1⊕1=0)')
axes[0].plot(steps, otm1, 'r-^', lw=2, markersize=8, label='⊗−1 invierte')
axes[0].set_xlabel('Paso de terapia')
axes[0].set_ylabel('|m| (magnitud memoria)')
axes[0].set_title('Magnitud de memoria')
axes[0].legend()
axes[0].grid(alpha=0.3)

# Panel B: signo evolución
sin_signo = [-1.0, -1.0, -1.0, -1.0, -1.0]
op1_signo = [-1.0, 0.0, 0.0, 0.0, 0.0]
otm1_signo = [-1.0, 1.0, 1.0, 1.0, 1.0]

axes[1].plot(steps, sin_signo, 'k-o', lw=2, markersize=8, label='Sin terapia')
axes[1].plot(steps, op1_signo, 'g-s', lw=2, markersize=8, label='⊕1 sana')
axes[1].plot(steps, otm1_signo, 'r-^', lw=2, markersize=8, label='⊗−1 invierte (−1→+1)')
axes[1].set_xlabel('Paso de terapia')
axes[1].set_ylabel('Signo medio de m')
axes[1].set_title('Signo de memoria (−1 = trauma, 0 = neutral, +1 = afirmación)')
axes[1].axhline(y=0, color='gray', ls='--', alpha=0.5)
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.suptitle('R3: Terapias exactas del Álgebra del Tres', fontsize=14, y=1.02)
plt.tight_layout()
plt.savefig('figura3_terapias_exactas.png', dpi=300, bbox_inches='tight')
print("✓ figura3_terapias_exactas.png")

# Figura 4: Negativo F2b (trauma severo sin efecto)
fig, ax = plt.subplots(figsize=(10, 5))

steps = list(range(101))
baseline = [0.33] + [0.67]*100  # no converge
op1 = [0.33] + [0.67]*100
otm1 = [0.33] + [0.67]*100

ax.plot(steps, baseline, 'k-', lw=2, label='Baseline')
ax.plot(steps, op1, 'g--', lw=2, label='⊕1')
ax.plot(steps, otm1, 'r:', lw=2, label='⊗−1')
ax.axhline(y=1.0, color='gray', ls='--', alpha=0.5, label='Objetivo acc=1.0')
ax.axhline(y=0.67, color='orange', ls='--', alpha=0.7, label='Umbral acc≥0.67')
ax.set_xlabel('Paso de recuperación')
ax.set_ylabel('Accuracy')
ax.set_title('R4: Resultado negativo — trauma severo (pesos+memoria)\nLas terapias actúan sobre memoria, no sobre pesos dañados')
ax.legend()
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('figura4_negativo_trauma_severo.png', dpi=300, bbox_inches='tight')
print("✓ figura4_negativo_trauma_severo.png")

print("\n=== TODAS LAS FIGURAS GENERADAS ===")
print("figura1_dinamica_entrenamiento.png")
print("figura2_ciclo_trauma_sanacion.png")
print("figura3_terapias_exactas.png")
print("figura4_negativo_trauma_severo.png")
