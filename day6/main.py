import math

race = {
    'time': 44899691,
    'distance': 277113618901768
}

ways_to_win = 0
for hold_time in range(1, race['time']):
    time_racing = race['time'] - hold_time 
    speed = hold_time
    distance = speed * time_racing
    if distance > race['distance']:
        ways_to_win += 1
print(ways_to_win)