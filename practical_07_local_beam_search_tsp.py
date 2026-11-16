# Practical 7: Local Beam Search for Travelling Salesman Problem (TSP)

d = [[0,10,15,20],
     [10,0,35,25],
     [15,35,0,30],
     [20,25,30,0]]

def cost(p):
    return sum(d[p[i]][p[(i+1) % 4]] for i in range(4))

def neighbors(p):
    out = []
    for i in range(1, 4):
        for j in range(i+1, 4):
            t = list(p)
            t[i], t[j] = t[j], t[i]
            out.append(tuple(t))
    return out

k = 2
beam = [(0,1,2,3), (0,2,1,3)]

for _ in range(5):
    cand = set(beam)
    for p in beam:
        cand.update(neighbors(p))
    beam = sorted(cand, key=lambda p: (cost(p), p))[:k]

best = beam[0]
print("Best Path:", best + (0,))
print("Minimum Cost:", cost(best))
