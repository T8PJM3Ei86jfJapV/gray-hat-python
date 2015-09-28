# -*- coding: utf-8 -*-

from ctypes import  *

# Microsoft VC Runtime Library
libc = cdll.msvcrt

def print_line(objs):
    print '\t'.join('{0: <12}'.format(x) for x in objs)

# 打印数据类型信息
def print_class_info(dict):
    for pyClass, pyType in dict.items():
        print_line((pyClass.__name__, pyType, pyClass._type_, pyClass().value))

# ctypes常用数据类型
dicts = [{c_char: '1-char-string', c_wchar: '1-char-unicode'},
        {c_byte: 'int/long', c_ubyte: 'int/long'},
        {c_short: 'int/long', c_ushort: 'int/long'},
        {c_int: 'int/long', c_uint: 'int/long'},
        {c_long: 'int/long', c_ulong: 'int/long', c_longlong: 'int/long', c_ulonglong: 'int/long'},
        {c_float: 'float', c_double: 'float'},
        {c_char_p: 'string/None', c_wchar_p: 'unicode/Node'},
        {c_void_p: 'int/long/Node'}]

def main():
    # ctypes, Python, C/C++数据类型的对应关系
    print_line(('ctypes', 'Python', 'C/C++', 'default value'))
    print_line(('------', '------', '-----', '-------------'))
    for dict in dicts:
        print_class_info(dict)
        
    # 初始化
    print '\nInitializing:'
    print '-------------'
    print 'c_ushort(-1).value: \t', c_ushort(-1).value
    print 'c_uint(-1).value: \t', c_uint(-1).value
    print 'c_ulong(-1).value: \t', c_ulong(-1).value
    print 'c_ulong(2**32).value: \t', c_ulong(2**32).value
    
    # 指针与引用
    print '\nPointer & Reference:'
    print '------------------'
    i = c_int()
    f = c_float()
    s = create_string_buffer('\000' * 32)
    libc.sscanf("1 3.14 Hello", "%d %f %s", byref(i), byref(f), s)
    libc.memset(s, ord('x'), 2)
    libc.printf("%d, %f, %s", i, f, repr(s.value))
    
if __name__ == "__main__":
    main()