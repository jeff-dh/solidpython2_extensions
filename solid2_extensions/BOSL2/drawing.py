from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/drawing.scad'}", use_not_include=False)

class stroke(OpenSCADObject):
    def __init__(self, path=None, width=None, closed=None, endcaps=None, endcap1=None, endcap2=None, joints=None, dots=None, endcap_width=None, endcap_width1=None, endcap_width2=None, joint_width=None, dots_width=None, endcap_length=None, endcap_length1=None, endcap_length2=None, joint_length=None, dots_length=None, endcap_extent=None, endcap_extent1=None, endcap_extent2=None, joint_extent=None, dots_extent=None, endcap_angle=None, endcap_angle1=None, endcap_angle2=None, joint_angle=None, dots_angle=None, endcap_color=None, endcap_color1=None, endcap_color2=None, joint_color=None, dots_color=None, color=None, trim=None, trim1=None, trim2=None, convexity=None, hull=None, **kwargs):
       super().__init__("stroke", {"path" : path, "width" : width, "closed" : closed, "endcaps" : endcaps, "endcap1" : endcap1, "endcap2" : endcap2, "joints" : joints, "dots" : dots, "endcap_width" : endcap_width, "endcap_width1" : endcap_width1, "endcap_width2" : endcap_width2, "joint_width" : joint_width, "dots_width" : dots_width, "endcap_length" : endcap_length, "endcap_length1" : endcap_length1, "endcap_length2" : endcap_length2, "joint_length" : joint_length, "dots_length" : dots_length, "endcap_extent" : endcap_extent, "endcap_extent1" : endcap_extent1, "endcap_extent2" : endcap_extent2, "joint_extent" : joint_extent, "dots_extent" : dots_extent, "endcap_angle" : endcap_angle, "endcap_angle1" : endcap_angle1, "endcap_angle2" : endcap_angle2, "joint_angle" : joint_angle, "dots_angle" : dots_angle, "endcap_color" : endcap_color, "endcap_color1" : endcap_color1, "endcap_color2" : endcap_color2, "joint_color" : joint_color, "dots_color" : dots_color, "color" : color, "trim" : trim, "trim1" : trim1, "trim2" : trim2, "convexity" : convexity, "hull" : hull, **kwargs})

class dashed_stroke(OpenSCADObject):
    def __init__(self, path=None, dashpat=None, width=None, closed=None, **kwargs):
       super().__init__("dashed_stroke", {"path" : path, "dashpat" : dashpat, "width" : width, "closed" : closed, **kwargs})

class arc(OpenSCADObject):
    def __init__(self, n=None, r=None, angle=None, d=None, cp=None, points=None, corner=None, width=None, thickness=None, start=None, wedge=None, anchor=None, spin=None, **kwargs):
       super().__init__("arc", {"n" : n, "r" : r, "angle" : angle, "d" : d, "cp" : cp, "points" : points, "corner" : corner, "width" : width, "thickness" : thickness, "start" : start, "wedge" : wedge, "anchor" : anchor, "spin" : spin, **kwargs})

class helix(OpenSCADObject):
    def __init__(self, l=None, h=None, turns=None, angle=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, **kwargs):
       super().__init__("helix", {"l" : l, "h" : h, "turns" : turns, "angle" : angle, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, **kwargs})

class turtle(OpenSCADObject):
    def __init__(self, commands=None, state=None, full_state=None, repeat=None, **kwargs):
       super().__init__("turtle", {"commands" : commands, "state" : state, "full_state" : full_state, "repeat" : repeat, **kwargs})

class debug_polygon(OpenSCADObject):
    def __init__(self, points=None, paths=None, vertices=None, edges=None, convexity=None, size=None, **kwargs):
       super().__init__("debug_polygon", {"points" : points, "paths" : paths, "vertices" : vertices, "edges" : edges, "convexity" : convexity, "size" : size, **kwargs})

class stroke(OpenSCADObject):
    def __init__(self, path=None, width=None, closed=None, endcaps=None, endcap1=None, endcap2=None, joints=None, dots=None, endcap_width=None, endcap_width1=None, endcap_width2=None, joint_width=None, dots_width=None, endcap_length=None, endcap_length1=None, endcap_length2=None, joint_length=None, dots_length=None, endcap_extent=None, endcap_extent1=None, endcap_extent2=None, joint_extent=None, dots_extent=None, endcap_angle=None, endcap_angle1=None, endcap_angle2=None, joint_angle=None, dots_angle=None, endcap_color=None, endcap_color1=None, endcap_color2=None, joint_color=None, dots_color=None, color=None, trim=None, trim1=None, trim2=None, convexity=None, hull=None, **kwargs):
       super().__init__("stroke", {"path" : path, "width" : width, "closed" : closed, "endcaps" : endcaps, "endcap1" : endcap1, "endcap2" : endcap2, "joints" : joints, "dots" : dots, "endcap_width" : endcap_width, "endcap_width1" : endcap_width1, "endcap_width2" : endcap_width2, "joint_width" : joint_width, "dots_width" : dots_width, "endcap_length" : endcap_length, "endcap_length1" : endcap_length1, "endcap_length2" : endcap_length2, "joint_length" : joint_length, "dots_length" : dots_length, "endcap_extent" : endcap_extent, "endcap_extent1" : endcap_extent1, "endcap_extent2" : endcap_extent2, "joint_extent" : joint_extent, "dots_extent" : dots_extent, "endcap_angle" : endcap_angle, "endcap_angle1" : endcap_angle1, "endcap_angle2" : endcap_angle2, "joint_angle" : joint_angle, "dots_angle" : dots_angle, "endcap_color" : endcap_color, "endcap_color1" : endcap_color1, "endcap_color2" : endcap_color2, "joint_color" : joint_color, "dots_color" : dots_color, "color" : color, "trim" : trim, "trim1" : trim1, "trim2" : trim2, "convexity" : convexity, "hull" : hull, **kwargs})

class dashed_stroke(OpenSCADObject):
    def __init__(self, path=None, dashpat=None, closed=None, **kwargs):
       super().__init__("dashed_stroke", {"path" : path, "dashpat" : dashpat, "closed" : closed, **kwargs})

class arc(OpenSCADObject):
    def __init__(self, n=None, r=None, angle=None, d=None, cp=None, points=None, corner=None, width=None, thickness=None, start=None, wedge=None, long=None, cw=None, ccw=None, endpoint=None, **kwargs):
       super().__init__("arc", {"n" : n, "r" : r, "angle" : angle, "d" : d, "cp" : cp, "points" : points, "corner" : corner, "width" : width, "thickness" : thickness, "start" : start, "wedge" : wedge, "long" : long, "cw" : cw, "ccw" : ccw, "endpoint" : endpoint, **kwargs})

class helix(OpenSCADObject):
    def __init__(self, l=None, h=None, turns=None, angle=None, r=None, r1=None, r2=None, d=None, d1=None, d2=None, **kwargs):
       super().__init__("helix", {"l" : l, "h" : h, "turns" : turns, "angle" : angle, "r" : r, "r1" : r1, "r2" : r2, "d" : d, "d1" : d1, "d2" : d2, **kwargs})

class _normal_segment(OpenSCADObject):
    def __init__(self, p1=None, p2=None, **kwargs):
       super().__init__("_normal_segment", {"p1" : p1, "p2" : p2, **kwargs})

class turtle(OpenSCADObject):
    def __init__(self, commands=None, state=None, full_state=None, repeat=None, **kwargs):
       super().__init__("turtle", {"commands" : commands, "state" : state, "full_state" : full_state, "repeat" : repeat, **kwargs})

class _turtle_repeat(OpenSCADObject):
    def __init__(self, commands=None, state=None, full_state=None, repeat=None, **kwargs):
       super().__init__("_turtle_repeat", {"commands" : commands, "state" : state, "full_state" : full_state, "repeat" : repeat, **kwargs})

class _turtle_command_len(OpenSCADObject):
    def __init__(self, commands=None, index=None, **kwargs):
       super().__init__("_turtle_command_len", {"commands" : commands, "index" : index, **kwargs})

class _turtle(OpenSCADObject):
    def __init__(self, commands=None, state=None, full_state=None, index=None, **kwargs):
       super().__init__("_turtle", {"commands" : commands, "state" : state, "full_state" : full_state, "index" : index, **kwargs})

class _turtle_command(OpenSCADObject):
    def __init__(self, command=None, parm=None, parm2=None, state=None, index=None, **kwargs):
       super().__init__("_turtle_command", {"command" : command, "parm" : parm, "parm2" : parm2, "state" : state, "index" : index, **kwargs})

