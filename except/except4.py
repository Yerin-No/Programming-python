list1 = [1, 2, 3]
try:
    print(list1[0])
    print(list1[1])
    print(list1[2])
    print(list1[3])
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)    #list index out of range
except:
    print('error')
else:   #예외가 발생하지 않았을 때 실행하는 코드
    print('It is work well')
finally:
    print('finally')