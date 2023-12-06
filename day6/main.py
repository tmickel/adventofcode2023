import math
# Time:      7  15   30
# Distance:  9  40  200

races = [
    {
        'time': 7,
        'distance': 9, 
    },
    {
        'time': 15,
        'distance': 40, 
    },
    {
        'time': 30,
        'distance': 200, 
    }
]

races_input = [
    {
        'time': 44,
        'distance': 277, 
    },
    {
        'time': 89,
        'distance': 1136, 
    },
    {
        'time': 96,
        'distance': 1890, 
    },
    {
        'time': 91,
        'distance': 1768, 
    }
]

races_ways = []
for race in races_input:
    ways_to_win = 0
    for hold_time in range(1, race['time']):
        time_racing = race['time'] - hold_time 
        speed = hold_time
        distance = speed * time_racing
        if distance > race['distance']:
            ways_to_win += 1
    races_ways += [ways_to_win]
print(math.prod(races_ways))