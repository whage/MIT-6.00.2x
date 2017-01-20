#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 21:07:05 2016

@author: yinuochen
"""

from itertools import chain, combinations

def powerSet(i):
    for subset in chain.from_iterable(combinations(i, r) for r in range(len(i)+1)):
        yield subset

for i in powerSet([1,2,3,4]):
	print i        