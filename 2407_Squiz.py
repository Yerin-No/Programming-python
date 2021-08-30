#3/26
'''주민등록번호 앞 6자리를 변수 id_number에 넣고.
출생년도 끝 두자기\n 출생 월일\n그 두개의 곱 출력
예시
id_number =020316일때
출력예시
02
0316
632
'''

id_number="040828"
print(id_number[0:2])
year=(id_number[:2])
print(year)
print(id_number[-6:-4])
print(id_number[:-4])

print(id_number[2:])
print(id_number[2:6])
month_day=id_number[-4:]
print(month_day)
print(id_number[-4:])

print(int(year)*int(month_day))
print('곱한결과: ' + str(int(year)*int(month_day)))
print('곱한결과: ', int(year)*int(month_day))
#print(year*month_day)

#f-string
name = "노예린"
age = 18

#%-formatting
print('안녕 나는 %s이야 내 나이는 %d살이야'%(name,age))

#str-format()
print('안녕 나는 {}이야. 내 나이는 {}살이야'.format(name,age))

#f-string
print(f'안녕 나는 {name}이야. 내 나이는 {age}살이야')

print(name * 10) #문자열+문자열,문자열*정수형

student_number = "2407"
print(student_number[1:2])
print(student_number[1])
print(student_number[-2:][1])#'03'[1]
print(int(student_number[-2:]))

# import random
# 반4=list(range(1,20))
# 반4.remove(3)
# print(반4)
# print(random.choice(반4))

#4/2
#휴대폰 번호를 입력할 때 - 있든, 없든 없이 출력하기
phone_number1='010-2540-5357'
phone_number2='010 7584 1367'
phone_number3='01073201685'

phone_number=phone_number1
result = phone_number1.replace('-','').replace(' ','')
print(result)
result = phone_number2.replace(' ','')
print(result)

#Quiz2-1. 학번을 student_number 변수에 넣고,
# 학급을 출력하고, 학과를 출력하기
#반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
# student_number =(input("학번: "))

student_number='2407'   #student_number[1:2]
number=student_number[1]
number=int(number)
majors = ['뉴소과','뉴웹과','뉴디과']
if 1 <= number <=6:
    print(f"{number}반{majors[(number-1)//2]}")
else:
    print("잘못 입력했습니다.")

# if number=='1':
#     print(f"{number}반 {majors[number]}")
# elif number=='2':
#     print(f"{number}반 {majors[number]}")
# elif number=='3':
#     print(f"{number}반 {majors[number]}")
# elif number=='4':
#     print(f"{number}반 {majors[number]}")
# elif number=='5':
#     print(f"{number}반 {majors[number]}")
# elif number == '6':
#     print(f"{number}반 {majors[number]}")
# else:
#     print("잘못입력했습니다.")

#Quiz2-2. 학번을 함수의 인수(argument)로 전달하여
# 호출하면 학년과 학과를 리턴하는 함수 만들기

def get_major(student_number):
    majors =['소','소','솔','솔','디','디']
    grade = student_number[0]
    classroom = student_number[1]
    classroom =int(student_number[1])
    return grade,majors[classroom-1]

grade, major = get_major("2407")
print(major, grade)

#Quiz2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고,
# 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기

# def average(*numbers):
#     count = 0
#     sum_value = 0
#     for number in numbers:
#         sum_value += number
#         count += 1
#     return  sum_value/count

def average(*numbers):
    return sum(numbers)/len(numbers)

print(average(10,20,30))
print(average(4,23))

#Quiz2-4. 키(cm)와 몸무게(kg)를 인수로 넣고,
#함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
# (소수 첫째자리까지 반올림)
#* BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
#18.5 미만: 저체중
# 18.5 이상 23 미만: 보통
# 23 이상 25 미만: 과체중
# 25 이상: 비만


def get_bmi(height, weight):
    height/=100
    bmi = weight/height**2
    return round(bmi,1)


bmi = get_bmi(176, 69)
print(bmi) #22.3

if 18.5>bmi:
    print("저체중")
elif bmi <23:       #elif 18.5<= bmi<23:
    print("보통")
elif bmi<25:        #elif 23<= bmi < 25:
    print("과체중")
else:
    print("비만")

#구구단 7단 출력하기
#i:1~9/1,2,3,4,5,6,7,8,9
for i in range(1, 10):
    print(f'7 x {i} = {7*i}')

#구구단 2~9단 출력하기
# for i in range(2, 10):
#     for j in range(1,10):
#         print(f'{i} x {j} = {i*j}')
#
for dan in range(2,9+1):    #2~9
    for i in range(1,9+1):  #x1~x9
        print(f'{dan} x {i} = {dan*i}')
    print()

#구구단 2~7단까지 출력for i in ra   nge(2, 10):
for dan in range(2,9+1):    #2~9
    for i in range(1,9+1):  #x1~x9
        print(f'{dan} x {i} = {dan*i}')
    print()
    if dan == 7:
        break
#구구단 2~7단까지 출력하되,1,3,5,7,9인것만 출력하기break,continue
for dan in range(2,9+1):    #2~9
    for i in range(1,9+1):  #x1~x9
        if i % 2 ==0:
            continue
        print(f'{dan} x {i} = {dan*i}')
    print()
    if dan == 7:
        break