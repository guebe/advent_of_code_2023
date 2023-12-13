# Find mirror candidates by comparing pairs of two consecutive lines. In a
# second step check which candidates are really mirrors. Columns are handled
# like lines by transposing the matrix.
import numpy as np

def mirror_candidates(matrix):
    res = []
    prev = matrix[0]
    for i, line in enumerate(matrix[1:]):
        if np.array_equal(line, prev):
            res.append(i+1)
        prev = line
    return res

def fixup(matrix, mirrors):
    corrected = []
    for pos in mirrors:
        m = min(pos, len(matrix)-pos)
        start = pos - m
        end = min(pos + m, len(matrix))
        assert 0 <= start < pos < end <= len(matrix)
        slice0 = matrix[start:pos,:]
        slice1 = matrix[pos:end,:]
        assert len(slice0) == len(slice1)
        if np.array_equal(slice0, slice1[::-1]):
            corrected.append(pos)
    return corrected

ans = 0
for section in open("input").read().split("\n\n"):
    matrix = np.matrix([list(line.strip()) for line in section.strip().split("\n")])
    h = fixup(matrix, mirror_candidates(matrix))
    v = fixup(np.transpose(matrix), mirror_candidates(np.transpose(matrix)))
    assert len(h) + len(v) <= 1
    ans += v[0] if v else 0
    ans += 100*h[0] if h else 0
print(ans)
