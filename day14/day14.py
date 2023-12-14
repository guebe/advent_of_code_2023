import numpy as np

def slide(x):
    weight = 0
    o, e, n = [], [], []
    for s in x:
        if s == '#':
            weight += sum(len(x) - len(n) - i for i, _ in enumerate(o))
            n += o + e + ['#']
            o, e = [], []
        elif s == '.':
            e.append('.')
        elif s == 'O':
            o.append('O')
    weight += sum(len(x) - len(n) - i for i, _ in enumerate(o))
    return weight, n + o + e

def slide_array(a):
    return sum(slide(x)[0] for x in a)

a = np.array([list(line.strip()) for line in open("input").readlines()])
a = np.transpose(a)
print(slide_array(a))
