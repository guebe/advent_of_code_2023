import numpy as np

a = np.array([list(line.strip()) for line in open("input").readlines()])
LEN = len(a) # ATTENTION: only works for arrays of same dimensional length

# moves the beam forward along its current direction
def forward(b):
    x, y, dx, dy = b
    return (x+dx, y+dy, dx, dy)

# changes the direction of the beam sideways because of a reflection
def change(b, dx, dy):
    x, y, *_ = b
    return forward((x, y, dx, dy))

# get the next beam position and direction
# [.]  carry on in same direction
# [\/] change direction
# [-|] duplicate beam or handle like [.] depending on direction
# returns one or two new beams
def one_step(b):
    x, y, dx, dy = b
    match a[y][x]:
        case '.': return [forward(b)]
        case '\\': return [change(b,dy,dx)]
        case '/': return [change(b,-dy,-dx)]
        case '|': return [forward(b)] if (dy != 0) else [change(b,0,1), change(b,0,-1)]
        case '-': return [forward(b)] if (dx != 0) else [change(b,1,0), change(b,-1,0)]

def energy(b):
    x, y, *_ = b
    bs = [b] # beams
    sbs = {b} # set of visited beams positions and directions to find cycles
    ebs = {(x,y)} # set of visited beam positions to get energy
    while bs:
        for b in one_step(bs.pop(0)):
            x, y, *_ = b
            # check position in range and not a cycle
            if (0 <= x < LEN) and (0 <= y < LEN) and b not in sbs:
                bs.append(b)
                sbs.add(b)
                ebs.add((x, y))
    return len(ebs)

print(energy((0,0,1,0))) # x,y,dx,dy

res = 0
for i in range(LEN):
    res = max(energy((0,i,1,0)), res)
    res = max(energy((i,0,0,1)), res)
    res = max(energy((LEN-1,i,-1,0)), res)
    res = max(energy((i,LEN-1,0,-1)), res)
print(res)
