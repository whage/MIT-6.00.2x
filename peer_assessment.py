# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 21:54:30 2016

@author: Sam
"""

from itertools import chain, combinations

def powerSet(items):
    return chain.from_iterable(combinations(items,n) for n in range(len(items)+1))

p = powerSet(['a', 'b', 'c'])

for result in p:
	print(result)

results = list(powerSet([1, 2, 3]))
print(results)