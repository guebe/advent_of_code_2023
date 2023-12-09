l = [list(map(int,line.split())) for line in open("input").readlines()]

def extrapolate(points):
    s = 0
    while (not all(x == 0 for x in points)):
        s += points[-1]
        points = [b - a for a, b in zip(points, points[1:])]
    return s

print(sum(extrapolate(points) for points in l))
print(sum(extrapolate(list(reversed(points))) for points in l))
