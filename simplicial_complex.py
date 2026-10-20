from itertools import combinations

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

    # format pretty output
    def _format_face(self, face):
        return f"{{{', '.join(sorted(face))}}}"
    
    def n_simplices(self, n):
        simplex_lengths = [len(f)-1 for f in self.S]
        if(n > max(simplex_lengths)):
            raise ValueError(
                f"{n}-simplex does not exisit"
            )
        return {f for f in self.S if len(f)-1 == n}

    # max dim of any simplices
    def dim(self):
        return max(len(f)-1 for f in self.S)
    
    def boundary_k(self):
        return

    def is_surface(self):
        return

    def is_orientable(self):
        return

    def is_connected(self):
        return

    def barycentric_subdivision(self):
        return


