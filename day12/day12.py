ans = 0
OPERATIONAL = '.'
DAMAGED = '#'
UNKNOWN = '?'

def get_damaged(springs):
    return [len(x) for x in "".join(springs).replace(OPERATIONAL, " ").split()]

for line in open("input"):
    springs_, damaged_ = line.strip().split()
    damaged_ = list(map(int, damaged_.split(",")))
    springs_ = list(springs_)
    unknown = springs_.count(UNKNOWN)
    variations = 2**unknown

    print("")
    print(f"{''.join(springs_)} {damaged_} scanning {variations} variations ...")

    for i in range(variations):
        springs = springs_.copy()

        for pos in reversed(range(unknown)):
            springs[springs.index(UNKNOWN)] = DAMAGED if (i & (1<<pos)) else OPERATIONAL

        if get_damaged(springs) == damaged_:
            ans += 1
            print(f"{''.join(springs)} {ans}")

print(ans)
