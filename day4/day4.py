f = open("input").readlines()

s = 0
cards = [1 for _ in f]

for index, line in enumerate(f):
    line = line.split(":")[1]
    a, b = line.split("|")
    a, b = a.split(), b.split()

    n = len(set(a) & set(b))

    if n > 0:
        s += 2 ** (n - 1)

    for i in range(n):
        x = index + i + 1
        if x < len(cards):
            cards[x] += cards[index]

print(s, sum(cards))
