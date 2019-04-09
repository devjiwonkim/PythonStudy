#-*- coding:utf-8 -*
'''
Created on 2019. 4. 8.

@author: there
'''
from random import randint

count = 0
Chance = 4

while count < Chance:
    RandomNumber = randint(1,2)
    guess = int(input("기회가  %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요 : " % (Chance-count)))
    if count == 4:
        print("아쉽습니다. 정답은 %d 였습니다." % (RandomNumber))
        break
    else:     
        if guess == RandomNumber:
            count += 1            
            print("축하합니다. %d번만에 숫자를 맞추셨습니다." %(count))
            break
        elif guess > RandomNumber:
            count += 1
            Chance = Chance - count
            print("Down")
        elif guess < RandomNumber:
            count += 1
            Chance = Chance - count
            print("Up")


        