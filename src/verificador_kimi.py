import itertools
P=[-1,0,1]; cl=lambda x:max(-1,min(1,x))
ops=lambda v,o: v if o==0 else (1 if v==0 else v) if o==1 else (-1 if v==0 else v)
entradas=list(itertools.product(P,P))
pos={e:i for i,e in enumerate(entradas)}
funcs=[tuple(ops(cl(w1*a+w2*b),o) for a,b in entradas)
       for w1 in P for w2 in P for o in (0,1,-1)]
print("funciones distintas:", len(set(funcs)))   # espera 27
target=tuple({(-1,-1):1,(-1,0):-1,(-1,1):0,(0,-1):-1,(0,0):0,
              (0,1):1,(1,-1):0,(1,0):1,(1,1):1}[e] for e in entradas)
mejor=0; fallo=None
for A in funcs:
    for B in funcs:
        pares=[(A[i],B[i]) for i in range(9)]
        for G in funcs:
            ac=sum(1 for i in range(9) if G[pos[pares[i]]]==target[i])
            if ac>mejor: mejor=ac
print("mejor acierto 2->2->1:", mejor, "/9 =", round(mejor/9,4))  # espera 8/9 = 0.8889
