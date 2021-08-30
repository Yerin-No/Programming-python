#Quiz)3-1
#주민등록번호 앞 6자리를 변수 id_number에 넣고,
#출생년도 끝 두자리\n출생 월일\n그 두개의 합 출력
# id_number = "040828"
# print("출생년도 끝 두자리: "+id_number[0:2])
# print("출생 월일: "+id_number[2:7])
# print("두개의 합: "+id_number[0:2]+id_number[2:7])
#
# #Quiz)3-2
# phone_number="02-2232-6963"
# print("지역번호: "+phone_number[0:phone_number.find("-")])
# print("맨 끝 네 자리 : "+phone_number[8:])

#Quiz2-1. 학번을 student_number 변수에 넣고,
# 학급을 출력하고, 학과를 출력하기
#반이 0 미만이거나 7 이상이면 "잘못 입력했습니다." 출력하기
# student_number =(input("학번: "))
# student_number="2407"
# d = int(student_number[1])
# if d==1 or d==2:
# 	print(f"{student_number[1]}반 뉴미디어소프트웨어과")
# elif d==3 or d==4:
# 	print(f"{student_number[1]}반 뉴미디어웹솔루션과")
# elif d==5 or d==6:
# 	print(f"{student_number[1]}반 디자인과")
# elif d>=0 and d>7:
# 	print("잘못입력했습니다.")
#
# #Quiz2-2. 학번을 함수의 인수(argument)로 전달하여
# # 호출하면 학년과 학과를 리턴하는 함수 만들기
# def get_major(grade):
# 	d = int(student_number[1])
# 	if d == 1 or d == 2:
# 		return student_number[0], "뉴미디어소프트과"
# 	elif d == 3 or d == 4:
# 		return student_number[0], "뉴미디어솔루션과"
# 	elif d == 5 or d == 6:
# 		return student_number[0], "뉴미디어디자인과"
# 	elif d >= 0 and d > 7:
# 		return student_number[0], "잘못"
#
# grade, major = get_major("2407")
# print(major, grade)
#
#
# #Quiz2-3. 인수의 개수에 상관없이 인수로 숫자를 여러개 넣고,
# # 함수를 호출하면 그 인수들의 평균을 구하여 리턴하는 함수 만들기
# def average(*number):
# 	sum = 0
# 	for i in number:
# 		sum += i
# 	return sum / len(number)
#
# print(average(10, 20, 30)) #20.0
# print("평균값 : {}".format(average(list)))

#Quiz2-4. 키(cm)와 몸무게(kg)를 인수로 넣고,
#함수를 호출하여 BMI 지수를 리턴하는 함수 만들기
# (소수 첫째자리까지 반올림)
#* BMI 지수 계산법: 체중(kg) ÷ 키의 제곱(m²)
#18.5 미만: 저체중
# 18.5 이상 23 미만: 보통
# 23 이상 25 미만: 과체중
# 25 이상: 비만
# def get_bmi(height,weight):
#     height=height*0.01
#
#     return round(weight/(height*height))
#
# bmi = get_bmi(176, 69)
# print(bmi) #22.3

'''
Quiz3-1. n_sum() 함수를 만든다. 함수의 인수(argument)로 
10자리 숫자보다 작은 숫자를 넣으면, 각 자리의 숫자의 합계를 리턴한다. 
10자리 이상이면 -1 리턴한다.
'''

# def n_sum(number):
# 	number = str(number)	#number='408'
# 	result = 0
# 	for i in number:	# i -> '4'
# 		if number[:]>number[:9]:	#number[:]='1000000000' number[:9]='100000000'
# 			result=(-1)
# 			break
# 		else:
# 			result = result + int(i)
# 	return result
#
# result = n_sum(10)
# print(result)        #1
# result = n_sum(331)
# print(result)         #7
# result = n_sum(408)
# print(result)         #12
# result = n_sum(1000000000)
# print(result)         #-1

'''
Quiz3-2. get_subway_fare() 함수를 만든다. 이 함수는 인수로 가는 거리(km)를 숫자로 넣으면, 요금을 리턴한다.
* 지하철 요금계산법 10km 이내: 720원(청소년), 10~50km: 5km마다 100원, 50km 초과 시 8km마다 100원
'''

# def get_subway_fare(km):
# 	fare=0
# 	if km<10:
# 		fare=(720)
# 	elif 10<km<50:
# 		fare=(720+(int(km-10)//5*100))
# 	else:
# 		fare=(720+(int(km)//8*100))
# 	return fare
# fare = get_subway_fare(5)
# print(fare)        #720
# fare = get_subway_fare(26)
# print(fare)        #1120
# fare = get_subway_fare(61)
# print(fare)        #1720

'''
Quiz3-3. get_three_six_nine() 함수를 만든다. 이 함수에 숫자를 입력하면 369 게임에  해당하는 답변을 리턴한다.
* 369게임: 숫자의 어느 자리든 3 또는 6 또는 9가 있다면 그 갯수만큼 '짝'을 외치고, 아니면 그냥 숫자를 외친다.
힌트: 문자열 함수 중에 특정 글자를 세는 함수가 있음
'''

# def get_three_six_nine(number):
# 	str_i = str(number)
# 	count_369 = 0
# 	for i in str_i:
# 		if (i == '3') or (i == '6') or (i == '9'):
# 			count_369 += 1
# 	if count_369 == 0:
# 		result=(i)
# 	else:
# 		result=(count_369 * '짝')
# 	return result
#
#
# result = get_three_six_nine(1)
# print(result)        #1
# result = get_three_six_nine(3)
# print(result)        #짝
# result = get_three_six_nine(16)
# print(result)        #짝
# result = get_three_six_nine(36)
# print(result)        #짝짝

'''
Quiz3-4. 나만의 재미난 문제를 만들어보세요. 단, 조건이 있습니다.
1. 함수의 이름을 정해준다.
2. 인수로 넣어야하는 자료형이나 개수를 말해준다.
3. 리턴하는 것을 말해준다.
4. 출력 예시를 보여준다.
5. 내가 낸 문제의 답안을 제출한다.
'''

# def seconds(second):
# 	hours=second//3600
# 	second=second-hours*3600
# 	min=second//60
# 	sec=second-min*60
# 	result=(hours,'시간',min,'분',sec,'초')
# 	return result
#
# result=seconds(10000)
# print(result)
# seconds(36100)

'''
Quiz4-1. [학생퀴즈] 소수판별하기(소수: 1이나 자기자신으로만 나누어 떨어지는 수)
is_prime() 함수를 만든다.
인수로 1개의 숫자를 받는다.
인수로 넘어온 숫자가 소수(prime number)이면 "소수" 아니면, "소수 아님" 리턴한다.
'''
def is_prime(number):
	if number < 2:
		return "소수아님"
	for i in range(2, number):
		if number % i == 0:
			return "소수아님"
	return "소수"

result = is_prime(2)
print(result)     #소수
result = is_prime(13)
print(result)     #소수
result = is_prime(36)
print(result)     #소수 아님

'''
Quiz4-2. [학생퀴즈] get_compliment() 함수를 만든다. 이 함수에 '고구마' 또는 '맛있는'이 들어가는 말을 입력하면 그에 해당하는 답변을 리턴한다.
'고구마'가 들어가는 말을 입력하면 '왓쇼이!', '맛있는'이 들어가는 말을 입력하면 '우마이!',
'놀랄 만한', '황당한', '굉장한'이 들어가는 말을 입력하면 '요모야..!', 특정 단어가 하나라도 들어가지 않는다면 '으무!'를 리턴한다. 
'''

# def get_compliment(taste):
#
# 	if taste == "고구마":
# 		return "왓쇼이!"
# 	elif taste == "맛있는":
# 		return "우마이!"
# 	elif taste == "놀랄 만한" or "황당한" or "굉장한":
# 		return "요모야!"
# 	else:
# 		return "으무!"
#
# result = get_compliment('고구마 된장국')
# print(result) # 왓쇼이!
# result = get_compliment('맛있는 크레이프')
# print(result) # 우마이!
# result = get_compliment('놀랄 만한 상황')
# print(result) # 요모야..!
# result = get_compliment('좋은 마음가짐이다!')
# print(result) # 으무!

'''
0820 Quiz5-1 모듈이란?
쉽게 사용할수 있도록 따로 만들어진 파일

Quiz5-2. 패키지란?
모듈을 효율적으로 관리하기위해 나눠 놓은 것

Quiz5-3. theater_module.py 모듈(파일)의 price 함수를 p학번 라는 이름으로 호출 하도록 import문을 작성하세요
import theater_module

Quiz5-4. __all__의 역할은?
모듈 목록을 가지고 있는 것

Quiz5-5. 지금 파이썬 파일을 직접실행할 때만 실행되고, 다른 모듈에서 import할 때는 실행되지 않도록 하는 제어문은?
inspect(?)

Quiz5-6. travel 패키지(폴더) 안에 vietnam.py 모듈(파일) 안의 ThailandPackage 클래스를 생성하고 detail 함수를 호출하는 < 가 >, < 나 >, < 다 > 에 들어갈 각 방법은?
import travel.vietnam
< 가 >
trip_to = vietnam.VietnamPackage()
trip_to.detail()

from travel import vietnam
< 나 >
trip_to = vietnam.VietnamPackage()
trip_to.detail()

from travel.vietnam import ThailandPackage
< 다 >
trip_to = vietnam.VietnamPackage()
trip_to.detail()
'''



