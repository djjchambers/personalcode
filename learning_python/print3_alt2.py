#!python
"Use 2.x/3.x keyword args deletion with defaults"
import sys

def print3(*args, **kargs):
    sep = kargs.pop('sep', ' ')
    end = karg.pop('end', '\n')
    file = kargs.pop('file', sys.stdout)
    if kargs: raise TypeError('extra keywords: %s' % kargs)
    output = ' '
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)