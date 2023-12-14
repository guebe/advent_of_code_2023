import numpy as np

def slide_rocks(x):
    LEN = len(x)
    i = LEN
    res = 0
    O = []
    e = []
    n = []
    for s in x:
        if s == '#':
            if len(O) > 0:
                print((len(O), i, res))
                for x in O:
                    res += i
                    i -= 1
            n += O
            n += e
            n.append('#')
            i = LEN - len(n)
            e=[]
            O=[]
        elif s == '.':
            e.append('.')
        elif s == 'O':
            O.append('O')
    if len(O) > 0:
        print((len(O), i, res))
        for x in O:
            res += i
            i -= 1
    n += O
    n += e
    return n, res

a = np.array([list(line.strip()) for line in open("input").readlines()])

print(a)
print("")
b = np.transpose(a)
print(b)
print("")

ans1 = 0
for x in b:
    c, res = slide_rocks(x)
    ans1 += res
    print(res)
    print(np.array(c))

print(ans1)
