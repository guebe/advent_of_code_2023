from functools import cache

OPERATIONAL = '.'
DAMAGED = '#'
UNKNOWN = '?'

# return memorized sub-results to improve performance
@cache
def count_accepted(springs, damaged):
    # here we stop the recursive function
    # return 0: don't accept - still damaged springs left
    # return 1: accept - legal variation
    if springs == "":
        return 0 if len(damaged) > 0 else 1
    if len(damaged) == 0:
        return 0 if DAMAGED in springs else 1

    accepted = 0
    # start two sub-variation recursion searches
    # sub-variant 1: treat UNKNOWN as OPERATIONAL
    if springs[0] in OPERATIONAL + UNKNOWN:
        accepted += count_accepted(springs[1:], damaged)
    # sub-variant 2: treat UNKNOWN as DAMAGED
    # this is the start of a DAMAGED block we account for
    if springs[0] in DAMAGED + UNKNOWN:
        # there must be enough springs left and
        # only DAMAGED _and_ UNKNOWN (no OPERATIONAL) springs within the damaged springs range and
        # no more springs left or next spring is OPERATIONAL or UNKNOWN
        if (len(springs) >= damaged[0] and
            OPERATIONAL not in springs[:damaged[0]] and
            (len(springs) == damaged[0] or springs[damaged[0]] in OPERATIONAL + UNKNOWN)):
            # +1 is essential because otherwise we immediately start a new
            # damaged block recursively, but this is not allowed as no two
            # damaged blocks can occur immediately after one another. Also the
            # +1 does not overflow if no more strings left because python
            # creates an empty string instead.
            accepted += count_accepted(springs[damaged[0]+1:], damaged[1:])
    return accepted

ans = 0    
for line in open("input"):
    springs, damaged = line.strip().split()
    damaged = tuple(map(int, damaged.split(",")))
    ans += count_accepted("?".join([springs] * 5), damaged * 5)
print(ans)
