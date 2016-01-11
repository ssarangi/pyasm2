from distutils.core import setup, Extension

jittermodule = Extension('jitter',
                         sources = ['jitter/jittermodule.c'])

setup (name = 'PackageName',
       version = '1.0',
       description = 'This is the Jitter Module for Pyasm2',
       ext_modules = [jittermodule])
