#-*- coding:utf-8 -*-
'''
Created on 2019. 4. 8.

@author: there
'''

count = 0
previous = 0
current = 1

while count < 20:
    print(current)
    temp = previous
    previous = current
    current = temp + current
    count += 1
