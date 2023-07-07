#!/usr/bin/env python
"""
This script runs a test of the Kyber encryption system, which
is implemented in C and invoked from a shared library. The
C code is based on the Kyber reference implementation.
"""
import os
import ctypes

# Load shared library
libname = f"{os.getcwd()}/execute_round_trip1024.so"
clib = ctypes.CDLL(libname, mode=1)
print("Shared lib loaded successfully:")
print(clib)

# Call round trip function
print("Executing round trip:")
clib.round_trip()
