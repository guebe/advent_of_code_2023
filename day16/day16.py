import numpy as np

a = np.array([list(line.strip()) for line in open("input").readlines()])

# moves the beam in its previous direction
def move(b):
    return (b[0]+b[2], b[1]+b[3], b[2], b[3])

# changes the direction of a beam because of a reflection
def move2(b, dx, dy):
    return move((b[0], b[1], dx, dy))

def step(b):
    tile = a[b[1]][b[0]]
    if (tile == '.'): # carry on
        return [move(b)]
    elif (tile == '\\'): # reflect beam in one dir
        return [move2(b,b[3],b[2])]
    elif (tile == '/'): # reflect beam in one dir
        return [move2(b,-b[3],-b[2])]
    elif (tile == '|'):
        if b[3] != 0:
            return [move(b)] # beam is like '.' in this dir
        else: # reflect beam in two dirs
            return [move2(b,0,1), move2(b,0,-1)]
    elif (tile == '-'):
        if b[2] != 0:
            return [move(b)] # beam is like '.' in this dir
        else: # reflect beam in two dirs
            return [move2(b,1,0), move2(b,-1,0)]

def len_energized(bs):
    bbbs = set() # storing visited tiles position - to count later
    bbbbs = set() # storing visited tiles position and direction to find cycles
    # add initial tile
    bbbs.add((bs[0][0], bs[0][1]))
    bbbbs.add(bs[0])
    while bs:
        b = bs.pop(0)
        for bbs in step(b): # one or two new beams
            # the beam may reached the end or the beam may be a cycle
            if (0 <= bbs[0] < len(a)) and (0 <= bbs[1] < len(a)) and bbs not in bbbbs:
                bs.append(bbs)
                bbbs.add((bbs[0], bbs[1]))
                bbbbs.add(bbs)
        #print(bs)
    return len(bbbs)

print(len_energized([(0,0,1,0)])) # x,y,dx,dy

maxx = 0
for i in range(len(a[0])):
    tmp = len_energized([(0,i,1,0)])
    maxx = tmp if tmp > maxx else maxx

for i in range(len(a[0])):
    tmp = len_energized([(i,0,0,1)])
    maxx = tmp if tmp > maxx else maxx

for i in range(len(a[0])):
    tmp = len_energized([(len(a[0])-1,i,-1,0)])
    maxx = tmp if tmp > maxx else maxx

for i in range(len(a[0])):
    tmp = len_energized([(i,len(a[0])-1,0,-1)])
    maxx = tmp if tmp > maxx else maxx

print(maxx)
