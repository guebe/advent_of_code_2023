FILE = open("input").readlines()
inputs = FILE[0].strip()

maps = {}
for line in FILE[2:]:
    a, b, c = line.translate(str.maketrans('=(,)','    ')).strip().split()
    maps[a] = (b,c)

import sys
i = 0
key = 'AAA'
while (True):
    for n in inputs:
        key = maps[key][0 if n=='L' else 1]
        i += 1
        if (key == 'ZZZ'):
            print(i)
            sys.exit()
