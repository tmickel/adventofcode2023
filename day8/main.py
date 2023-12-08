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

current_nodes = list(filter(lambda k: k.endswith("A"), nodes.keys()))

ip = 0
count = 0
while True:
    count+=1
    instruction = instructions[ip]
    if instruction == 'L':
        new_nodes = []
        for n in list(current_nodes):
            new_nodes += [nodes[n][0]]
        current_nodes = new_nodes
    if instruction == 'R':
        new_nodes = []
        for n in list(current_nodes):
            new_nodes += [nodes[n][1]]
        current_nodes = new_nodes 
    if all((node.endswith('Z') for node in current_nodes)):
        break
    ip = (ip + 1) % len(instructions)
print(count)