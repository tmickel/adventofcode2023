import re

# --- part 1 ---
# numbers = []
# all_chars = []
# with open("./input.txt") as f:
#     y = 0
#     for line in f.readlines():
#         chars = [x for x in line.strip()]
#         all_chars += [chars]
        
#         parts = re.split(r'[^0-9]+',line)
#         print(parts)
#         number_parts = list(filter(lambda x: x != '', [re.sub(r'[^0-9]+', '', part) for part in parts]))
#         x = 0
        
#         print(number_parts)
#         for p in number_parts:
#             print("checking", p)
#             match = re.search(p, line)
#             line = line[match.span()[1]:]
#             numbers += [{
#                 'value': int(p),
#                 'y': y,
#                 'x': x+match.span()[0],
#                 'width':match.span()[1]-match.span()[0]
#             }]
#             x += match.span()[1]
#         y += 1
    
#     def char_at(x, y):
#         return all_chars[y][x]

#     def is_symbol(x, y):
#         if x < 0 or x >= len(all_chars[0]):
#             return False
#         if y < 0 or y >= len(all_chars):
#             return False
#         char = char_at(x, y)
#         return char not in ['.','1','2','3','4','5','6','7','8','9','0']

#     sum_nums = 0
#     for num in numbers:
#         print("checking", num['value'])
#         adjacent = False
        
#         x = num['x']
#         y = num['y']
#         width = num['width']
        
#         # previous line
#         for i in range(width+2):
#             check_x = x+i-1
#             check_y = y-1
#             if is_symbol(check_x, check_y):
#                 print("previous adjacent")
#                 adjacent = True
#         # same line
#         if is_symbol(x-1, y):
#             adjacent = True
#             print("same adjacent left")
#         if is_symbol(x+width, y):
#             adjacent = True
#             print("same adjacent right")
#         # next line
#         for i in range(width+2):
#             check_x = x+i-1
#             check_y = y+1
#             if is_symbol(check_x, check_y):
#                 print("next adjacent", check_x, check_y)
#                 adjacent = True
        
#         if adjacent:
#             sum_nums += num['value']
#         print(num['value'], adjacent)
#         print("----")
#     print(sum_nums)

numbers = []
all_chars = []
with open("./input.txt") as f:
    y = 0
    for line in f.readlines():
        chars = [x for x in line.strip()]
        all_chars += [chars]
        
        parts = re.split(r'[^0-9]+',line)
        number_parts = list(filter(lambda x: x != '', [re.sub(r'[^0-9]+', '', part) for part in parts]))
        x = 0
        
        for p in number_parts:
            match = re.search(p, line)
            line = line[match.span()[1]:]
            numbers += [{
                'value': int(p),
                'y': y,
                'x': x+match.span()[0],
                'width':match.span()[1]-match.span()[0]
            }]
            x += match.span()[1]
        y += 1
    
    def char_at(x, y):
        return all_chars[y][x]

    def is_gear(x, y):
        if x < 0 or x >= len(all_chars[0]):
            return False
        if y < 0 or y >= len(all_chars):
            return False
        char = char_at(x, y)
        return char == '*'

    adjacencies = {}
    sum_nums = 0
    for num in numbers:
        x = num['x']
        y = num['y']
        width = num['width']
        
        # previous line
        for i in range(width+2):
            check_x = x+i-1
            check_y = y-1
            if is_gear(check_x, check_y):
                if (check_x,check_y) not in adjacencies:
                   adjacencies[(check_x,check_y)]=[] 
                adjacencies[(check_x,check_y)]+=[num['value']]
        # same line
        if is_gear(x-1, y):
            check_x=x-1
            check_y=y
            if (check_x,check_y) not in adjacencies:
                   adjacencies[(check_x,check_y)]=[] 
            adjacencies[(check_x,check_y)]+=[num['value']]
        if is_gear(x+width, y):
            check_x=x+width
            check_y=y
            if (check_x,check_y) not in adjacencies:
                   adjacencies[(check_x,check_y)]=[] 
            adjacencies[(check_x,check_y)]+=[num['value']]
        # next line
        for i in range(width+2):
            check_x = x+i-1
            check_y = y+1
            if is_gear(check_x, check_y):
                if (check_x,check_y) not in adjacencies:
                   adjacencies[(check_x,check_y)]=[] 
                adjacencies[(check_x,check_y)]+=[num['value']]
    sum = 0
    for gear_pos, numbers in adjacencies.items():
        if len(numbers) == 2:
            sum += numbers[0]*numbers[1]
    print(sum)