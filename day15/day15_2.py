a = open("input").readline().strip()
b = a.split(",")

def myhash(a):
    s = 0
    for i in range(len(a)):
        c = a[i]
        o = ord(c)
        s += o
        s *= 17
        s %= 256
    return s

boxes = [[] for i in range(256)]

import sys

for ii, x in enumerate(b):
    print(ii)
    if '=' in x:
        y = x.split('=')
        assert len(y) == 2
        label = y[0]
        length = y[1]
        h = myhash(label)
        box = boxes[h]
        #print(f"hash {h} box {box}")
        match = False
        for j in range(len(box)):
            if box[j][0] == label:
                box[j] = (label, length)
                match = True
                break
        if (not match):
            # append
            box.append((label, length))
    elif '-' in x:
        y = x.split('-')
        assert len(y) == 2
        assert y[1] == ''
        label = y[0]
        box = boxes[myhash(label)]
        #print(f"hash {myhash(label)} box {box}")
        for j in range(len(box)):
            if box[j][0] == label:
                del box[j]
                break
    else:
        assert not "failed"
    print(boxes)

tot = 0
for i in range(len(boxes)):
    box = boxes[i]
    for j in range(len(box)):
        label, length = box[j]
        m = (i+1)*(j+1)*int(length)
        print(f"{label} {length} {m}")
        tot += m
print(tot)

