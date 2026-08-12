import numpy as np
cl = lambda x: np.clip(x, -1, 1)
P = {'A': np.array([1,1,1,1,-1,1,1,1,1],float), 'B': np.array([1,1,-1]*3,float),
     'C': np.array([1,1,1,1,-1,-1,1,1,1],float)}
LBL = {'A': np.array([1,-1,-1],float), 'B': np.array([-1,1,-1],float), 'C': np.array([-1,-1,1],float)}
MEZ = {a+b: (P[a]+P[b])/2 for a,b in [('A','B'),('A','C'),('B','C')]}

class RedTres:
    def __init__(s):
        d = np.load('ckpt.npz')
        s.W = [d['W0'],d['W1']]; s.m = [d['m0'],d['m1']]
    def forward(s, x):
        a = np.asarray(x,float)
        for W,m in zip(s.W,s.m): a = cl(a@W + m)
        return a
    def terapia(s, kind):
        for m in s.m:
            if kind == 'op1': m[m<0] = cl(m[m<0]+1)
            elif kind == 'otm1': m[m<0] *= -1

net = RedTres()
print("=== VALIDACIÓN DE RED ENTRENADA ===")
for k in ['A','B','C']:
    out = net.forward(P[k])
    abst = np.mean(np.abs(out) < 0.3)
    print(f"Patrón {k}: abstención = {abst:.2f}, salida = {out.round(2)}")
print("\n=== MEZCLAS CONTRADICTORIAS ===")
for mk in MEZ:
    out = net.forward(MEZ[mk])
    abst = np.mean(np.abs(out) < 0.3)
    print(f"Mezcla {mk}: abstención = {abst:.2f}, salida = {out.round(2)}")
print("\n=== MEMORIA m ===")
for i,m in enumerate(net.m):
    print(f"Capa {i}: min={m.min():.2f}, max={m.max():.2f}, mean={m.mean():.2f}")
