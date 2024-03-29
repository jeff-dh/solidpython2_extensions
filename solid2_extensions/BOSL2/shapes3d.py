from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/shapes3d.scad'}", use_not_include=False)

class cube(OpenSCADObject):
    def __init__(self, size=None, center=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cube", {"size" : size, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cuboid(OpenSCADObject):
    def __init__(self, size=None, p1=None, p2=None, chamfer=None, rounding=None, edges=None, _except=None, except_edges=None, trimcorners=None, teardrop=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cuboid", {"size" : size, "p1" : p1, "p2" : p2, "chamfer" : chamfer, "rounding" : rounding, "edges" : edges, "_except" : _except, "except_edges" : except_edges, "trimcorners" : trimcorners, "teardrop" : teardrop, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class prismoid(OpenSCADObject):
    def __init__(self, size1=None, size2=None, h=None, shift=None, rounding=None, rounding1=None, rounding2=None, chamfer=None, chamfer1=None, chamfer2=None, l=None, center=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("prismoid", {"size1" : size1, "size2" : size2, "h" : h, "shift" : shift, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "l" : l, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class octahedron(OpenSCADObject):
    def __init__(self, size=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("octahedron", {"size" : size, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rect_tube(OpenSCADObject):
    def __init__(self, h=None, size=None, isize=None, center=None, shift=None, wall=None, size1=None, size2=None, isize1=None, isize2=None, rounding=None, rounding1=None, rounding2=None, irounding=None, irounding1=None, irounding2=None, chamfer=None, chamfer1=None, chamfer2=None, ichamfer=None, ichamfer1=None, ichamfer2=None, anchor=None, spin=None, orient=None, l=None, **kwargs):
       super().__init__("rect_tube", {"h" : h, "size" : size, "isize" : isize, "center" : center, "shift" : shift, "wall" : wall, "size1" : size1, "size2" : size2, "isize1" : isize1, "isize2" : isize2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "irounding" : irounding, "irounding1" : irounding1, "irounding2" : irounding2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "ichamfer" : ichamfer, "ichamfer1" : ichamfer1, "ichamfer2" : ichamfer2, "anchor" : anchor, "spin" : spin, "orient" : orient, "l" : l, **kwargs})

class wedge(OpenSCADObject):
    def __init__(self, size=None, center=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("wedge", {"size" : size, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cylinder(OpenSCADObject):
    def __init__(self, h=None, r1=None, r2=None, center=None, l=None, r=None, d=None, d1=None, d2=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cylinder", {"h" : h, "r1" : r1, "r2" : r2, "center" : center, "l" : l, "r" : r, "d" : d, "d1" : d1, "d2" : d2, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cyl(OpenSCADObject):
    def __init__(self, h=None, r=None, center=None, l=None, r1=None, r2=None, d=None, d1=None, d2=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, rounding=None, rounding1=None, rounding2=None, circum=None, realign=None, from_end=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cyl", {"h" : h, "r" : r, "center" : center, "l" : l, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "circum" : circum, "realign" : realign, "from_end" : from_end, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class xcyl(OpenSCADObject):
    def __init__(self, h=None, r=None, d=None, r1=None, r2=None, d1=None, d2=None, l=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, rounding=None, rounding1=None, rounding2=None, circum=None, realign=None, from_end=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("xcyl", {"h" : h, "r" : r, "d" : d, "r1" : r1, "r2" : r2, "d1" : d1, "d2" : d2, "l" : l, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "circum" : circum, "realign" : realign, "from_end" : from_end, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class ycyl(OpenSCADObject):
    def __init__(self, h=None, r=None, d=None, r1=None, r2=None, d1=None, d2=None, l=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, rounding=None, rounding1=None, rounding2=None, circum=None, realign=None, from_end=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("ycyl", {"h" : h, "r" : r, "d" : d, "r1" : r1, "r2" : r2, "d1" : d1, "d2" : d2, "l" : l, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "circum" : circum, "realign" : realign, "from_end" : from_end, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class zcyl(OpenSCADObject):
    def __init__(self, h=None, r=None, d=None, r1=None, r2=None, d1=None, d2=None, l=None, chamfer=None, chamfer1=None, chamfer2=None, chamfang=None, chamfang1=None, chamfang2=None, rounding=None, rounding1=None, rounding2=None, circum=None, realign=None, from_end=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("zcyl", {"h" : h, "r" : r, "d" : d, "r1" : r1, "r2" : r2, "d1" : d1, "d2" : d2, "l" : l, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "chamfang" : chamfang, "chamfang1" : chamfang1, "chamfang2" : chamfang2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "circum" : circum, "realign" : realign, "from_end" : from_end, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class tube(OpenSCADObject):
    def __init__(self, h=None, _or=None, ir=None, center=None, od=None, id=None, wall=None, or1=None, or2=None, od1=None, od2=None, ir1=None, ir2=None, id1=None, id2=None, realign=None, l=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("tube", {"h" : h, "_or" : _or, "ir" : ir, "center" : center, "od" : od, "id" : id, "wall" : wall, "or1" : or1, "or2" : or2, "od1" : od1, "od2" : od2, "ir1" : ir1, "ir2" : ir2, "id1" : id1, "id2" : id2, "realign" : realign, "l" : l, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class pie_slice(OpenSCADObject):
    def __init__(self, h=None, r=None, ang=None, center=None, r1=None, r2=None, d=None, d1=None, d2=None, l=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("pie_slice", {"h" : h, "r" : r, "ang" : ang, "center" : center, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "l" : l, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class sphere(OpenSCADObject):
    def __init__(self, r=None, d=None, circum=None, style=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("sphere", {"r" : r, "d" : d, "circum" : circum, "style" : style, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class spheroid(OpenSCADObject):
    def __init__(self, r=None, style=None, d=None, circum=None, dual=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("spheroid", {"r" : r, "style" : style, "d" : d, "circum" : circum, "dual" : dual, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class torus(OpenSCADObject):
    def __init__(self, r_maj=None, r_min=None, center=None, d_maj=None, d_min=None, _or=None, od=None, ir=None, id=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("torus", {"r_maj" : r_maj, "r_min" : r_min, "center" : center, "d_maj" : d_maj, "d_min" : d_min, "_or" : _or, "od" : od, "ir" : ir, "id" : id, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class teardrop(OpenSCADObject):
    def __init__(self, h=None, r=None, ang=None, cap_h=None, r1=None, r2=None, d=None, d1=None, d2=None, cap_h1=None, cap_h2=None, l=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("teardrop", {"h" : h, "r" : r, "ang" : ang, "cap_h" : cap_h, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "cap_h1" : cap_h1, "cap_h2" : cap_h2, "l" : l, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class onion(OpenSCADObject):
    def __init__(self, r=None, ang=None, cap_h=None, d=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("onion", {"r" : r, "ang" : ang, "cap_h" : cap_h, "d" : d, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class text3d(OpenSCADObject):
    def __init__(self, text=None, h=None, size=None, font=None, halign=None, valign=None, spacing=None, direction=None, language=None, script=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("text3d", {"text" : text, "h" : h, "size" : size, "font" : font, "halign" : halign, "valign" : valign, "spacing" : spacing, "direction" : direction, "language" : language, "script" : script, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class path_text(OpenSCADObject):
    def __init__(self, path=None, text=None, font=None, size=None, thickness=None, lettersize=None, offset=None, reverse=None, normal=None, top=None, center=None, textmetrics=None, kern=None, **kwargs):
       super().__init__("path_text", {"path" : path, "text" : text, "font" : font, "size" : size, "thickness" : thickness, "lettersize" : lettersize, "offset" : offset, "reverse" : reverse, "normal" : normal, "top" : top, "center" : center, "textmetrics" : textmetrics, "kern" : kern, **kwargs})

class interior_fillet(OpenSCADObject):
    def __init__(self, l=None, r=None, ang=None, overlap=None, d=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("interior_fillet", {"l" : l, "r" : r, "ang" : ang, "overlap" : overlap, "d" : d, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class heightfield(OpenSCADObject):
    def __init__(self, data=None, size=None, bottom=None, maxz=None, xrange=None, yrange=None, style=None, convexity=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("heightfield", {"data" : data, "size" : size, "bottom" : bottom, "maxz" : maxz, "xrange" : xrange, "yrange" : yrange, "style" : style, "convexity" : convexity, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cylindrical_heightfield(OpenSCADObject):
    def __init__(self, data=None, l=None, r=None, base=None, transpose=None, aspect=None, style=None, convexity=None, xrange=None, yrange=None, maxh=None, r1=None, r2=None, d=None, d1=None, d2=None, h=None, height=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cylindrical_heightfield", {"data" : data, "l" : l, "r" : r, "base" : base, "transpose" : transpose, "aspect" : aspect, "style" : style, "convexity" : convexity, "xrange" : xrange, "yrange" : yrange, "maxh" : maxh, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "h" : h, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class ruler(OpenSCADObject):
    def __init__(self, length=None, width=None, thickness=None, depth=None, labels=None, pipscale=None, maxscale=None, colors=None, alpha=None, unit=None, inch=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("ruler", {"length" : length, "width" : width, "thickness" : thickness, "depth" : depth, "labels" : labels, "pipscale" : pipscale, "maxscale" : maxscale, "colors" : colors, "alpha" : alpha, "unit" : unit, "inch" : inch, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cube(OpenSCADObject):
    def __init__(self, size=None, center=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cube", {"size" : size, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cuboid(OpenSCADObject):
    def __init__(self, size=None, p1=None, p2=None, chamfer=None, rounding=None, edges=None, except_edges=None, trimcorners=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cuboid", {"size" : size, "p1" : p1, "p2" : p2, "chamfer" : chamfer, "rounding" : rounding, "edges" : edges, "except_edges" : except_edges, "trimcorners" : trimcorners, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class prismoid(OpenSCADObject):
    def __init__(self, size1=None, size2=None, h=None, shift=None, rounding=None, rounding1=None, rounding2=None, chamfer=None, chamfer1=None, chamfer2=None, l=None, center=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("prismoid", {"size1" : size1, "size2" : size2, "h" : h, "shift" : shift, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "l" : l, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class octahedron(OpenSCADObject):
    def __init__(self, size=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("octahedron", {"size" : size, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class rect_tube(OpenSCADObject):
    def __init__(self, h=None, size=None, isize=None, center=None, shift=None, wall=None, size1=None, size2=None, isize1=None, isize2=None, rounding=None, rounding1=None, rounding2=None, irounding=None, irounding1=None, irounding2=None, chamfer=None, chamfer1=None, chamfer2=None, ichamfer=None, ichamfer1=None, ichamfer2=None, anchor=None, spin=None, orient=None, l=None, **kwargs):
       super().__init__("rect_tube", {"h" : h, "size" : size, "isize" : isize, "center" : center, "shift" : shift, "wall" : wall, "size1" : size1, "size2" : size2, "isize1" : isize1, "isize2" : isize2, "rounding" : rounding, "rounding1" : rounding1, "rounding2" : rounding2, "irounding" : irounding, "irounding1" : irounding1, "irounding2" : irounding2, "chamfer" : chamfer, "chamfer1" : chamfer1, "chamfer2" : chamfer2, "ichamfer" : ichamfer, "ichamfer1" : ichamfer1, "ichamfer2" : ichamfer2, "anchor" : anchor, "spin" : spin, "orient" : orient, "l" : l, **kwargs})

class wedge(OpenSCADObject):
    def __init__(self, size=None, center=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("wedge", {"size" : size, "center" : center, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cylinder(OpenSCADObject):
    def __init__(self, h=None, r1=None, r2=None, center=None, l=None, r=None, d=None, d1=None, d2=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cylinder", {"h" : h, "r1" : r1, "r2" : r2, "center" : center, "l" : l, "r" : r, "d" : d, "d1" : d1, "d2" : d2, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class pie_slice(OpenSCADObject):
    def __init__(self, h=None, r=None, ang=None, center=None, r1=None, r2=None, d=None, d1=None, d2=None, l=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("pie_slice", {"h" : h, "r" : r, "ang" : ang, "center" : center, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "l" : l, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class sphere(OpenSCADObject):
    def __init__(self, r=None, d=None, circum=None, style=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("sphere", {"r" : r, "d" : d, "circum" : circum, "style" : style, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _subsample_triangle(OpenSCADObject):
    def __init__(self, p=None, N=None, **kwargs):
       super().__init__("_subsample_triangle", {"p" : p, "N" : N, **kwargs})

class _dual_vertices(OpenSCADObject):
    def __init__(self, vnf=None, **kwargs):
       super().__init__("_dual_vertices", {"vnf" : vnf, **kwargs})

class spheroid(OpenSCADObject):
    def __init__(self, r=None, style=None, d=None, circum=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("spheroid", {"r" : r, "style" : style, "d" : d, "circum" : circum, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class torus(OpenSCADObject):
    def __init__(self, r_maj=None, r_min=None, center=None, d_maj=None, d_min=None, _or=None, od=None, ir=None, id=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("torus", {"r_maj" : r_maj, "r_min" : r_min, "center" : center, "d_maj" : d_maj, "d_min" : d_min, "_or" : _or, "od" : od, "ir" : ir, "id" : id, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class teardrop(OpenSCADObject):
    def __init__(self, h=None, r=None, ang=None, cap_h=None, r1=None, r2=None, d=None, d1=None, d2=None, cap_h1=None, cap_h2=None, l=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("teardrop", {"h" : h, "r" : r, "ang" : ang, "cap_h" : cap_h, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "cap_h1" : cap_h1, "cap_h2" : cap_h2, "l" : l, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class onion(OpenSCADObject):
    def __init__(self, r=None, ang=None, cap_h=None, d=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("onion", {"r" : r, "ang" : ang, "cap_h" : cap_h, "d" : d, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class _cut_interp(OpenSCADObject):
    def __init__(self, pathcut=None, path=None, data=None, **kwargs):
       super().__init__("_cut_interp", {"pathcut" : pathcut, "path" : path, "data" : data, **kwargs})

class heightfield(OpenSCADObject):
    def __init__(self, data=None, size=None, bottom=None, maxz=None, xrange=None, yrange=None, style=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("heightfield", {"data" : data, "size" : size, "bottom" : bottom, "maxz" : maxz, "xrange" : xrange, "yrange" : yrange, "style" : style, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

class cylindrical_heightfield(OpenSCADObject):
    def __init__(self, data=None, l=None, r=None, base=None, transpose=None, aspect=None, style=None, maxh=None, xrange=None, yrange=None, r1=None, r2=None, d=None, d1=None, d2=None, h=None, height=None, anchor=None, spin=None, orient=None, **kwargs):
       super().__init__("cylindrical_heightfield", {"data" : data, "l" : l, "r" : r, "base" : base, "transpose" : transpose, "aspect" : aspect, "style" : style, "maxh" : maxh, "xrange" : xrange, "yrange" : yrange, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, "h" : h, "height" : height, "anchor" : anchor, "spin" : spin, "orient" : orient, **kwargs})

