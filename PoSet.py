class PoSet:
    """
    Partial ordered set class:
        This class defines a partial order set (poset). 
        The arguments taken are:
            S := a set
            R := a relation on S
        
        The relation R is a subset of SxS such that R satisfies 
        the following three properties:

            1.) Reflexivity: 
                    For all x in S: (x,x) is in R

            2.) Antisymmetry: 
                    For all x and y in S, ff (x, y) and (y, x) are in R, 
                    then x = y.
                    i.e. R never contains both a pair and its mirror image,
                    unless the two are the same pair.

            3.) Transitivity:
                    For all x, y, z in S, if (x,y) and (y,z) are in R,
                    then (x,z) is also in R.
    """
    def __init__(self, S, R):

        
            

        # Value Checks
        if 

        # Relation Checks
        if self._is_reflexive() == False:
            raise ValueError(f"{return} is not in R")

        self.S = set(S)
        self.R = R