from itertools import permutations

from poset import PoSet
from simplicial_complex import SimplicialComplex

mobius = SimplicialComplex([
    (0, 1, 2),
    (1, 2, 3),
    (2, 3, 4),
    (3, 4, 0),
    (4, 0, 1),
])

def _get_rotations(simplex):

    rotation_dict = {}
    for p in permutations(simplex):
        
        orient_sum = 0
        for i in range(len(p)):
            edge = [p[i], p[(i+1)%3]]
            orientation = edge[0]<edge[1]
            orient_sum += orientation
        rotation_dict[p] = orient_sum
    return rotation_dict

def _get_edges(triangle):
    edges = []
    for i in range(len(triangle)):
        edge = [triangle[i], triangle[(i+1)%3]]
        edges.append(edge)
    return list(edges)


G = mobius.hasse_diagram()
start_simplex = mobius.maximal()[0]
rotations = _get_rotations(start_simplex)
set_rotation = next(iter(rotations))
orientation_dict = {start_simplex: set_rotation}

orientable = True
to_check = [start_simplex]
print(f"Starting Simplex: {start_simplex}")
while orientable and to_check:
    current = to_check.pop()
    for edge in _get_edges(orientation_dict[current]):
        check_neighbors = list(
            G.successors(frozenset(edge)))
        neighbors = [n for n in check_neighbors if n != current]

        for n in neighbors:
            neighbor_rotations = _get_rotations(n)
            neighbor_order = next(iter(neighbor_rotations))
            if edge in _get_edges(neighbor_order):
                neighbor_order = next(
                    k for k, v in neighbor_rotations.items() 
                    if v != neighbor_rotations[neighbor_order])
        
            if n not in orientation_dict:
                orientation_dict[n] = neighbor_order
                to_check.append(n)
                print(f"Orientaion Passed, added: {neighbor_order}")
            else:
                already_in = orientation_dict[n]
                old_direction = neighbor_rotations[already_in]
                new_direction = neighbor_rotations[neighbor_order]
                if old_direction != new_direction:
                    print("\n")
                    print("Checked:")
                    print(*orientation_dict.values(), sep="\n")
                    print("\n")
                    print(f"Old Orientation: {old_direction}")
                    print(f"{already_in}")
                    print(f"New Orientation: {new_direction}")
                    print(f"{neighbor_order}")
                    
                    orientable = False
                    break  
print("\n")
print("Orientable" if orientable else "Not Orientable")


