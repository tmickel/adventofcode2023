games = {}

with open("./input.txt") as f:
    for line in f.readlines():
        id = int(line.split(":")[0].split()[1])
        if id not in games:
            games[id] = {
                'red': 0,
                'green': 0,
                'blue': 0,
            }
        rest = line.split(":")[1]
        draws = rest.split(";")
        for draw in draws:
            clean_draw = draw.strip()
            color_count_pairs = clean_draw.split(",")
            for color_count_pair in color_count_pairs:
                clean_color_count_pair = color_count_pair.strip()
                num, color = clean_color_count_pair.split()
                if int(num) > games[id][color]:
                    games[id][color] = int(num)
    possible_sum = 0
    power_sum = 0
    for id, game in games.items():
        if game['red'] <= 12 and game['green'] <= 13 and game["blue"] <= 14:
            possible_sum += id
        power_sum += game['red']*game['green']*game['blue']
    print(possible_sum)
    print(power_sum)