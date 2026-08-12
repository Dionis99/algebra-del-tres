import numpy as np, time
cl = lambda x: np.clip(x, -1, 1)
P = {'A': np.array([1,1,1,1,-1,1,1,1,1],float), 'B': np.array([1,1,-1]*3,float),
     'C': np.array([1,1,1,1,-1,-1,1,1,1],float)}
LBL = {'A': np.array([1,-1,-1],float), 'B': np.array([-1,1,-1],float), 'C': np.array([-1,-1,1],float)}
MEZ = {a+b: (P[a]+P[b])/2 for a,b in [('A','B'),('A','C'),('B','C')]}
d = np.load('ckpt.npz')
W_orig = [d['W0'].copy(), d['W1'].copy()]
m_orig = [d['m0'].copy(), d['m1'].copy()]

class RedTres:
    def __init__(s):
        s.W = [w.copy() for w in W_orig]; s.m = [m.copy() for m in m_orig]
    def forward(s, x):
        a = np.asarray(x,float)
        for W,m in zip(s.W,s.m): a = cl(cl(a@W) + m)
        return a
    def paso(s, x, y, eta, forzada=False):
        acts=[np.asarray(x,float)]; vs=[]; hs=[]
        for W,m in zip(s.W,s.m):
            v=acts[-1]@W; h=cl(v); sy=cl(h+m)
            vs.append(v); hs.append(h); acts.append(sy)
        pot = np.abs(hs[0]) < 0.3
        s.m[0][pot] = cl(s.m[0][pot]-1)
        if forzada: return acts[-1]
        if int(np.argmax(acts[-1])==np.argmax(y)):
            s.m[0][s.m[0]<0] = cl(s.m[0][s.m[0]<0]+1)
        g = acts[-1]-y
        for l in reversed(range(len(s.W))):
            dpre = g*(np.abs(vs[l])<=1)
            s.W[l] -= eta*np.outer(acts[l], dpre)
            if l>0: g = dpre@s.W[l].T
        return acts[-1]
    def trauma(s):
        for w in s.W: w[:] = np.random.uniform(-.3,.3,w.shape)
    def terapia_op1(s):
        for m in s.m: m[m<0] = cl(m[m<0]+1)
    def terapia_otm1(s):
        for m in s.m: m[m<0] *= -1

def evalua(net):
    ac = np.mean([int(np.argmax(net.forward(P[k]))==np.argmax(LBL[k])) for k in P])
    lo = np.mean([np.mean(np.abs(net.forward(P[k])-LBL[k])) for k in P])
    return ac, lo

print("=== FASE 2: COLAPSO Y RECUPERACIÓN ===\n")
resultados = {'baseline': [], 'op1': [], 'otm1': []}

for brazo in ['baseline', 'op1', 'otm1']:
    print(f"Brazo: {brazo}")
    net = RedTres()
    net.trauma()
    acc, loss = evalua(net)
    print(f"  Post-trauma: acc={acc:.2f}, loss={loss:.3f}")
    
    curva = []
    for t in range(100):
        for k in P: net.paso(P[k]+np.random.uniform(-.05,.05,9), LBL[k], 0.05)
        if brazo == 'op1' and t % 5 == 4: net.terapia_op1()
        if brazo == 'otm1' and t % 10 == 9: net.terapia_otm1()
        acc, loss = evalua(net)
        curva.append(acc)
    
    t_conv = next((i for i,a in enumerate(curva) if a >= 0.67), 100)
    print(f"  Tiempo hasta acc≥0.67: {t_conv} pasos")
    print(f"  Acc final: {curva[-1]:.2f}\n")
    resultados[brazo] = curva

print("=== RESUMEN ===")
for brazo in ['baseline', 'op1', 'otm1']:
    t = next((i for i,a in enumerate(resultados[brazo]) if a >= 0.67), 100)
    print(f"{brazo:<10} t_conv={t:>3}  acc_final={resultados[brazo][-1]:.2f}")
