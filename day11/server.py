file_path = "input.txt"

def traverse(root, node_map, visited):
    if root == None:
        return 1
    if root.val in visited:
        return 0

    visited.append(root.val)
    valid_paths = 0
    for neighbor in root.neighbors:
        neighbor_node = node_map.get(neighbor)
        valid_paths += traverse(neighbor_node, node_map, visited)

    visited.remove(root.val)
    return valid_paths

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
        self.seen = False

with open(file_path, 'r') as file:
    nodes = {}
    for line in file:
        vals = line.strip().split()
        val = vals[0][0:3]
        neighbors = vals[1:]
        nodes[val] = Node(val, neighbors)

    print(traverse(nodes.get('you'), nodes, []))