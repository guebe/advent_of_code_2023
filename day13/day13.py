import numpy as np
import sys

file = open("input").read()

sections = file.split("\n\n")

def get_split(matrix):
    res = []
    i = 0
    prev = matrix[0]
    #print(prev)
    for line in matrix[1:]:
        if np.array_equal(line, prev):
            res.append(i+1)
            #print(f">>>>")
        #print(line)
        prev = line
        i += 1
    #print("")
    return res

def correct_splits(matrix, vs):
    v1 = []
    for v in vs:
        l1 = v
        l2 = len(matrix)-v
        m = min(l1, l2)
        s = (l1 - m)
        e = min(v + m, len(matrix))
        #print(f"min({v} + {m}, {len(matrix)})")
        #print(f"{s} {v} {e}")
        assert(s < v < e)
        assert(s >= 0)
        assert(e <= len(matrix))
        x0 = matrix[s:v,:]
        x1 = matrix[v:e,:]
        #print(x0)
        #print()
        #print(x1)
        assert (len(x0) == len(x1))
        if np.array_equal(x0, x1[::-1]):
            v1.append(v)
    return v1

ans = 0
i = 0
for section in sections:
    section = section.strip().split("\n")
    print("")
    for line in section:
        print(line)
    matrix = np.matrix([list(line.strip()) for line in section])
    v = get_split(matrix)
    h = get_split(np.transpose(matrix))
    print(f"section {i} {v} {h}")
    v1 = correct_splits(matrix, v)
    h1 = correct_splits(np.transpose(matrix), h)
    print(f"corrected {v1} {h1}")
    assert(len(v1) <= 1)
    assert(len(h1) <= 1)
    try:
        v2 = v1[0]
    except IndexError:
        v2 = 0
    try:
        h2 = h1[0]
    except IndexError:
        h2 = 0

    ans += h2 + v2*100
    print(ans)
    i += 1

