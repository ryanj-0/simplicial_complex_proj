# Talking Points in Class
## Work that _could_ be done on class
- Considering a `frozenset` or not for our Poset.
    - This is because if we add an pair into R, we must check for all
    properties but this can balloon very fast computationally. So, one might
    have to decide how to deal with possible situations to deal with this.

        e.g. R = {(a,a), (b,b), (c,c), (d,d), (a,b), (c,d)} and then add (b,c)
    - []


# Sources
- https://en.wikipedia.org/wiki/Partially_ordered_set
- https://www.routledge.com/Data-Science-for-Mathematicians/Carter/p/book/9780367528492
- https://www.math.cmu.edu/~af1p/Teaching/Combinatorics/Slides/Posets.pdf
- https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Applied_Discrete_Structures_(Doerr_and_Levasseur)/13:_Boolean_Algebra/13.01:_Posets_Revisited


# Question for Justin
- Are all simplicial complexes the power set?
-


# Simplicial Complex (K) Subclass
## Methods
- `dim_k()`
    - =max dim $\sigma$ for $\sigma \in K$
    - $dim~\sigma = \lvert \sigma \rvert - 1$
    - Euler Characterisc?
- `boundary_k()`
  - $\set{\sigma \in \text{K, s.t. } \exists \tau \subset \sigma}$
- `is_surface()`
- `is_orientable()`
- `is_connected()`
  - closure of K
  - interior of K
  - closed serface is a 2D simplicial complex with $\emptyset$ boundary
- `barycentric_)subdivision()`
  - $K \mapsto BSD(K)$
