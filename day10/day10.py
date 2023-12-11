L = '-FLS'; R = '-J7S'; U = '|F7S'; D = '|JLS'; X = None
TILES = { 'S': [L,R,U,D],
          '-': [L,R,X,X],
          '|': [X,X,U,D],
          'J': [L,X,U,X],
          'L': [X,R,U,X],
          'F': [X,R,X,D],
          '7': [L,X,X,D] }

def coord(i): return (i%COLS, i//COLS)
def tile(c): return FILE[c[0]+c[1]*COLS]
def vim(c): return (c[1]+1,c[0]+1)

def neighbors(c):
    x,y = c
    l = (x-1, y) if (x > 0) else None
    r = (x+1, y) if ((x+1) < COLS) else None
    u = (x, y-1) if (y > 0) else None
    d = (x, y+1) if ((y+1) < ROWS) else None
    return (l, r, u, d) 

def get_next(c, prevc):
    for c, tiles in zip(neighbors(c), TILES[tile(c)]):
        if c != prevc and tiles and tile(c) in tiles:
            return c

FILE = open("input").read()
COLS = FILE.index('\n') + 1
ROWS = len(FILE)//COLS

firstc = prevc = coord(FILE.index('S'))
c = get_next(firstc, (-1,-1))

coords = [firstc, c]

i = 1
while (c != firstc):
    tmp = c
    c = get_next(c, prevc)
    prevc = tmp
    coords.append(c)
    i+=1
print(i//2)
me = coords[i//2]

from matplotlib.path import Path
path = Path(coords)
print(sum(1 for x in range(len(FILE)) if not coord(x) in coords and path.contains_point(coord(x))))

import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig, ax = plt.subplots()
patch = patches.PathPatch(path, facecolor='orange', lw=2)
ax.add_patch(patch)
ax.plot(firstc[0], firstc[1], "or")
ax.plot(me[0], me[1], "og")
ax.set_xlim(0, COLS)
ax.set_ylim(0, ROWS)
plt.show()
