class Hand(object):
    def __init__(self, cards, bid: int):
        self.cards = cards
        self.bid = bid
    def top_rank(self):
        card_set = set(self.cards)
        if 'J' in card_set:
            if len(card_set) == 1:
                return 0xf00000 
            card_set.remove("J")
        card_freqs = {f: self.cards.count(f) for f in card_set}
        top_card = max(card_freqs, key=card_freqs.get)
        replaced_hand = [c for c in ''.join(self.cards).replace('J', top_card)]
       
        # five of a kind
        if replaced_hand[0] == replaced_hand[1] == replaced_hand[2] == replaced_hand[3] == replaced_hand[4]:
           return 0xf00000
        # four of a kind
        sorted_cards = sorted(replaced_hand)
        if (sorted_cards[0] == sorted_cards[1] == sorted_cards[2] == sorted_cards[3]) or (sorted_cards[1] == sorted_cards[2] == sorted_cards[3] == sorted_cards[4]):
            return 0xe00000
        # full house
        if ((sorted_cards[0] == sorted_cards[1] == sorted_cards[2]) and (sorted_cards[3] == sorted_cards[4])) or ((sorted_cards[0] == sorted_cards[1]) and (sorted_cards[2] == sorted_cards[3] == sorted_cards[4])):
            return 0xd00000
        # three of a kind
        if (sorted_cards[0] == sorted_cards[1] == sorted_cards[2]) or (sorted_cards[4] == sorted_cards[3] == sorted_cards[2]) or (sorted_cards[1] == sorted_cards[2] == sorted_cards[3]):
            return 0xc00000
        # two pair
        if len(set(replaced_hand)) == 3:
            return 0xb00000
        # one pair
        if len(set(replaced_hand)) == 4:
            return 0xa00000
        # high card
        return 0
    def card_rank(self, card):
        order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'][::-1]
        return order.index(card)
    def card_score(self, card, pos):
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