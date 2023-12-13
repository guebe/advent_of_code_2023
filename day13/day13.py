# Find mirror candidates by comparing pairs of two consecutive lines. In a
# second step check which candidates are really mirrors. Columns are handled
# like lines by transposing the matrix.
import numpy as np

def mirrors(matrix, allowed_err):
    res = []
    prev = matrix[0]
    for i, line in enumerate(matrix[1:]):
        cnt = np.sum(~np.equal(line, prev))
        assert cnt >= 0
        if cnt <= allowed_err:
            res.append(i+1)
        prev = line
    return res

def fixup(matrix, mirrors, allowed_err):
    corrected = []
    for pos in mirrors:
        m = min(pos, len(matrix)-pos)
        start = pos - m
        end = min(pos + m, len(matrix))
        assert 0 <= start < pos < end <= len(matrix)
        slice0 = matrix[start:pos,:]
        slice1 = matrix[pos:end,:]
        assert len(slice0) == len(slice1)
        if np.sum(~np.equal(slice0, slice1[::-1])) == allowed_err:
            corrected.append(pos)
    return corrected

ans1 = 0
ans2 = 0
for section in open("input").read().split("\n\n"):
    matrix = np.matrix([list(line.strip()) for line in section.strip().split("\n")])
    tmatrix = np.transpose(matrix)
    h = fixup(matrix, mirrors(matrix, 1), 0)
    v = fixup(tmatrix, mirrors(tmatrix, 1), 0)
    assert len(h) + len(v) <= 1
    ans1 += v[0] if v else 0
    ans1 += 100*h[0] if h else 0
    h = fixup(matrix, mirrors(matrix, 1), 1)
    v = fixup(tmatrix, mirrors(tmatrix, 1), 1)
    assert len(h) + len(v) <= 1
    ans2 += v[0] if v else 0
    ans2 += 100*h[0] if h else 0
print(ans1)
print(ans2)
