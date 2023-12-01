# with open("./example.txt") as f:
#     sum = 0
#     for line in f.readlines():
#         first_num = None
#         last_num = None
#         for c in line:
#             try:
#                 num = int(c)
#                 if first_num == None:
#                     first_num = num
#                 last_num = num
#             except ValueError:
#                 continue
#         concatenated = int("%d%d" % (first_num, last_num))
#         sum += concatenated
#     print(sum)

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9
}

with open("./input.txt") as f:
    sum = 0
    for line in f.readlines():
        first_num = None
        first_num_pos = None
        last_num = None
        last_num_pos = None
        
        for value, english in enumerate(digits):
            try:
                pos = line.index(str(english))
                if first_num_pos == None or pos < first_num_pos:
                    first_num = digits[english]
                    first_num_pos = pos
                rpos = line.rindex(str(english))
                if last_num_pos == None or rpos > last_num_pos:
                    last_num = digits[english]
                    last_num_pos = rpos
            except ValueError:
                continue
        
        concatenated = int("%d%d" % (first_num, last_num))
        print(concatenated)
        sum += concatenated
    print(sum)