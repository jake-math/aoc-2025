file_path = "input.txt"
dp = {}

def traverse(root, node_map, visited_set, required_nodes):
    if root is None:
        return 1 if not required_nodes else 0

    if root.val in visited_set:
        return 0

    dp_key = (root.val, required_nodes)
    if dp_key in dp:
        return dp[dp_key]

    new_required_nodes = required_nodes
    if root.val in required_nodes:
        new_required_nodes = required_nodes - {root.val}

    visited_set.add(root.val)
    valid_paths = 0
    for neighbor_val in root.neighbors:
        neighbor_node = node_map.get(neighbor_val)
        valid_paths += traverse(
            neighbor_node,
            node_map,
            visited_set,
            new_required_nodes
        )

    visited_set.remove(root.val)
    dp[dp_key] = valid_paths
    return valid_paths


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


with open(file_path, 'r') as file:
    nodes = {}
    for line in file:
        vals = line.strip().split()
        val = vals[0][0:3]
        neighbors = vals[1:]
        nodes[val] = Node(val, neighbors)

    required_nodes = frozenset({'fft', 'dac'})
    start_node = nodes.get('svr')

    print(traverse(start_node, nodes, set(), required_nodes))