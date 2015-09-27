# -*- coding: utf-8 -*-

from ctypes import  *

def print_line(objs):
    print '\t'.join('{0: <12}'.format(x) for x in objs)

def print_class_info(dict):
    print_line(('ctypes', 'Python', 'C/C++', 'default value'))
    print_line(('------', '------', '-----', '-------------'))
    for pyClass, pyType in dict.items():
        print_line((pyClass.__name__, pyType, pyClass._type_, pyClass().value))

dict = {c_char: '1-char-string', c_wchar: '1-char-unicode',
        c_byte: 'int/long', c_ubyte: 'int/long',
        c_short: 'int/long', c_ushort: 'int/long',
        c_int: 'int/long', c_uint: 'int/long',
        c_long: 'int/long', c_ulong: 'int/long', c_longlong: 'int/long', c_ulonglong: 'int/long',
        c_float: 'float', c_double: 'float',
        c_char_p: 'string/None', c_wchar_p: 'unicode/Node',
        c_void_p: 'int/long/Node'}

print_class_info(dict)