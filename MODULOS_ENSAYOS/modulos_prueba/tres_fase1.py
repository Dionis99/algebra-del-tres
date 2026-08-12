import numpy as np, time, os, sys
TLIM = int(sys.argv[1]) if len(sys.argv) > 1 else 1200
ETA, MAXEP, SZ = 0.05, 3000, [9,6,3]
cl = lambda x: np.clip(x, -1, 1)
P = {'A': np.array([1,1,1,1,-1,1,1,1,1],float), 'B': np.array([1,1,-1]*3,float),
     'C': np.array([1,1,1,1,-1,-1,1,1,1],float)}
LBL = {'A': np.array([1,-1,-1],float), 'B': np.array([-1,1,-1],float), 'C': np.array([-1,-1,1],float)}
MEZ = {a+b: (P[a]+P[b])/2 for a,b in [('A','B'),('A','C'),('B','C')]}

class RedTres:
    def __init__(s, seed=0):
        r = np.random.default_rng(seed)
        s.W = [r.uniform(-.5,.5,(a,b)) for a,b in zip(SZ[:-1],SZ[1:])]
        s.m = [np.zeros(b) for b in SZ[1:]]
    def forward(s, x):
        a = np.asarray(x,float)
        for W,m in zip(s.W,s.m): a = cl(a@W + m)
        return a
    def paso(s, x, y, eta):
        acts=[np.asarray(x,float)]; pres=[]
        for W,m in zip(s.W,s.m):
            pre=acts[-1]@W+m; pres.append(pre); acts.append(cl(pre))
        g = acts[-1]-y
        for l in reversed(range(len(s.W))):
            dpre = g*(np.abs(pres[l])<=1)
            s.W[l] -= eta*np.outer(acts[l], dpre)
            if l>0: g = dpre@s.W[l].T

def evalua(net):
    al=np.mean([np.mean(np.abs(net.forward(P[k]))<.3) for k in P])
    am=np.mean([np.mean(np.abs(net.forward(MEZ[t]))<.3) for t in MEZ])
    ac=np.mean([int(np.argmax(net.forward(P[k]))==np.argmax(LBL[k])) for k in P])
    lo=np.mean([np.mean(np.abs(net.forward(P[k])-LBL[k])) for k in P])
    return lo, al, am, ac

net = RedTres(); ep = 0
if os.path.exists('ckpt.npz'):
    d = np.load('ckpt.npz'); ep = int(d['ep'])
    net.W = [d['W0'],d['W1']]; net.m = [d['m0'],d['m1']]
    print("reanudando en epoch", ep)
t0 = time.time()
while ep < MAXEP and time.time()-t0 < TLIM:
    for k in P: net.paso(P[k]+np.random.uniform(-.05,.05,9), LBL[k], ETA)
    lo, al, am, ac = evalua(net)
    with open('log.txt','a') as f:
        f.write(f"{ep} loss={lo:.3f} abst_l={al:.2f} abst_m={am:.2f} sep={am-al:.2f} acc={ac:.2f}\n")
    ep += 1
    if ep % 25 == 0:
        np.savez('ckpt.npz', W0=net.W[0],W1=net.W[1],
                 m0=net.m[0],m1=net.m[1], ep=ep)
np.savez('ckpt.npz', W0=net.W[0],W1=net.W[1],
         m0=net.m[0],m1=net.m[1], ep=ep)
lo, al, am, ac = evalua(net)
print(f"sesion cerrada en epoch {ep} · loss={lo:.3f} sep={am-al:.2f} acc={ac:.2f}")
print("reanuda con: python3 tres_fase1.py 1200")
