import functools
import math

file_path = "input.txt"

def compare(junction_distance1, junction_distance2):
    return junction_distance1.distance - junction_distance2.distance

class Junction:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.circuit = -1

class JunctionDistance:
    def __init__(self, junction1, junction2, distance):
        self.junction1 = junction1
        self.junction2 = junction2
        self.distance = distance

def calc_distance(junction1, junction2):
    x_distance = junction1.x - junction2.x
    y_distance = junction1.y - junction2.y
    z_distance = junction1.z - junction2.z

    return math.sqrt(math.pow(x_distance, 2) + math.pow(y_distance, 2) + math.pow(z_distance, 2))

def get_distances(junctions):
    junction_distances = []
    for i in range(0, len(junctions) - 1):
        for j in range(i + 1, len(junctions)):
            junction_distances.append(JunctionDistance(junctions[i], junctions[j], calc_distance(junctions[i], junctions[j])))

    return junction_distances

with open(file_path, 'r') as file:
    junctions = []
    for line in file:
        split_line = line.split(',')
        junctions.append(Junction(int(split_line[0]), int(split_line[1]), int(split_line[2])))

    junction_distances = sorted(get_distances(junctions), key=functools.cmp_to_key(compare))

    circuits = []
    for junction_distance in junction_distances:
        junction1 = junction_distance.junction1
        junction2 = junction_distance.junction2

        if junction1.circuit == -1 and junction2.circuit == -1:
            circuits_index = len(circuits)
            junction1.circuit = circuits_index
            junction2.circuit = circuits_index
            circuits.append({junction1, junction2})
        elif junction1.circuit != -1 and junction2.circuit == -1:
            circuits_index = junction1.circuit
            junction2.circuit = circuits_index
            circuits[circuits_index].add(junction2)
        elif junction1.circuit == -1 and junction2.circuit != -1:
            circuits_index = junction2.circuit
            junction1.circuit = circuits_index
            circuits[circuits_index].add(junction1)
        elif junction1.circuit != junction2.circuit:
            if junction1.circuit < junction2.circuit:
                target_index = junction1.circuit
                source_index = junction2.circuit
            else:
                target_index = junction2.circuit
                source_index = junction1.circuit

            for junction in circuits[source_index]:
                junction.circuit = target_index
                circuits[target_index].add(junction)

            circuits[source_index] = set()

        if len(circuits[0]) == len(junctions):
            print(junction1.x * junction2.x)
            break