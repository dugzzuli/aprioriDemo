# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 16:10:40 2017

@author: dugking
"""
def gen(D, minSup):
    C1 = {}
    for T in D:
        for I in T:
            if I in C1:
                C1[I] += 1
            else:
                C1[I] = 1
    print(C1)
    _keys1 = C1.keys()
    print(_keys1)
    keys1=[]
    for i in _keys1:
        keys1.append([i])

    print(keys1[:])
    cutKeys1 = []
    for k in keys1[:]:
        cutKeys1.append(k)
    cutKeys1.sort()
    print(cutKeys1)
D = [['A','B','C','D'],['B','C','E'],['A','B','C','E'],['B','D','E'],['A','B','C','D']]
gen(D, 0.7) 