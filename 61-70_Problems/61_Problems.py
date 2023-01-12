# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from itertools import permutations

class GetOutOfLoop(Exception):
    pass

def triangle(n):
    return n*(n+1)//2

def square(n):
    return n*(2*n+0)//2

def pentagon(n):
    return n*(3*n-1)//2

def hexagon(n):
    return n*(4*n-2)//2

def heptagon(n):
    return n*(5*n-3)//2

def octagon(n):
    return n*(6*n-4)//2


polygon = [triangle, square, pentagon, hexagon, heptagon, octagon]

'''
for p in range(len(polygons)):
    polygon = polygons[p]
    def polygon(n):
        return  n*((p+1)+1-p)//2
'''

polygons = []


for i in range(6):
    count = 1
    polygons.append([])
    while polygon[i](count) < 10000:
        polygons[i].append(polygon[i](count))
        count+=1
    polygons[i] = list(filter(lambda x: x > 999, polygons[i]))
    polygons[i] = list(map(str,polygons[i]))


temp = [None]*6

orders = list(range(6))

try:
    for order in permutations(orders):
        for temp[0] in polygons[order[0]]:
            for temp[1] in polygons[order[1]]:
                if temp[0][-2:]==temp[1][:2]:
                    for temp[2] in polygons[order[2]]:
                        if temp[1][-2:]==temp[2][:2]:
                            for temp[3] in polygons[order[3]]:
                                if temp[2][-2:]==temp[3][:2]:
                                    for temp[4] in polygons[order[4]]:
                                        if temp[3][-2:]==temp[4][:2]:
                                            for temp[5] in polygons[order[5]]:
                                                if temp[4][-2:]==temp[5][:2]:
                                                    if temp[5][-2:]==temp[0][:2]:
                                                        print(temp, order, sum([int(i) for i in temp]))
                                                        raise GetOutOfLoop

except GetOutOfLoop:
    pass




'''
for p in polygons:
    print(str(list(map(p, range(1,6)))))
'''
    