from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/distributors.scad'}", use_not_include=False)

class move_copies(OpenSCADObject):
    def __init__(self, a=None, **kwargs):
       super().__init__("move_copies", {"a" : a, **kwargs})

class line_of(OpenSCADObject):
    def __init__(self, spacing=None, n=None, l=None, p1=None, p2=None, **kwargs):
       super().__init__("line_of", {"spacing" : spacing, "n" : n, "l" : l, "p1" : p1, "p2" : p2, **kwargs})

class xcopies(OpenSCADObject):
    def __init__(self, spacing=None, n=None, l=None, sp=None, **kwargs):
       super().__init__("xcopies", {"spacing" : spacing, "n" : n, "l" : l, "sp" : sp, **kwargs})

class ycopies(OpenSCADObject):
    def __init__(self, spacing=None, n=None, l=None, sp=None, **kwargs):
       super().__init__("ycopies", {"spacing" : spacing, "n" : n, "l" : l, "sp" : sp, **kwargs})

class zcopies(OpenSCADObject):
    def __init__(self, spacing=None, n=None, l=None, sp=None, **kwargs):
       super().__init__("zcopies", {"spacing" : spacing, "n" : n, "l" : l, "sp" : sp, **kwargs})

class grid2d(OpenSCADObject):
    def __init__(self, spacing=None, n=None, size=None, stagger=None, inside=None, nonzero=None, **kwargs):
       super().__init__("grid2d", {"spacing" : spacing, "n" : n, "size" : size, "stagger" : stagger, "inside" : inside, "nonzero" : nonzero, **kwargs})

class rot_copies(OpenSCADObject):
    def __init__(self, rots=None, v=None, cp=None, n=None, sa=None, offset=None, delta=None, subrot=None, **kwargs):
       super().__init__("rot_copies", {"rots" : rots, "v" : v, "cp" : cp, "n" : n, "sa" : sa, "offset" : offset, "delta" : delta, "subrot" : subrot, **kwargs})

class xrot_copies(OpenSCADObject):
    def __init__(self, rots=None, cp=None, n=None, sa=None, r=None, d=None, subrot=None, **kwargs):
       super().__init__("xrot_copies", {"rots" : rots, "cp" : cp, "n" : n, "sa" : sa, "r" : r, "d" : d, "subrot" : subrot, **kwargs})

class yrot_copies(OpenSCADObject):
    def __init__(self, rots=None, cp=None, n=None, sa=None, r=None, d=None, subrot=None, **kwargs):
       super().__init__("yrot_copies", {"rots" : rots, "cp" : cp, "n" : n, "sa" : sa, "r" : r, "d" : d, "subrot" : subrot, **kwargs})

class zrot_copies(OpenSCADObject):
    def __init__(self, rots=None, cp=None, n=None, sa=None, r=None, d=None, subrot=None, **kwargs):
       super().__init__("zrot_copies", {"rots" : rots, "cp" : cp, "n" : n, "sa" : sa, "r" : r, "d" : d, "subrot" : subrot, **kwargs})

class arc_of(OpenSCADObject):
    def __init__(self, n=None, r=None, rx=None, ry=None, d=None, dx=None, dy=None, sa=None, ea=None, rot=None, **kwargs):
       super().__init__("arc_of", {"n" : n, "r" : r, "rx" : rx, "ry" : ry, "d" : d, "dx" : dx, "dy" : dy, "sa" : sa, "ea" : ea, "rot" : rot, **kwargs})

class ovoid_spread(OpenSCADObject):
    def __init__(self, n=None, r=None, d=None, cone_ang=None, scale=None, perp=None, **kwargs):
       super().__init__("ovoid_spread", {"n" : n, "r" : r, "d" : d, "cone_ang" : cone_ang, "scale" : scale, "perp" : perp, **kwargs})

class path_spread(OpenSCADObject):
    def __init__(self, path=None, n=None, spacing=None, sp=None, rotate_children=None, closed=None, **kwargs):
       super().__init__("path_spread", {"path" : path, "n" : n, "spacing" : spacing, "sp" : sp, "rotate_children" : rotate_children, "closed" : closed, **kwargs})

class mirror_copy(OpenSCADObject):
    def __init__(self, v=None, offset=None, cp=None, **kwargs):
       super().__init__("mirror_copy", {"v" : v, "offset" : offset, "cp" : cp, **kwargs})

class xflip_copy(OpenSCADObject):
    def __init__(self, offset=None, x=None, **kwargs):
       super().__init__("xflip_copy", {"offset" : offset, "x" : x, **kwargs})

class yflip_copy(OpenSCADObject):
    def __init__(self, offset=None, y=None, **kwargs):
       super().__init__("yflip_copy", {"offset" : offset, "y" : y, **kwargs})

class zflip_copy(OpenSCADObject):
    def __init__(self, offset=None, z=None, **kwargs):
       super().__init__("zflip_copy", {"offset" : offset, "z" : z, **kwargs})

class distribute(OpenSCADObject):
    def __init__(self, spacing=None, sizes=None, dir=None, l=None, **kwargs):
       super().__init__("distribute", {"spacing" : spacing, "sizes" : sizes, "dir" : dir, "l" : l, **kwargs})

class xdistribute(OpenSCADObject):
    def __init__(self, spacing=None, sizes=None, l=None, **kwargs):
       super().__init__("xdistribute", {"spacing" : spacing, "sizes" : sizes, "l" : l, **kwargs})

class ydistribute(OpenSCADObject):
    def __init__(self, spacing=None, sizes=None, l=None, **kwargs):
       super().__init__("ydistribute", {"spacing" : spacing, "sizes" : sizes, "l" : l, **kwargs})

class zdistribute(OpenSCADObject):
    def __init__(self, spacing=None, sizes=None, l=None, **kwargs):
       super().__init__("zdistribute", {"spacing" : spacing, "sizes" : sizes, "l" : l, **kwargs})

class line_of(OpenSCADObject):
    def __init__(self, spacing=None, n=None, l=None, p1=None, p2=None, **kwargs):
       super().__init__("line_of", {"spacing" : spacing, "n" : n, "l" : l, "p1" : p1, "p2" : p2, **kwargs})

