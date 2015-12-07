#coding=utf8
from distutils.core import setup, Extension

'''
module1 = Extension(‘PyMesh’,
define_macros = [('PYMESH_EXPORTS', '1')],
libraries = ['MapSubdivision'],
library_dirs = [r'..\Test\Release'],
sources = ['PyMesh.cpp'])
'''

setup(name = "test_distutils",
version = "1.0.0",
description = "This is a demo package",
py_modules = ['test_distutils'],
#ext_modules=[module1],
)
