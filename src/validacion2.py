import numpy as np
cl = lambda x: np.clip(x, -1, 1)
P = {'A': np.array([1,1,1,1,-1,1,1,1,1],float), 'B': np.array([1,1,-1]*3,float),
     'C': np.array([1,1,1,1,-1,-1,1,1,1],float)}
MEZ = {a+b: (P[a]+P[b])/2 for a,b in [('A','B'),('A','C'),('B','C')]}
d = np.load('ckpt.npz')
W = [d['W0'],d['W1']]; m = [d['m0'].copy(), d['m1'].copy()]

def forward(x, mm):
    a = np.asarray(x,float); hs=[]
    for Wl,ml in zip(W,mm):
        h = cl(a@Wl); hs.append(h); a = cl(h+ml)
    return a, hs

def escribe(x, mm):
    _, hs = forward(x, mm)
    pot = np.abs(hs[0]) < 0.3
    mm[0][pot] = cl(mm[0][pot]-1)

print("C1 · memoria tras trauma (20 mediciones forzadas)")
for t in range(20):
    for mk in MEZ: escribe(MEZ[mk], m)
print("  max|m| =", round(float(np.max(np.abs(m[0]))),2), "→ debe ser > 0")
print("  m oculta =", m[0].round(2))

print("C2 · la memoria cambia la conducta (ablacion)")
diffs = []
for mk in MEZ:
    con,_ = forward(MEZ[mk], m)
    sin,_ = forward(MEZ[mk], [np.zeros_like(m[0]), np.zeros_like(m[1])])
    diffs.append(np.mean(np.abs(con-sin)))
print("  diferencia media en mezclas =", round(float(np.mean(diffs)),3), "→ debe ser > 0")

print("C3 · terapia op1 sana (exito verificado gasta su 1)")
for t in range(5):
    m[0][m[0]<0] = cl(m[0][m[0]<0]+1)
print("  max|m| tras terapia =", round(float(np.max(np.abs(m[0]))),2), "→ debe bajar a 0")
