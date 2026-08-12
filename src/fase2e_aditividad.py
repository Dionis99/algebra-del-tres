import numpy as np
cl = lambda x: np.clip(x, -1, 1)
P = {'A': np.array([1,1,1,1,-1,1,1,1,1],float), 'B': np.array([1,1,-1]*3,float),
     'C': np.array([1,1,1,1,-1,-1,1,1,1],float)}
LBL = {'A': np.array([1,-1,-1],float), 'B': np.array([-1,1,-1],float), 'C': np.array([-1,-1,1],float)}
d = np.load('ckpt.npz'); Wo = [d['W0'], d['W1']]
# PREDICCIONES REGISTRADAS:
# P1 aditividad: combo(acc) > max(retrain, op1solo); combo llega a 1.0
# P2 disociacion: op1solo termina |m|=0 pero acc~0.67 (traza sanada, estructura no)
# P3 severidad: a alpha baja op1~combo~1.0; a alpha alta op1~retrain; umbral alpha* donde se separan

class Red:
    def __init__(s, W, m): s.W=W; s.m=m
    def forward(s, x):
        a=np.asarray(x,float)
        for W,m in zip(s.W,s.m): a=cl(cl(a@W)+m)
        return a
    def paso(s, x, y, eta, interna=True):
        acts=[np.asarray(x,float)]; vs=[]; hs=[]
        for W,m in zip(s.W,s.m):
            v=acts[-1]@W; h=cl(v); vs.append(v); hs.append(h); acts.append(cl(h+m))
        if interna:
            pot=np.abs(hs[0])<0.3; s.m[0][pot]=cl(s.m[0][pot]-1)
            if int(np.argmax(acts[-1])==np.argmax(y)): s.m[0][s.m[0]<0]=cl(s.m[0][s.m[0]<0]+1)
        g=acts[-1]-y
        for l in reversed(range(len(s.W))):
            dpre=g*(np.abs(vs[l])<=1); s.W[l]-=eta*np.outer(acts[l],dpre)
            if l>0: g=dpre@s.W[l].T
    def op1(s):
        for m in s.m: m[m<0]=cl(m[m<0]+1)

acc_de=lambda net: np.mean([int(np.argmax(net.forward(P[k]))==np.argmax(LBL[k])) for k in P])

def run(alpha, brazo, seed, steps=100):
    r=np.random.default_rng(seed)
    W=[(1-alpha)*w+alpha*r.uniform(-1,1,w.shape) for w in Wo]
    net=Red(W, [-np.ones(6), -np.ones(3)])
    for t in range(steps):
        for k in P:
            net.paso(P[k], LBL[k], 0.0 if brazo=='op1solo' else 0.05,
                     interna=(brazo!='op1solo'))
        if brazo!='retrain' and t%5==4: net.op1()
    return acc_de(net), float(np.mean(np.abs(net.m[0])))

print("alpha  brazo     acc   |m|")
for alpha in [0., .25, .5, .75, 1.]:
    for brazo in ['retrain','op1solo','combo']:
        A=[run(alpha,brazo,s) for s in range(3)]
        ac=np.mean([a for a,_ in A]); mm=np.mean([m for _,m in A])
        print(f"{alpha:<6}{brazo:<10}{ac:.2f}  {mm:.2f}")
