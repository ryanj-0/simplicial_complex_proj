from itertools import combinations, permutations

import networkx as nx

from poset import PoSet


class SimplicialComplex(PoSet):
    """
    Create a simplicial complex as a PoSet object.

    Parameters
    ----------
    S : iterable
        Set of the faces of a simplicial complex


    Methods
    -------
    

    Notes
    -----
    - S can be at minimum the set of maximal simplices. All subsets will be
      generated automatically.
    - R contains (x, y) when x is a subset of y.
    - We excluded the empty set.
    """
    def __init__(self, S):

        # generate all subsets/faces
        simplex_faces = {
            frozenset(sub_face)
            for face in S
            for size in range(1, len(face)+1)
            for sub_face in combinations(face, size)
        }

        relation = {
            (x, y)
            for x in simplex_faces for y in simplex_faces
            if x <= y
        }

        super().__init__(S=simplex_faces, R=relation)

    def __str__(self):
        ordered_output = sorted(
            self.S,
            key=lambda face: (len(face), sorted(face))
        )
        format_output = [self._format_face(f) for f in ordered_output]
        return f"S = {{{', '.join(format_output)}}}"

    def _format_face(self, face):
        return f"{{{', '.join(map(str, self._orient_element(face)))}}}"
    
    def _node_label(self, node):
        return "".join(str(x) for x in self._orient_element(node))

    def _orient_element(self, element):
        return tuple(sorted(element))
    
    def facets(self):
        G = self.hasse_diagram()
        return [n for n in G if G.out_degree(n) == 0]

    def n_simplices(self, n):
        simplex_lengths = [len(f)-1 for f in self.S]
        if(n > max(simplex_lengths)):
            raise ValueError(f"{n}-simplex does not exisit")
        return {f for f in self.S if len(f)-1 == n}

    def complex_graph(self):
        get_edges = self.n_simplices(1)
        G = nx.Graph()
        G.add_edges_from(get_edges)
        return nx.draw(G, with_labels=True)
    
    def hasse_diagram(self):
        order_relations = sorted(self.R, key=lambda x: (len(x[0]), len(x[1])))
        G = nx.DiGraph(order_relations)
        G.remove_edges_from(list(nx.selfloop_edges(G)))
        G = nx.transitive_reduction(G)
        for n in G.nodes:
            G.nodes[n]["level"] = len(n)
        return G

    def draw_hasse(self):
        G = self.hasse_diagram()
        pos = nx.multipartite_layout(G, subset_key="level", align="horizontal")
        my_labels = {x: self._node_label(x) for x in self.S}
        nx.draw(G, pos, labels=my_labels, with_labels=True)

    def dim(self):
        return max(len(f)-1 for f in self.S)

    def is_connected(self):
        G = self.hasse_diagram()
        G = G.to_undirected()
        return nx.is_connected(G)
    
    def boundary_k(self):
        G = self.hasse_diagram()
        boundary = [
            p 
            for n in self.facets() 
            for p in G.predecessors(n) 
            if G.out_degree(p) == 1           
        ]
        return [self._format_face(f) for f in boundary]
        
    def is_surface(self):
        # Every vertex in a 2-simplex and every maximal is a 2-simplex
        all(len(n) == 3 for n in self.facets())

        # Edge contained in exactly two simplices
        G = self.hasse_diagram()
        contained_in_two = [
            len(list(G.successors(n))) for n in self.n_simplices(1)]
        return all(n == 2 for n in contained_in_two)

    def is_orientable(self):
        return