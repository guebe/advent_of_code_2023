import numpy as np

def mirror(p):
    y, x, kk = p

    b = np.rot90(a, k=kk);

    print(f"find reflection {p}")
    for bb in b:
        print("".join(bb))

    for x in range(x,len(b[y])):
        if b[y][x] == '\\':
            return [(len(b[0])-x,y,1)]
        elif b[y][x] == '/':
            return [(x,len(b[0])-y,3)]
        elif b[y][x] == '|':
            print"()"
            newa = (len(b[0])-x,y,1)
            newb = (x,len(b[0])-y,3)
            return [newa, newb]
    return None

a = np.array([list(line.strip()) for line in open("input").readlines()])

reflections = [(0, 0, 0)]

while reflections:
    r = reflections.pop(0)
    rr = mirror(r)
    reflections += rr
    print(reflections)
