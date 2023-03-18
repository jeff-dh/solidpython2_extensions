from solid2.core.object_base import OpenSCADObject, OpenSCADConstant
from solid2.core.scad_import import extra_scad_include
from pathlib import Path

extra_scad_include(f"{Path(__file__).parent.parent / 'scad/BOSL2/strings.scad'}", use_not_include=False)

class substr(OpenSCADObject):
    def __init__(self, str=None, pos=None, len=None, **kwargs):
       super().__init__("substr", {"str" : str, "pos" : pos, "len" : len, **kwargs})

class _substr(OpenSCADObject):
    def __init__(self, str=None, pos=None, len=None, substr=None, **kwargs):
       super().__init__("_substr", {"str" : str, "pos" : pos, "len" : len, "substr" : substr, **kwargs})

class suffix(OpenSCADObject):
    def __init__(self, str=None, len=None, **kwargs):
       super().__init__("suffix", {"str" : str, "len" : len, **kwargs})

class str_find(OpenSCADObject):
    def __init__(self, str=None, pattern=None, start=None, last=None, all=None, **kwargs):
       super().__init__("str_find", {"str" : str, "pattern" : pattern, "start" : start, "last" : last, "all" : all, **kwargs})

class _str_find_first(OpenSCADObject):
    def __init__(self, str=None, pattern=None, max_sindex=None, sindex=None, **kwargs):
       super().__init__("_str_find_first", {"str" : str, "pattern" : pattern, "max_sindex" : max_sindex, "sindex" : sindex, **kwargs})

class _str_find_last(OpenSCADObject):
    def __init__(self, str=None, pattern=None, sindex=None, **kwargs):
       super().__init__("_str_find_last", {"str" : str, "pattern" : pattern, "sindex" : sindex, **kwargs})

class _str_find_all(OpenSCADObject):
    def __init__(self, str=None, pattern=None, **kwargs):
       super().__init__("_str_find_all", {"str" : str, "pattern" : pattern, **kwargs})

class _str_cmp(OpenSCADObject):
    def __init__(self, str=None, sindex=None, pattern=None, **kwargs):
       super().__init__("_str_cmp", {"str" : str, "sindex" : sindex, "pattern" : pattern, **kwargs})

class _str_cmp_recurse(OpenSCADObject):
    def __init__(self, str=None, sindex=None, pattern=None, plen=None, pindex=None, **kwargs):
       super().__init__("_str_cmp_recurse", {"str" : str, "sindex" : sindex, "pattern" : pattern, "plen" : plen, "pindex" : pindex, **kwargs})

class starts_with(OpenSCADObject):
    def __init__(self, str=None, pattern=None, **kwargs):
       super().__init__("starts_with", {"str" : str, "pattern" : pattern, **kwargs})

class ends_with(OpenSCADObject):
    def __init__(self, str=None, pattern=None, **kwargs):
       super().__init__("ends_with", {"str" : str, "pattern" : pattern, **kwargs})

class str_split(OpenSCADObject):
    def __init__(self, str=None, sep=None, keep_nulls=None, **kwargs):
       super().__init__("str_split", {"str" : str, "sep" : sep, "keep_nulls" : keep_nulls, **kwargs})

class _str_split_recurse(OpenSCADObject):
    def __init__(self, str=None, sep=None, i=None, result=None, **kwargs):
       super().__init__("_str_split_recurse", {"str" : str, "sep" : sep, "i" : i, "result" : result, **kwargs})

class _remove_empty_strs(OpenSCADObject):
    def __init__(self, list=None, **kwargs):
       super().__init__("_remove_empty_strs", {"list" : list, **kwargs})

class str_join(OpenSCADObject):
    def __init__(self, list=None, sep=None, _i=None, _result=None, **kwargs):
       super().__init__("str_join", {"list" : list, "sep" : sep, "_i" : _i, "_result" : _result, **kwargs})

class _str_count_leading(OpenSCADObject):
    def __init__(self, s=None, c=None, _i=None, **kwargs):
       super().__init__("_str_count_leading", {"s" : s, "c" : c, "_i" : _i, **kwargs})

class _str_count_trailing(OpenSCADObject):
    def __init__(self, s=None, c=None, _i=None, **kwargs):
       super().__init__("_str_count_trailing", {"s" : s, "c" : c, "_i" : _i, **kwargs})

class str_strip(OpenSCADObject):
    def __init__(self, s=None, c=None, start=None, end=None, **kwargs):
       super().__init__("str_strip", {"s" : s, "c" : c, "start" : start, "end" : end, **kwargs})

class str_pad(OpenSCADObject):
    def __init__(self, str=None, length=None, char=None, left=None, **kwargs):
       super().__init__("str_pad", {"str" : str, "length" : length, "char" : char, "left" : left, **kwargs})

class str_replace_char(OpenSCADObject):
    def __init__(self, str=None, char=None, replace=None, **kwargs):
       super().__init__("str_replace_char", {"str" : str, "char" : char, "replace" : replace, **kwargs})

class downcase(OpenSCADObject):
    def __init__(self, str=None, **kwargs):
       super().__init__("downcase", {"str" : str, **kwargs})

class upcase(OpenSCADObject):
    def __init__(self, str=None, **kwargs):
       super().__init__("upcase", {"str" : str, **kwargs})

class rand_str(OpenSCADObject):
    def __init__(self, n=None, charset=None, seed=None, **kwargs):
       super().__init__("rand_str", {"n" : n, "charset" : charset, "seed" : seed, **kwargs})

class parse_int(OpenSCADObject):
    def __init__(self, str=None, base=None, **kwargs):
       super().__init__("parse_int", {"str" : str, "base" : base, **kwargs})

class _parse_int_recurse(OpenSCADObject):
    def __init__(self, str=None, base=None, i=None, **kwargs):
       super().__init__("_parse_int_recurse", {"str" : str, "base" : base, "i" : i, **kwargs})

class parse_float(OpenSCADObject):
    def __init__(self, str=None, **kwargs):
       super().__init__("parse_float", {"str" : str, **kwargs})

class parse_frac(OpenSCADObject):
    def __init__(self, str=None, mixed=None, improper=None, signed=None, **kwargs):
       super().__init__("parse_frac", {"str" : str, "mixed" : mixed, "improper" : improper, "signed" : signed, **kwargs})

class parse_num(OpenSCADObject):
    def __init__(self, str=None, **kwargs):
       super().__init__("parse_num", {"str" : str, **kwargs})

class format_int(OpenSCADObject):
    def __init__(self, i=None, mindigits=None, **kwargs):
       super().__init__("format_int", {"i" : i, "mindigits" : mindigits, **kwargs})

class format_fixed(OpenSCADObject):
    def __init__(self, f=None, digits=None, **kwargs):
       super().__init__("format_fixed", {"f" : f, "digits" : digits, **kwargs})

class format_float(OpenSCADObject):
    def __init__(self, f=None, sig=None, **kwargs):
       super().__init__("format_float", {"f" : f, "sig" : sig, **kwargs})

class _format_matrix(OpenSCADObject):
    def __init__(self, M=None, sig=None, sep=None, eps=None, **kwargs):
       super().__init__("_format_matrix", {"M" : M, "sig" : sig, "sep" : sep, "eps" : eps, **kwargs})

class format(OpenSCADObject):
    def __init__(self, fmt=None, vals=None, **kwargs):
       super().__init__("format", {"fmt" : fmt, "vals" : vals, **kwargs})

class is_lower(OpenSCADObject):
    def __init__(self, s=None, **kwargs):
       super().__init__("is_lower", {"s" : s, **kwargs})

class is_upper(OpenSCADObject):
    def __init__(self, s=None, **kwargs):
       super().__init__("is_upper", {"s" : s, **kwargs})

class is_digit(OpenSCADObject):
    def __init__(self, s=None, **kwargs):
       super().__init__("is_digit", {"s" : s, **kwargs})

class is_hexdigit(OpenSCADObject):
    def __init__(self, s=None, **kwargs):
       super().__init__("is_hexdigit", {"s" : s, **kwargs})

class is_letter(OpenSCADObject):
    def __init__(self, s=None, **kwargs):
       super().__init__("is_letter", {"s" : s, **kwargs})

