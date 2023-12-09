FILE = open("input").readlines()
inputs = FILE[0].strip()

maps = {}
keys = []
for line in FILE[2:]:
    a, b, c = line.translate(str.maketrans('=(,)','    ')).strip().split()
    maps[a] = (b,c)
    if (a[-1] == 'A'):
        keys.append(a)

def solvestep(key):
    i = 0
    while (key[-1] != 'Z'):
        key = maps[key][0 if inputs[i%len(inputs)]=='L' else 1]
        i += 1
    return i

steps = [solvestep(k) for k in keys]

from math import lcm
kgv = lcm(*steps)
print(kgv)
