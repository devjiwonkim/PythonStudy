#-*- coding:utf-8 -*
'''
Created on 2019. 4. 8.

@author: there
'''
from random import randint

tries = 0
answer = randint(1, 20)

while tries < 4:
    guess = int(input("기회가  %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요 : " % (4 - tries)))
    if answer > guess:
        tries += 1
        print("Up")
        if tries == 4:
            print("아쉽습니다. 정답은 %d였습니다." % (answer))
            break
    elif answer < guess:
        tries += 1
        print("Down")
        if tries == 4:
            print("아쉽습니다. 정답은 %d였습니다." % (answer))
            break
    else:
        print("축하합니다. %d번 만에 숫자를 맞추셨습니다." % (tries + 1))
        break
