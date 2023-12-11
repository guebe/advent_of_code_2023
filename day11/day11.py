space = []
for line in open("input"):
    space.append(list(line.strip()))

X = len(space[0])
Y = len(space)

expand_y = []
for y in range(Y):
    if all(space[y][x] == '.' for x in range(X)):
        expand_y.append(y)

expand_x = []
for x in range(X):
    if all(space[y][x] == '.' for y in range(Y)):
        expand_x.append(x);

points = []
for y in range(Y):
    for x in range(X):
        if space[y][x] == '#':
            points.append((x, y))

from itertools import combinations
all_pairs = list(combinations(points, 2))

def distance(expansion):
    dist = 0
    for (x1, y1), (x2, y2) in all_pairs:
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        d_x = x2 - x1
        d_y = y2 - y1
        for x in expand_x:
            if x1 < x < x2:
                d_x += expansion
        for y in expand_y:
            if y1 < y < y2:
                d_y += expansion
        dist += d_x + d_y
    return dist

print(distance(1))
print(distance(999999))

import matplotlib.pyplot as plt
for x, y in points:
    plt.plot(x, y, "r*")
plt.show()

