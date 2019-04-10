#-*- coding:utf-8 -*
'''
Created on 2019. 4. 9.

@author: there
'''

# <주의> 반드시 while문을 활용해주세요. 
# <주의> 새로운 리스트를 만들거나, append 메소드를 사용하지 마세요. 
# <주의> 섭씨 온도 리스트의 원소가 정수형이든지, 소수점 첫째짜리까지든지, 원래 소수값이든지 상관없습니다. 
# <주의> 자동 채점 과제이기 때문에, 문제의 조건에 정확히 따라주시기 바랍니다. 띄어쓰기도 일치해야 합니다.
# 화씨 온도에서 섭씨 온도로 바꿔주는 함수
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32 ) * 5 / 9

# 테스트용 온도 리스트
sample_temperature_list = [40, 15, 32, 64, -4, 11]

# 화씨 온도 출력
print("화씨 온도 리스트: " + str(sample_temperature_list))

# 리스트의 값들을 화씨에서 섭씨로 변환
count = 0
while count < len(sample_temperature_list):
    sample_temperature_list[count] = round(fahrenheit_to_celsius(sample_temperature_list[count]), 2)
    count += 1

# 섭씨 온도 출력
print("섭씨 온도 리스트: " + str(sample_temperature_list))