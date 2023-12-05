class Mapping:
    def __init__(self):
        self.ranges = []
    
    def add_range(self, dst_start: int, src_start: int, range_length: int):
        self.ranges.append(
            {
                'dst_start': dst_start,
                'src_start': src_start,
                'range_length': range_length
            }
        )
    
    def map_num(self, num: int) -> int:
        for range in self.ranges:
            if num >= range['src_start'] and num < range['src_start']+range['range_length']:
                return range['dst_start'] + (num - range['src_start'])
        return num

    def reverse_map_num(self, num: int) -> int:
        for range in self.ranges:
            if num >= range['dst_start'] and num < range['dst_start']+range['range_length']:
                return range['src_start'] + (num - range['dst_start'])
        return num 

    def __repr__(self) -> str:
        return self.ranges.__repr__()+'\n\n'

seed_ranges = []
mappings = [
    Mapping(),
    Mapping(),
    Mapping(),
    Mapping(),
    Mapping(),
    Mapping(),
    Mapping(),
]

with open("./input.txt") as f:
    current_mapping = -1
    for line in f.readlines():
        if line.startswith("seeds: "):
            remaining = line.strip("seeds: ")
            seeds = [int(n) for n in remaining.split()]
            seed_ranges = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
            continue
        if "-to-" in line:
            current_mapping += 1
            continue
        parts = [int(n) for n in line.split()]
        if len(parts) != 3:
            continue
        mappings[current_mapping].add_range(parts[0], parts[1], parts[2])
        
    def in_seed_ranges(n: int) -> bool:
        for s in seed_ranges:
            if n >= s[0] and n < s[0]+s[1]:
                print(s)
                return True
        return False

    i = 0
    while True:
        current = i
        for mapping in mappings[::-1]:
            current = mapping.reverse_map_num(current)
        if in_seed_ranges(current):
            print(i)
            break
        i+=1