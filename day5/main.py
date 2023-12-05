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

    def __repr__(self) -> str:
        return self.ranges.__repr__()+'\n\n'

seeds = []
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
            continue
        if "-to-" in line:
            current_mapping += 1
            continue
        parts = [int(n) for n in line.split()]
        if len(parts) != 3:
            continue
        mappings[current_mapping].add_range(parts[0], parts[1], parts[2])
    locations = []
    for seed in seeds:
        current = seed
        for i, mapping in enumerate(mappings):
            current = mapping.map_num(current)
            if i == len(mappings)-1:
                locations += [current]
    print(min(locations))
    