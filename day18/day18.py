# https://en.wikipedia.org/wiki/Shoelace_formula
def triangle_formula(coords):
    A = 0
    for i in range(1, len(coords)):
        x1, y1 = coords[i - 1]
        x2, y2 = coords[i]
        A += x1*y2 - x2*y1
    A = abs(A // 2)
    return A

# https://en.wikipedia.org/wiki/Pick%27s_theorem
def picks_theorem(A, b):
    i = A - b//2 + 1
    return i

def parse_file():
    lines = []
    for line in open("input").readlines():
        direction, length, color = line.strip().split()
        length = int(length)
        lines.append((direction, length, color))
    return lines

def coordinates(lines):
    x, y = 0, 0
    coords = [(x, y)]
    outline = 0
    for direction, length, color in lines:
        if (direction == 'R'):   x += length
        elif (direction == 'L'): x -= length
        elif (direction == 'D'): y += length
        elif (direction == 'U'): y -= length
        coords.append((x, y))
        outline += length
    return coords, outline

def fix_lines(lines):
    fixup = []
    for direction, length, color in lines:
        length = int(color[2:-2],16)
        direction = ['R', 'D', 'L', 'U'][int(color[len(color)-2])]
        fixup.append((direction, length, color))
    return fixup

def min_max(coords):
    xmin, xmax = 0x7FFFFFFF, -0x80000000
    ymin, ymax = 0x7FFFFFFF, -0x80000000
    for x, y in coords:
        xmin = min(x, xmin)
        xmax = max(x, xmax)
        ymin = min(y, ymin)
        ymax = max(y, ymax)
    return xmin, xmax, ymin, ymax

def plot(coords):
    from matplotlib.path import Path
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    patch = patches.PathPatch(Path(coords), facecolor='orange', lw=2)
    fig, ax = plt.subplots()
    ax.add_patch(patch)
    xmin, xmax, ymin, ymax = min_max(coords)
    ax.set_xlim(xmin-1, xmax+1)
    ax.set_ylim(ymin-1, ymax+1)
    plt.show()

lines = parse_file()
coords, outline = coordinates(lines)
interior = picks_theorem(triangle_formula(coords), outline)
print(interior + outline)
plot(coords)

coords, outline = coordinates(fix_lines(lines))
interior = picks_theorem(triangle_formula(coords), outline)
print(interior + outline)
plot(coords)
