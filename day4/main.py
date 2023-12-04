# part 1
# with open("./input.txt") as f:
#     cards = f.readlines()
#     score = 0
#     for card in cards:
#         rest = card.strip().split(":")[1]
#         winning, have = rest.split("|")
#         win_nums = set([int(n) for n in winning.split()])
#         have_nums = [int(n) for n in have.split()]
#         win_count = len(list(filter(lambda x: x in win_nums, have_nums)))
#         if win_count == 0:
#             continue
#         score += 2**(win_count-1)
#     print(score)

with open("./input.txt") as f:
    cards = f.readlines()
    cards_win_count = {}
    for i, card in enumerate(cards):
        rest = card.strip().split(":")[1]
        winning, have = rest.split("|")
        win_nums = set([int(n) for n in winning.split()])
        have_nums = [int(n) for n in have.split()]
        win_count = len(list(filter(lambda x: x in win_nums, have_nums)))
        cards_win_count[i+1]=win_count
    card_indexes = list(range(1, len(cards)+1))
    copies_count = {k: 1 for k in card_indexes}
    for current in card_indexes: 
        add_copies_count = cards_win_count[current]
        for add_copies_index in list(range(current+1, current+add_copies_count+1)):
            copies_count[add_copies_index] += copies_count[current]
    print(sum(copies_count.values()))