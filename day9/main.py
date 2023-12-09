with open("./input.txt") as f:
    seqs = [[int(n) for n in l.strip().split()] for l in f.readlines()]
    total = 0
    for seq in seqs:
        levels = [seq]
        # down
        while not all(v == 0 for v in levels[-1]):
            prev_level = levels[-1]
            new_level = []
            for i in range(1, len(prev_level)):
                new_level += [prev_level[i] - prev_level[i-1]]
            levels += [new_level]
        # up
        levels[-1] += [0]
        for i in range(len(levels)-2, -1, -1):
            levels[i] += [levels[i][-1] + levels[i+1][-1]]
        # sum
        total += levels[0][-1]
    print(total)