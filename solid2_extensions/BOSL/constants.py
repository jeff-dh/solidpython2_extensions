from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent / Path('../'*1) / 'scad/BOSL/constants.scad'}", use_not_include=False)

PRINTER_SLOP = OpenSCADConstant('PRINTER_SLOP')
V_LEFT = OpenSCADConstant('V_LEFT')
V_RIGHT = OpenSCADConstant('V_RIGHT')
V_FWD = OpenSCADConstant('V_FWD')
V_BACK = OpenSCADConstant('V_BACK')
V_DOWN = OpenSCADConstant('V_DOWN')
V_UP = OpenSCADConstant('V_UP')
V_ALLPOS = OpenSCADConstant('V_ALLPOS')
V_ALLNEG = OpenSCADConstant('V_ALLNEG')
V_ZERO = OpenSCADConstant('V_ZERO')
V_CENTER = OpenSCADConstant('V_CENTER')
V_ABOVE = OpenSCADConstant('V_ABOVE')
V_BELOW = OpenSCADConstant('V_BELOW')
V_BEFORE = OpenSCADConstant('V_BEFORE')
V_BEHIND = OpenSCADConstant('V_BEHIND')
V_TOP = OpenSCADConstant('V_TOP')
V_BOTTOM = OpenSCADConstant('V_BOTTOM')
V_FRONT = OpenSCADConstant('V_FRONT')
V_REAR = OpenSCADConstant('V_REAR')
ALIGN_POS = OpenSCADConstant('ALIGN_POS')
ALIGN_CENTER = OpenSCADConstant('ALIGN_CENTER')
ALIGN_NEG = OpenSCADConstant('ALIGN_NEG')
ORIENT_X = OpenSCADConstant('ORIENT_X')
ORIENT_Y = OpenSCADConstant('ORIENT_Y')
ORIENT_Z = OpenSCADConstant('ORIENT_Z')
ORIENT_XNEG = OpenSCADConstant('ORIENT_XNEG')
ORIENT_YNEG = OpenSCADConstant('ORIENT_YNEG')
ORIENT_ZNEG = OpenSCADConstant('ORIENT_ZNEG')
ORIENT_X_90 = OpenSCADConstant('ORIENT_X_90')
ORIENT_Y_90 = OpenSCADConstant('ORIENT_Y_90')
ORIENT_Z_90 = OpenSCADConstant('ORIENT_Z_90')
ORIENT_XNEG_90 = OpenSCADConstant('ORIENT_XNEG_90')
ORIENT_YNEG_90 = OpenSCADConstant('ORIENT_YNEG_90')
ORIENT_ZNEG_90 = OpenSCADConstant('ORIENT_ZNEG_90')
ORIENT_X_180 = OpenSCADConstant('ORIENT_X_180')
ORIENT_Y_180 = OpenSCADConstant('ORIENT_Y_180')
ORIENT_Z_180 = OpenSCADConstant('ORIENT_Z_180')
ORIENT_XNEG_180 = OpenSCADConstant('ORIENT_XNEG_180')
ORIENT_YNEG_180 = OpenSCADConstant('ORIENT_YNEG_180')
ORIENT_ZNEG_180 = OpenSCADConstant('ORIENT_ZNEG_180')
ORIENT_X_270 = OpenSCADConstant('ORIENT_X_270')
ORIENT_Y_270 = OpenSCADConstant('ORIENT_Y_270')
ORIENT_Z_270 = OpenSCADConstant('ORIENT_Z_270')
ORIENT_XNEG_270 = OpenSCADConstant('ORIENT_XNEG_270')
ORIENT_YNEG_270 = OpenSCADConstant('ORIENT_YNEG_270')
ORIENT_ZNEG_270 = OpenSCADConstant('ORIENT_ZNEG_270')
EDGE_TOP_BK = OpenSCADConstant('EDGE_TOP_BK')
EDGE_TOP_FR = OpenSCADConstant('EDGE_TOP_FR')
EDGE_BOT_FR = OpenSCADConstant('EDGE_BOT_FR')
EDGE_BOT_BK = OpenSCADConstant('EDGE_BOT_BK')
EDGE_TOP_RT = OpenSCADConstant('EDGE_TOP_RT')
EDGE_TOP_LF = OpenSCADConstant('EDGE_TOP_LF')
EDGE_BOT_LF = OpenSCADConstant('EDGE_BOT_LF')
EDGE_BOT_RT = OpenSCADConstant('EDGE_BOT_RT')
EDGE_BK_RT = OpenSCADConstant('EDGE_BK_RT')
EDGE_BK_LF = OpenSCADConstant('EDGE_BK_LF')
EDGE_FR_LF = OpenSCADConstant('EDGE_FR_LF')
EDGE_FR_RT = OpenSCADConstant('EDGE_FR_RT')
EDGES_X_TOP = OpenSCADConstant('EDGES_X_TOP')
EDGES_X_BOT = OpenSCADConstant('EDGES_X_BOT')
EDGES_X_FR = OpenSCADConstant('EDGES_X_FR')
EDGES_X_BK = OpenSCADConstant('EDGES_X_BK')
EDGES_X_ALL = OpenSCADConstant('EDGES_X_ALL')
EDGES_Y_TOP = OpenSCADConstant('EDGES_Y_TOP')
EDGES_Y_BOT = OpenSCADConstant('EDGES_Y_BOT')
EDGES_Y_LF = OpenSCADConstant('EDGES_Y_LF')
EDGES_Y_RT = OpenSCADConstant('EDGES_Y_RT')
EDGES_Y_ALL = OpenSCADConstant('EDGES_Y_ALL')
EDGES_Z_BK = OpenSCADConstant('EDGES_Z_BK')
EDGES_Z_FR = OpenSCADConstant('EDGES_Z_FR')
EDGES_Z_LF = OpenSCADConstant('EDGES_Z_LF')
EDGES_Z_RT = OpenSCADConstant('EDGES_Z_RT')
EDGES_Z_ALL = OpenSCADConstant('EDGES_Z_ALL')
EDGES_LEFT = OpenSCADConstant('EDGES_LEFT')
EDGES_RIGHT = OpenSCADConstant('EDGES_RIGHT')
EDGES_FRONT = OpenSCADConstant('EDGES_FRONT')
EDGES_BACK = OpenSCADConstant('EDGES_BACK')
EDGES_BOTTOM = OpenSCADConstant('EDGES_BOTTOM')
EDGES_TOP = OpenSCADConstant('EDGES_TOP')
EDGES_NONE = OpenSCADConstant('EDGES_NONE')
EDGES_ALL = OpenSCADConstant('EDGES_ALL')
EDGE_OFFSETS = OpenSCADConstant('EDGE_OFFSETS')
class corner_edge_count(OpenSCADObject):
    def __init__(self, edges=None, v=None, **kwargs):
       super().__init__("corner_edge_count", {"edges" : edges, "v" : v, **kwargs})

