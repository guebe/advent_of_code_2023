coords = []
point = (0,0)
coords.append(point)
outline = 0
xmax = 0
ymax = 0
xmin = 0
ymin = 0

for line in open("input").readlines():
    line = line.strip()
    line = line.split()
    #print(line)

    direction, length, color = line
    length = int(length)
    x, y = point

    xxx = len(coords)
    if (direction == 'R'):
        for i in range(length):
            x += 1
            coords.append((x,y))
    elif (direction == 'L'):
        for i in range(length):
            x -= 1
            coords.append((x,y))
    elif (direction == 'U'):
        for i in range(length):
            y -= 1 
            coords.append((x,y))
    elif (direction == 'D'):
        for i in range(length):
            y += 1 
            coords.append((x,y))

    for i in range(xxx, len(coords)):
        x, y = coords[i]
        print(f"({x}, {y}) ", end="") 
    print("")

    if (y > ymax):
        ymax = y
    if (x > xmax):
        xmax = x
    if (y < ymin):
        ymin = y
    if (x < xmin):
        xmin = x

    point = (x,y)
    outline += length
    print(f"{point} {outline} {direction}")

print(f"{xmax} {ymax}")
print(f"{xmin} {ymin}")

s = 0
from matplotlib.path import Path
path = Path(coords)
for y in range(ymin-1,ymax+1):
    for x in range(xmin-1,xmax+1):
        if path.contains_point((x, y)) and not (x,y) in coords:
            #print(f"inside ({x}, {y})")
            s += 1
print(outline)
print(s)
print(s+outline)

import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig, ax = plt.subplots()
patch = patches.PathPatch(path, facecolor='orange', lw=2)
ax.add_patch(patch)
ax.set_xlim(xmin-1, xmax+1)
ax.set_ylim(ymin-1, ymax+1)
plt.show()
