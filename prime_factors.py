#!/usr/bin/env python
"""
This script tries to find the prime factors for the number RSA-260
from the RSA Factoring Challenge ended in 2007.

Warning: The script will most likely not finish, as it is extremely
hard to perform the prime factorization.
"""
import sympy

rsa_260 = 22112825529529666435281085255026230927612089502470015394413748319128822941402001986512729726569746599085900330031400051170742204560859276357953757185954298838958709229238491006703034124620545784566413664540684214361293017694020846391065875914794251435144458199

print("Start factoring...")
factors = sympy.factorint(rsa_260)

# Will probably not be reached
print(factors)
