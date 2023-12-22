
file = []

for line in open("input").readlines():
    file.append(line.strip())

for i, line in enumerate(file):
    if 'S' in line:
        S = (line.index('S'), i)
        break

print(S)
XMAX = len(file[0])
YMAX = len(file)
print(f"{XMAX} {YMAX}")
print(file[S[1]][S[0]])

old = set()
old.add(S)
for _ in range(64):
    new = set()
    for x, y in old:
        for x_, y_ in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if x_ >= 0 and y_ >= 0 and y_ < YMAX and x_ < XMAX:
                if (file[y_][x_] != '#'):
                    new.add((x_, y_))
    old = new

print(old)

for y in range(YMAX):
    for x in range (XMAX):
        if (x, y) in old:
            print('O', end='')
        else:
            print(file[y][x], end='')
    print()

print(len(old))



