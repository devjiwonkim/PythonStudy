#-*- coding:utf-8 -*
'''
Created on 2019. 4. 10.

@author: there
'''
# 원(￦)에서 달러($)로 바꿔주는 함수
def krw_to_usd(won):
    return float(won * 0.001)

# 달러($)에서 엔(￥)로 바꿔주는 함수
def usd_to_jpy(dollars):
    return float(dollars * 125)
    # 코드를 입력하세요.

count = 0
count2 = 0

# 원(￦)으로 각각 얼마인가요?
amounts = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000]
print("한국 화폐: " + str(amounts))

# amounts를 원(￦)에서 달러($)로 바꿔주기
while count < len(amounts):
    amounts[count] = round(krw_to_usd(amounts[count]), 1)
    count = count + 1
# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(amounts))


# amounts를 달러($)에서 엔(￥)으로 바꿔주기
while count2 < len(amounts):
    amounts[count2] = round(usd_to_jpy(amounts[count2]), 1)
    count2 = count2 + 1

# 엔(￥)으로 각각 얼마인가요?
print("일본 화폐: " + str(amounts))