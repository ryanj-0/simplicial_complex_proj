class PoSet:
    """
    Create a partial ordered set (poset) with set S and realtion R.

    Extended Summary: S should be an interable and is silently converted to
    a set. Relations will also be silently converted a set of 2-tuples (x, y). 

    Parameters
    ----------
    S : set, list, or iterable.
        The elements in a set.
    R : set, list, or tuple or pairs
        A binary relation that satisfies 
        reflexivity, antisymmetry, and transitivity.
        
    Notes
    -----
    The relation R is a subset of SxS such that R satisfies the following:

        1. Reflexivity: For all x in S: (x,x) is in R

        2. Antisymmetry: For all x and y in S, if (x, y) and (y, x) are in R,
                then x = y. i.e. R never contains both a pair and its mirror 
                image,unless the two are the same pair.

        3. Transitivity: For all x, y, z in S, if (x,y) and (y,z) are in R,
                then (x,z) is also in R.
    
    Examples
    --------
    """
    def __init__(self, S, R):

        self.S = set(S)
        self.R = {tuple(p) for p in R}     
            
        # Value Checks
        incorrect_length = self._length_violation()
        if incorrect_length:
            raise ValueError(f"{incorrect_length} is not a pair.")
        
        missing_member = self._membership_violation()
        if missing_member:
            raise ValueError(f"{missing_member} is in R but not in S.")
        
        # Relation Checks
        violate_reflexive = self._reflexive_violation()
        if violate_reflexive:
            raise ValueError(
                "R is not reflexive."
                f"Missing {violate_reflexive}"
            )

        violate_antisymmetry = self._antisymmetric_violation()
        if violate_antisymmetry:
            raise ValueError(
                "R is not antisymmetric. "
                f"Violating pairs {violate_antisymmetry}"
            )

        violate_transitive = self._transitivity_violation()
        if violate_transitive:
            raise ValueError(
                "R is not transitive. "
                f"Violating pairs {violate_transitive}"
            )

    def _membership_violation(self):
        return [t for t in self.R if any(x not in self.S for x in t)]

    def _length_violation(self):
        return [t for t in self.R if len(t) != 2]

    def _reflexive_violation(self): 
        return [(e,e) for e in self.S if (e,e) not in self.R]
         
    def _antisymmetric_violation(self):
        return [(x,y) for (x,y) in self.R if x != y and (y,x) in self.R ]
        
    def _transitivity_violation(self):
        return [(a,d)
            for (a,b) in self.R for (c,d) in self.R
            if b == c and (a,d) not in self.R
        ]

