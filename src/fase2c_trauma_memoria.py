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
        # Trauma SOLO en memoria, pesos intactos
        for m in s.m: m[:] = np.full_like(m, -1)
    def paso(s, x, y, eta, entrenar=True):
        acts=[np.asarray(x,float)]; vs=[]
        for W,m in zip(s.W,s.m):
            v=acts[-1]@W; vs.append(v); acts.append(cl(cl(v)+m))
        if not entrenar: return acts[-1]
        pot = np.abs(vs[0]) < 0.3
        s.m[0][pot] = cl(s.m[0][pot]-1)
        if int(np.argmax(acts[-1])==np.argmax(y)):
            s.m[0][s.m[0]<0] = cl(s.m[0][s.m[0]<0]+1)
        g = acts[-1]-y
        for l in reversed(range(len(s.W))):
            dpre = g*(np.abs(vs[l])<=1)
            s.W[l] -= eta*np.outer(acts[l], dpre)
            if l>0: g = dpre@s.W[l].T
        return acts[-1]
    def terapia_op1(s):
        for m in s.m: m[m<0] = cl(m[m<0]+1)
    def terapia_otm1(s):
        for m in s.m: m[m<0] *= -1
    def diagnostico(s):
        acc = np.mean([int(np.argmax(s.forward(P[k]))==np.argmax(LBL[k])) for k in P])
        mm = float(np.mean(np.abs(s.m[0])))
        return acc, mm

print("=== FASE 2C: TRAUMA SOLO EN MEMORIA (pesos intactos) ===\n")
for brazo in ['baseline', 'op1', 'otm1']:
    net = RedTres()
    net.trauma_memoria()
    acc0, mm0 = net.diagnostico()
    print(f"{brazo:<10} post-trauma: acc={acc0:.2f} |m|={mm0:.2f}")
    
    curva_acc, curva_m = [], []
    for t in range(50):
        for k in P: net.paso(P[k]+np.random.uniform(-.05,.05,9), LBL[k], 0.01)
        if brazo == 'op1' and t % 3 == 2: net.terapia_op1()
        if brazo == 'otm1' and t % 5 == 4: net.terapia_otm1()
        acc, mm = net.diagnostico()
        curva_acc.append(acc); curva_m.append(mm)
    
    t_conv = next((i for i,a in enumerate(curva_acc) if a >= 0.67), 50)
    print(f"           t_conv={t_conv:>3}  acc_final={curva_acc[-1]:.2f}  |m|_final={curva_m[-1]:.2f}")
    
    # Mostrar evolución de |m| en primeros 10 pasos
    print(f"           |m| evolución: {[round(x,2) for x in curva_m[:10]]}\n")

print("=== PREDICCIÓN ===")
print("Si las terapias funcionan en su dominio correcto:")
print("- op1 y otm1 deberían drenar |m| más rápido que baseline")
print("- op1 y otm1 deberían converger a acc≥0.67 más rápido")
print("- Las curvas de |m| deberían ser visualmente distintas")
