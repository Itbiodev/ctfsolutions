import math

def dot(u,v):
    return sum([a*b for a,b in zip(u,v)])
def norm(u):
    return math.sqrt(dot(u,u))
def smul(a,v):
    return [a*b for b in v]
def proj(v,u):
    return [dot(u,v)/dot(u,u)*a for a in u]
def vsum(u,v):
    return [a+b for a,b in zip(u,v)]
def gs(v):
    n = len(v)
    u = [[]]*n
    m = len(v[0])
    t = [0]*m
    u[0] = v[0]
    for i in range(1,n):
        for j in range(i):
            t=vsum(t,proj(v[i],u[j]))
        u[i] = vsum(v[i],smul(-1,t))
        t = [0]*m
            
    return u

v = [846835985,9834798552]
u = [87502093,123094980]
print(dot(v,u))
while norm(u) < norm(v):
    k = math.floor(dot(u,v)/dot(u,u))
    v = vsum(v,smul(-k,u))
    v,u = u,v

print(dot(v,u))
print(dot(u,v))

v =[[4,1,3,-1],[2,1,-3,4],[1,0,-2,7],[6,2,9,-5]]

