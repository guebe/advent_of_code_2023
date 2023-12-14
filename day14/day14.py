import numpy as np

def weight(x):
    return sum(len(x)-i if s=='O' else 0 for i,s in enumerate(x))

def slide(x):
    o, e, n = [], [], []
    for s in x:
        if s == '#':
            n += o + e + ['#']
            o, e = [], []
        elif s == '.':
            e.append('.')
        elif s == 'O':
            o.append('O')
    return n + o + e

def slide_array(a):
    return sum(weight(slide(x)) for x in a)

a = np.array([list(line.strip()) for line in open("input").readlines()])
a = np.transpose(a)
print(slide_array(a))
