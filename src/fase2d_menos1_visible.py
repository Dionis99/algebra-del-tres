import numpy as np
cl = lambda x: np.clip(x, -1, 1)
P = {'A': np.array([1,1,1,1,-1,1,1,1,1],float), 'B': np.array([1,1,-1]*3,float),
     'C': np.array([1,1,1,1,-1,-1,1,1,1],float)}
LBL = {'A': np.array([1,-1,-1],float), 'B': np.array([-1,1,-1],float), 'C': np.array([-1,-1,1],float)}
d = np.load('ckpt.npz')

class RedTres:
    def __init__(s):
        s.W = [d['W0'].copy(), d['W1'].copy()]
        s.m = [d['m0'].copy(), d['m1'].copy()]
    def forward(s, x):
        a = np.asarray(x,float)
        for W,m in zip(s.W,s.m): a = cl(cl(a@W) + m)
        return a
    def trauma_memoria(s):
        for m in s.m: m[:] = -1
    def terapia_op1(s):
        for m in s.m: m[m<0] = cl(m[m<0]+1)
    def terapia_otm1(s):
        for m in s.m: m[m<0] *= -1
    def diagnostico(s):
        acc = np.mean([int(np.argmax(s.forward(P[k]))==np.argmax(LBL[k])) for k in P])
        mm = float(np.mean(np.abs(s.m[0])))
        signo = float(np.mean(s.m[0]))
        return acc, mm, signo

print("=== FASE 2D: EL −1 VISIBLE (sin auto-sanación, solo terapias) ===\n")
for brazo in ['sin_terapia', 'op1', 'otm1']:
    net = RedTres()
    net.trauma_memoria()
    acc0, mm0, sg0 = net.diagnostico()
    print(f"{brazo:<12} post-trauma: |m|={mm0:.2f} signo={sg0:+.2f} acc={acc0:.2f}")
    
    curva = [(mm0, sg0)]
    for t in range(4):
        if brazo == 'op1': net.terapia_op1()
        elif brazo == 'otm1': net.terapia_otm1()
        acc, mm, sg = net.diagnostico()
        curva.append((mm, sg))
    
    print(f"             |m|:    {[round(c[0],2) for c in curva]}")
    print(f"             signo:  {[round(c[1],2) for c in curva]}\n")

print("=== PREDICCIÓN DEL ÁLGEBRA ===")
print("sin_terapia: |m| se queda en 1.00 (el −1 persiste, memoria indeleble)")
print("op1:         −1⊕1=0  → |m| drena a 0.00 (neutraliza, sana)")
print("otm1:        −1⊗−1=+1 → |m| sigue 1.00 pero signo cambia a +1 (invierte, no sana)")
