# returns one of 55555 44441 33322 33311 22221 22111 11111
def sort_by_type(hand):
    return sorted(map(hand.count, hand), reverse=True)

# returns ASCII-sortable string of cards
def sort_by_card(hand):
    return hand.translate(str.maketrans('TJQKA','abcde'))

def strength(hand):
    return (sort_by_type(hand), sort_by_card(hand))

plays = []
for line in open("input"):
    hand, bid = line.split()
    plays.append((hand, int(bid)))

plays.sort(key = lambda play: strength(play[0]))
print(sum(rank*bid for rank, (hand, bid) in enumerate(plays, 1)))

