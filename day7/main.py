class Hand(object):
    def __init__(self, cards, bid: int):
        self.cards = cards
        self.bid = bid
    def top_rank(self):
        # five of a kind
        if self.cards[0] == self.cards[1] == self.cards[2] == self.cards[3] == self.cards[4]:
           return 0xf00000
        # four of a kind
        sorted_cards = sorted(self.cards)
        if (sorted_cards[0] == sorted_cards[1] == sorted_cards[2] == sorted_cards[3]) or (sorted_cards[1] == sorted_cards[2] == sorted_cards[3] == sorted_cards[4]):
            return 0xe00000
        # full house
        if ((sorted_cards[0] == sorted_cards[1] == sorted_cards[2]) and (sorted_cards[3] == sorted_cards[4])) or ((sorted_cards[0] == sorted_cards[1]) and (sorted_cards[2] == sorted_cards[3] == sorted_cards[4])):
            return 0xd00000
        # three of a kind
        if (sorted_cards[0] == sorted_cards[1] == sorted_cards[2]) or (sorted_cards[4] == sorted_cards[3] == sorted_cards[2]) or (sorted_cards[1] == sorted_cards[2] == sorted_cards[3]):
            return 0xc00000
        # two pair
        if len(set(self.cards)) == 3:
            return 0xb00000
        # one pair
        if len(set(self.cards)) == 4:
            return 0xa00000
        # high card
        return 0
    def card_rank(self, card):
        order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1]
        return order.index(card)
    def card_score(self, card, pos):
        # 0: 0
        # 1: 0xf0
        # 2: 0xf00
        return 16**(4-pos)*self.card_rank(card)
    def total_rank(self):
        rank = self.top_rank()
        for pos, card in enumerate(self.cards):
            rank += self.card_score(card, pos)
        return rank

all_hands = []

with open("./input.txt") as f:
    for line in f.readlines():
        hand, bid = line.split()
        cards = [c for c in hand]
        bid = int(bid)
        all_hands += [Hand(cards, bid)]
    all_hands.sort(key=lambda x: x.total_rank())
    score = 0
    for rank, card in enumerate(all_hands):
       score += (rank+1) * card.bid
    print(score)