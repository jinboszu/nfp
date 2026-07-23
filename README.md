This project provides a lightweight Python implementation of the no-fit polygon (NFP) of two convex polygons.

The boundary of the NFP is the locus of the reference point of a sliding polygon as it touches but does not overlap a fixed polygon. Its interior consists of placements where the two polygons overlap and is therefore called the no-fit region.

`nfp(P, Q)` in `nfp.py` computes the NFP of the sliding polygon `Q` relative to the fixed polygon `P`. Both input polygons must be convex and represented as counterclockwise lists of `(x, y)` tuples. The resulting NFP is returned in the same format.
