#!/usr/bin/python3
from ctypes import cdll
from sys import platform, argv

if platform == 'darwin':
    prefix = 'lib'
    ext = 'dylib'
elif platform == 'win32':
    prefix = ''
    ext = 'dll'
else:
    prefix = 'lib'
    ext = 'so'

lib = cdll.LoadLibrary('target/debug/{}sum_up.{}'.format(prefix, ext))
sum_up = lib.sum_up

sum_to = int(argv[1])
output = sum_up(sum_to)
print('your lucky digit calculated by rust is {}'.format(output))
