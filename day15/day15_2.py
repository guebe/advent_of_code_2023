a = open("input").readline().strip().split(",")

def myhash(a):
    s = 0
    for i in range(len(a)):
        s += ord(a[i])
        s *= 17
        s %= 256
    return s

boxes = [[] for i in range(256)]

for x in a:
    if '=' in x:
        y = x.split('=')
        assert len(y) == 2
        label, length = y
        box = boxes[myhash(label)]
        match = False
        for j in range(len(box)):
            if box[j][0] == label:
                box[j] = (label, length)
                match = True
                break
        if (not match):
            box.append((label, length))
    elif '-' in x:
        y = x.split('-')
        assert len(y) == 2 and y[1] == ''
        label = y[0]
        box = boxes[myhash(label)]
        for j in range(len(box)):
            if box[j][0] == label:
                del box[j]
                break
    else:
        assert not "failed"

tot = 0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        tot += (i+1)*(j+1)*int(boxes[i][j][1])
print(tot)

