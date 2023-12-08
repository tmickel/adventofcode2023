instructions = []
nodes = {}
with open("./input.txt") as f:
    for i, line in enumerate(f.readlines()):
        if i == 0:
            instructions = [c for c in line.strip()]
        elif i >= 2:
            node_label, rest = line.split(" = ")
            left, right = rest.split(", ")
            left = left.replace("(", "").strip()
            right = right.replace(")", "").strip()
            nodes[node_label] = (left, right)

current_node = 'AAA'
ip = 0
count = 0
while True:
    count+=1
    instruction = instructions[ip]
    if instruction == 'L':
        current_node = nodes[current_node][0]
    if instruction == 'R':
        current_node = nodes[current_node][1]
    if current_node == 'ZZZ':
        break
    ip = (ip + 1) % len(instructions)
print(count)