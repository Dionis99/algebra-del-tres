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
    def trauma_severo(s):
        # Trauma en AMBOS dominios: pesos Y memoria
        for w in s.W: w[:] = np.random.uniform(-1,1,w.shape)  # pesos random completos
        for m in s.m: m[:] = np.full_like(m, -1)  # memoria saturada en -1
    def paso(s, x, y, eta):
        acts=[np.asarray(x,float)]; vs=[]
        for W,m in zip(s.W,s.m):
            v=acts[-1]@W; vs.append(v); acts.append(cl(cl(v)+m))
        pot = np.abs(vs[0]) < 0.3
        s.m[0][pot] = cl(s.m[0][pot]-1)
        if int(np.argmax(acts[-1])==np.argmax(y)):
            s.m[0][s.m[0]<0] = cl(s.m[0][s.m[0]<0]+1)
        g = acts[-1]-y
        for l in reversed(range(len(s.W))):
            dpre = g*(np.abs(vs[l])<=1)
            s.W[l] -= eta*np.outer(acts[l], dpre)
            if l>0: g = dpre@s.W[l].T
    def terapia_op1(s):
        for m in s.m: m[m<0] = cl(m[m<0]+1)
    def terapia_otm1(s):
        for m in s.m: m[m<0] *= -1
    def diagnostico(s):
        acc = np.mean([int(np.argmax(s.forward(P[k]))==np.argmax(LBL[k])) for k in P])
        mm = float(np.mean(np.abs(s.m[0])))
        wm = float(np.mean(np.abs(s.W[0])))
        return acc, mm, wm

print("=== FASE 2B: TRAUMA SEVERO (pesos + memoria) ===\n")
for brazo in ['baseline', 'op1', 'otm1']:
    net = RedTres()
    net.trauma_severo()
    acc0, mm0, wm0 = net.diagnostico()
    print(f"{brazo:<10} post-trauma: acc={acc0:.2f} |m|={mm0:.2f} |W|={wm0:.2f}")
    
    curva_acc, curva_m = [], []
    for t in range(100):
        for k in P: net.paso(P[k]+np.random.uniform(-.05,.05,9), LBL[k], 0.05)
        if brazo == 'op1' and t % 5 == 4: net.terapia_op1()
        if brazo == 'otm1' and t % 10 == 9: net.terapia_otm1()
        acc, mm, _ = net.diagnostico()
        curva_acc.append(acc); curva_m.append(mm)
    
    t_conv = next((i for i,a in enumerate(curva_acc) if a >= 0.67), 100)
    print(f"           t_conv={t_conv:>3}  acc_final={curva_acc[-1]:.2f}  |m|_final={curva_m[-1]:.2f}\n")

print("=== OBSERVACIÓN ===")
print("Si las terapias son efectivas, deberían:")
print("1. Reducir t_conv (recuperación más rápida)")
print("2. Drenar |m| más rápido (sanación de memoria)")
print("3. Mostrar curvas de |m| distintas entre brazos")
