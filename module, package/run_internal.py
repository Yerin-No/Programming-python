#math
import math
print(math.ceil(3.5))   #4 올림
print(math.floor(3.5))  #3 내림
print(round(3.5))       #4 반올림
print(math.pow(2, 10))   #1024.0
print(math.sin(math.pi/2))  #1.0
#print(math.sin(math.pi))

#random
print('-'*20)
import random
print(random.random())  #java random: 0.0 <= r <1.0
print(random.randrange(1, 10))  #1 <= r <10 정수
print(random.randint(1, 10))    #1 <= r <= 10 정수

list1 = ['굶었음','피자','김치찜','닭가슴살']
print(random.choice(list1))      #list1 중 하나

print('before: ',list1)
print(random.shuffle(list1))    #list1 섞기
print('after: ',list1)

print(random.sample(list1, 2))  #list1에서 랜덤으로 n개 뽑기

#datetime
print('-'*20)
import datetime
now = datetime.datetime.now()
print(now.day)
print(now.hour)
birthday = datetime.datetime(2004, 11, 29)
print(birthday)
print(now - birthday)

#문제
print('-'*30)
'''핸드폰 요금이 62421원이 나왔다. 100원 미만은 절사한다고 한다.62400원 청구
59827원일 경우 실제 청구 금액은?'''
money = 59827
print(money//100*100)
print(money-money % 100)
print(math.floor(money/100)*100)
print(int(money/100)*100)

'''평가 계획은 100점 만점에 10점 단위로 점수를 줄 수 있다.
채점한 결과 93점이 나왔다. 90점부여 56점은 몇 점 부여?'''
score = 56
print(round(score/10)*10)
print(round(score, -1))

'''로또 복권 자동 생성기를 만든다면?
(로또복권:1~45 사이의 번호 중 랜덤으로 6개 뽑기'''
import random

print(random.sample(range(1, 45 +1),6))

'''1~9숫자로 중복되지 않은 숫자 세자리를 뽑는 방법은?'''
list_r = random.sample(range(1, 9 + 1),3)
print(list_r)
# print(str(list_r)) 리스트 그래도 출력됨
print("".join(str(n)for n in list_r))
print("".join(map(str, list_r)))

'''내가 태어난 날로부터 며칠이 지났는지?'''
import datetime

birth = datetime.datetime(2004, 8, 28)
time = now - birth
print("태어난지", time.days, "일")

'''올해 크리스마스까지 며칠이 남았는지?'''
chrismas = datetime.datetime(2021,12,25)
how = chrismas - datetime.datetime.now()

print('크리스마스 까지는 {}일'.format(how.days))

'''내 생일이 며칠이 남았는지?'''
birthday = datetime.datetime(2021,8,28)
if birthday < now:
    birthday = birthday.replace(year=2022)
print(birthday-now)

'''랜덤하게 번호로 자리를 배치하는 방법은?'''
#마지막 번호 묻기
last_number = input("마지막 번호는?")     #19
#마지막번호까지 숫자 리스트 만들기
list_class = list(range(1, int(last_number) + 1))
print(list_class)
#반복
while True:
    #뺄 번호 묻기
    exclude_number = input("빨 번호는?(enter치면 그만 빼기)")
    #다 뻈으면 반복 끝내기
    if exclude_number == '':
        break
    #빼기
    list_class.remove(int(exclude_number))
    print(list_class)
#섞기
random.shuffle(list_class)
#출력
print('자리\t학생번호')
for i, number in enumerate(list_class):
    print(f'{i+1}\t{number}')