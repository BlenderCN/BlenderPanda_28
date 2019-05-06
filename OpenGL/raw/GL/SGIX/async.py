'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_SGIX_async'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_SGIX_async',error_checker=_errors._error_checker)
GL_ASYNC_MARKER_SGIX=_C('GL_ASYNC_MARKER_SGIX',0x8329)
@_f
@_p.types(None,_cs.GLuint)
def glAsyncMarkerSGIX(marker):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLsizei)
def glDeleteAsyncMarkersSGIX(marker,range):pass
@_f
@_p.types(_cs.GLint,arrays.GLuintArray)
def glFinishAsyncSGIX(markerp):pass
@_f
@_p.types(_cs.GLuint,_cs.GLsizei)
def glGenAsyncMarkersSGIX(range):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsAsyncMarkerSGIX(marker):pass
@_f
@_p.types(_cs.GLint,arrays.GLuintArray)
def glPollAsyncSGIX(markerp):pass