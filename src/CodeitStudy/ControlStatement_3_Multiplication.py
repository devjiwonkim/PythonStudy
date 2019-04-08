#-*- coding:utf-8 -*-
'''
Created on 2019. 4. 8.

@author: there
'''
first = 1


while first <= 9:
    second = 1
    while second <= 9:
        print("%d * %d = %d" % (first, second, first * second))
        second += 1       
    first += 1