a = open("input").readline().strip().split(",")

def hash(a):
    s = 0
    for i in range(len(a)):
        s += ord(a[i])
        s *= 17
        s %= 256
    return s

res = 0
for x in a:
    res += hash(x)
print(res)

