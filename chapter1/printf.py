#-*-coding:utf-8-*-

from ctypes import cdll

# Microsoft VC Runtime Library
libc = cdll.msvcrt

# Linux C Library Shared Object
# from ctypes import CDLL
# libc = CDLL('libc.so.6)

massage = 'Hello World!\n'
print libc.printf("Printing by msvcrt: %s", massage)
