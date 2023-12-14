import numpy as np

def weight(a):
    a = np.rot90(a, k=1);
    res = 0
    for x in a:
        res += sum(len(x)-i if s=='O' else 0 for i,s in enumerate(x))
    a = np.rot90(a, k=-1);
    return res

def slide(a):
    for x in a:
        do_work = True
        while (do_work):
            do_work = False
            for i in range(1,len(x)):
                if (x[i-1] == "." and x[i] == "O"):
                    x[i-1], x[i] = x[i], x[i-1]
                    do_work = True

def cycle(a):
    a = np.rot90(a, k=1); slide(a); a = np.rot90(a, k=-1) # north
    slide(a) # west
    a = np.rot90(a, k=-1); slide(a); a = np.rot90(a, k=1) # south
    a = np.rot90(a, k=2); slide(a); a = np.rot90(a, k=-2) #east 

cache = {}
a = np.array([list(line.strip()) for line in open("input").readlines()])
i = 0
while i < 1000000000:
    print(f"cycle {i}")
    cycle(a)
    h = hash(tuple(["".join(l) for l in list(a)]))
    if h in cache:
        i = 1000000000 - (1000000000 - i) % (i - cache[h])
    cache[h] = i
    i += 1
print(weight(a))
