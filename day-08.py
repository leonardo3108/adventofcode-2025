'''
--- Day 8: Playground ---
Equipped with a new understanding of teleporter maintenance, you confidently step onto the repaired teleporter pad.

You rematerialize on an unfamiliar teleporter pad and find yourself in a vast underground space which contains a giant playground!

Across the playground, a group of Elves are working on setting up an ambitious Christmas decoration project. Through careful rigging, they have suspended a large number of small electrical junction boxes.

Their plan is to connect the junction boxes with long strings of lights. Most of the junction boxes don't provide electricity; however, when two junction boxes are connected by a string of lights, electricity can pass between those two junction boxes.

The Elves are trying to figure out which junction boxes to connect so that electricity can reach every junction box. They even have a list of all of the junction boxes' positions in 3D space (your puzzle input).

For example:

162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
This list describes the position of 20 junction boxes, one per line. Each position is given as X,Y,Z coordinates. So, the first junction box in the list is at X=162, Y=817, Z=812.

To save on string lights, the Elves would like to focus on connecting pairs of junction boxes that are as close together as possible according to straight-line distance. In this example, the two junction boxes which are closest together are 162,817,812 and 425,690,689.

By connecting these two junction boxes together, because electricity can flow between them, they become part of the same circuit. After connecting them, there is a single circuit which contains two junction boxes, and the remaining 18 junction boxes remain in their own individual circuits.

Now, the two junction boxes which are closest together but aren't already directly connected are 162,817,812 and 431,825,988. After connecting them, since 162,817,812 is already connected to another junction box, there is now a single circuit which contains three junction boxes and an additional 17 circuits which contain one junction box each.

The next two junction boxes to connect are 906,360,560 and 805,96,715. After connecting them, there is a circuit containing 3 junction boxes, a circuit containing 2 junction boxes, and 15 circuits which contain one junction box each.

The next two junction boxes are 431,825,988 and 425,690,689. Because these two junction boxes were already in the same circuit, nothing happens!

This process continues for a while, and the Elves are concerned that they don't have enough extension cables for all these circuits. They would like to know how big the circuits will be.

After making the ten shortest connections, there are 11 circuits: one circuit which contains 5 junction boxes, one circuit which contains 4 junction boxes, two circuits which contain 2 junction boxes each, and seven circuits which each contain a single junction box. Multiplying together the sizes of the three largest circuits (5, 4, and one of the circuits of size 2) produces 40.

Your list contains many junction boxes; connect together the 1000 pairs of junction boxes which are closest together. Afterward, what do you get if you multiply together the sizes of the three largest circuits?

Solution:
 - Parse the input into a list of junction box coordinates.
 - Loop through all pairs of junction boxes to calculate their Euclidean distances, and store them in a list.
 - Sort the list of distances in ascending order, and take the first 1000 pairs. 
 - Add the selected pairs to a queue of pending pairs to consider. It will join recursively the non-directly connected boxes.
   - Store the connected boxes into sets of candidate circuits
 - Sort and remove duplications, to produce a final list of circuits.
 - Calculate the sizes of all circuits, and multiply the sizes of the three largest circuits.


--- Part Two ---
The Elves were right; they definitely don't have enough extension cables. You'll need to keep connecting junction boxes together until they're all in one large circuit.

Continuing the above example, the first connection which causes all of the junction boxes to form a single circuit is between the junction boxes at 216,146,977 and 117,168,530. The Elves need to know how far those junction boxes are from the wall so they can pick the right extension cable; multiplying the X coordinates of those two junction boxes (216 and 117) produces 25272.

Continue connecting the closest unconnected pairs of junction boxes together until they're all in the same circuit. What do you get if you multiply together the X coordinates of the last two junction boxes you need to connect?

Solution:
 - Refactor into a function the final steps: sort and remove duplications from candidate circuits, calculate the sizes and multiply the three largest.
 - Adapt the main code: 
   - before: select n pairs, then process all pending pairs, and stop
   - after: select 1 pair, then process all pending pairs, and continue until all n pairs are selected (change a for+while to two nested-while)
 - One more change: 
   - before: continue the main while loop until all n pairs are selected (while index < limit)
   - after: eternal loop, if index = limit call the function for part one result, then continue
    - stop when max size of circuits = number of boxes, then take the last pair, take the two X coordenates, multiply then and print (part two result)

(the solution of part two takes a long time - optimization is desirable)
    
'''

input = '''
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
'''

num_closest_connections = 10
num_largest_circuits = 3

input = open('input-08.txt').read()
num_closest_connections = 1000

boxes = []
connections = {}
for line in input.strip().split('\n'):
    boxes.append([int(x) for x in line.strip().split(',')])
    connections[len(boxes) - 1] = {len(boxes) - 1}

num_boxes = len(boxes)
# print(f'Total boxes: {num_boxes}')

def euclidean_distance(box1, box2):
    return ((box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2 + (box1[2] - box2[2]) ** 2) ** 0.5

distances = []
for index1 in range(len(boxes)):
    box1 = boxes[index1]
    for index2 in range(index1 + 1, len(boxes)):
        box2 = boxes[index2]
        distance = euclidean_distance(box1, box2)
        # print(f'Box 1: ({box1[0]}, {box1[1]}, {box1[2]}) - Box 2: ({box2[0]}, {box2[1]}, {box2[2]}) -> Distance: {distance}')
        distances.append((distance, index1, index2))

# print(f'Total distances calculated: {len(distances)} - selecting {num_closest_connections} shortest distances:')

distances.sort(key=lambda x: x[0])


def get_sizes(connections):
    # print(connections)

    circuits = set()

    for boxes in connections.values():
        if len(boxes) > 1:
            circuits.add(tuple(sorted(boxes)))

    sizes = []
    for circuit in circuits:
        # print(circuit, '->', len(circuit), 'boxes')
        sizes.append(len(circuit))

    sizes.sort(reverse=True)

    # print(sizes[:num_largest_circuits])

    result = 1
    for size in sizes[:num_largest_circuits]:
        result *= size

    print(f'Part One - Multiplication of the sizes of the {num_largest_circuits} largest circuits: {result}')

pending = []

connection_index = 0

while True:
    max_size = 0
    distance, index1, index2 = distances[connection_index]
    # print(f'\tDistance: {distance:8.2f}    -    Box: {index1:>4}    -    Box: {index2:>4}')
    pending.append((index1, index2))

    while pending:
        index1, index2 = pending.pop()
        boxes1 = connections[index1]
        boxes2 = connections[index2]
        for box in boxes1:        
            if box not in boxes2:
                boxes2.add(box)
                if len(boxes2) > max_size:
                    max_size = len(boxes2)
                pending.append((box, index2))
        for box in boxes2:
            if box not in boxes1:
                boxes1.add(box)
                if len(boxes1) > max_size:
                    max_size = len(boxes1)
                pending.append((box, index1))

    connection_index += 1

    if connection_index == num_closest_connections:
        get_sizes(connections)
    
    if max_size >= num_boxes:
        # print(boxes[index1], boxes[index2])
        print(f'Part Two - Multiplication of the X coordinates of the last two junction boxes you need to connect: {boxes[index1][0] * boxes[index2][0]}')
        break
    
