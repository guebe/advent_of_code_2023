a = open("input").readline().strip()
b = a.split(",")

def hash(a):
    print(a)
    s = 0
    for i in range(len(a)):
        c = a[i]
        o = ord(c)
        s += o
        s *= 17
        s %= 256
    return s

res = 0
for x in b:
    res += hash(x)
print(res)

