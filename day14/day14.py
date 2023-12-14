import numpy as np

def weight(x):
    return sum(len(x)-i if s=='O' else 0 for i,s in enumerate(x))

def slide(x):
    O, e, n = [], [], []
    for s in x:
        if s == '#':
            n += O + e + ['#']
            O, e = [], []
        elif s == '.':
            e.append('.')
        elif s == 'O':
            O.append('O')
    return n + O + e

a = np.array([list(line.strip()) for line in open("input").readlines()])
a = np.transpose(a)

ans1 = 0
for x in a:
    ans1 += weight(slide(x))

print(ans1)
