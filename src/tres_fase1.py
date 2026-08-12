import numpy as np, time, os, sys
TLIM = int(sys.argv[1]) if len(sys.argv) > 1 else 1200
ETA, MAXEP, SZ, TH = 0.05, 3000, [9,6,3], 0.3
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
        for W,m in zip(s.W,s.m): a = cl(cl(a@W) + m)
        return a
    def paso(s, x, y, eta, forzada=False):
        acts=[np.asarray(x,float)]; vs=[]; hs=[]; syns=[]
        for W,m in zip(s.W,s.m):
            v=acts[-1]@W; h=cl(v); sy=cl(h+m)
            vs.append(v); hs.append(h); syns.append(sy); acts.append(sy)
        mh = s.m[0]
        pot = np.abs(hs[0]) < TH
        mh[pot] = cl(mh[pot]-1)                      # 1) escritura: potencial forzado deja -1
        if forzada: return syns[-1]
        if int(np.argmax(syns[-1])==np.argmax(y)):
            mh[mh<0] = cl(mh[mh<0]+1)                # 2) sanacion: exito verificado gasta su 1
        g = syns[-1]-y
        for l in reversed(range(len(s.W))):
            dpre = g*(np.abs(vs[l])<=1)
            s.W[l] -= eta*np.outer(acts[l], dpre)
            if l>0: g = dpre@s.W[l].T
        return syns[-1]

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
    if ep % 5 == 4:
        mk = list(MEZ)[(ep//5) % 3]; net.paso(MEZ[mk], LBL[mk[0]], 0., forzada=True)
    lo, al, am, ac = evalua(net)
    mm = float(np.mean(np.abs(net.m[0])))
    with open('log.txt','a') as f:
        f.write(f"{ep} loss={lo:.3f} sep={am-al:.2f} acc={ac:.2f} mm={mm:.2f}\n")
    ep += 1
    if ep % 25 == 0:
        np.savez('ckpt.npz', W0=net.W[0],W1=net.W[1], m0=net.m[0],m1=net.m[1], ep=ep)
np.savez('ckpt.npz', W0=net.W[0],W1=net.W[1], m0=net.m[0],m1=net.m[1], ep=ep)
lo, al, am, ac = evalua(net)
print(f"sesion cerrada en epoch {ep} · loss={lo:.3f} sep={am-al:.2f} acc={ac:.2f} mm={np.mean(np.abs(net.m[0])):.2f}")
