#-*- coding:utf-8 -*-
'''
Created on 2019. 4. 8.

@author: there
'''
AprtmentPrice = 1100000000
OriginalPrice = 50000000
BankRate = 0.12

Year = 1988
ThisYear = 2016

while Year < ThisYear:
    OriginalPrice = int(OriginalPrice * (1 + BankRate))
    print("Original : " + str(OriginalPrice))
    Year += 1

if OriginalPrice > AprtmentPrice:
    Diff = OriginalPrice - AprtmentPrice
    print("%d 차이로 동일 아저씨의 말씀이 맞습니다." % (Diff))
else:
    Diff = AprtmentPrice - OriginalPrice
    print("%d 차이로 미란 아주머니의 말씀이 맞습니다." % (Diff))
