# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 09:52:25 2020

@author: aromi
"""
import math

start = 2
finish = 10000
count = 0
for num in range(start, finish+1):
    
    cf = []
    root = math.floor(math.sqrt(num))
    if math.sqrt(num)%1==0: 
        continue
    add, sub, div = root, -root, 1 
    cf.append([add, num, sub, div])
    match = False

    while not match:
        div = (num - sub**2)//div
        temp = (root - sub) // div
        add = temp
        sub = -sub - (temp * div)
        temp = [add, num, sub, div]
        
        if temp in cf:
            period = len(cf) - cf.index(temp)
            match = True
            if period % 2 == 1:
                count+=1
                'print(num)'
        cf.append(temp)
        
    'print(cf)'
print(count)