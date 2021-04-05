'''파이썬 300제 51~70리스트'''
movie_rank = ["닥터 스트레인지","스플릿","럭키"]
movie_rank.append("배트맨")
print(movie_rank)
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)
del movie_rank[3]
print(movie_rank)

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Pyyhon", "Go", "C#"] 
print(lang1 + lang2)

nums = [1,2,3,4,5,6,7]
max : 7
min : 1
print(max(nums))
print(min(nums))

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))
nums = [1,2,3,4,5]
avg = sum(nums) / len(nums)
print(avg)

# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:]) # 슬라이싱

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2]) # 슬라이싱 홀수
print(nums[1::2]) # 슬라이싱 짝수
print(nums[::-1]) # 슬라이싱 역방향

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest[0],interest[2])  # join 메서드
print(" ".join(interest))
print("/".join(interest))
print("\n".join(interest)) #줄바꿈

string = "삼성전자/ LG전자/Naver"
splt_mthd = string.split("/")
print(splt_mthd) # 문자열 스플릿 메서드

data = [2,4,3,1,5,10,9]
data.sort() # 리스트값 오름차순 정렬
print(data)
'''
모듈 불러오기1
'''

# import mod1

# print(mod1.add(1,2))
# print(mod1.sub(1,2))
'''
모듈 불러오기2
'''

# from mod1 import add, sub

# print(add(3,4))
# print(sub(10,4))

'''
모듈 불러오기3
from 모듈명 import *
'''
# from mod1 import * # 모듈명 입력 필요x
# print(add(5,6))
# print(sub(5,6))

# import mod1

# import mod2
# print(mod2.PI) # 변수접근
# a = mod2.Math() # 클래스 객체 생성
# print(a.solv(2))    #메서드 사용
# print(mod2.add(mod2.PI, 4.4))  # 함수 사용

# 예외 처리
# f = open("나없는파일", 'r') # FileNotFoundError
# print(4/0) ZeroDivisionError

try:    # try, except문
    print(4/0)
    print('hello python')
except:
    print('0으로 못 나눕니다')
finally : # 오류여부 상관없이 수행되는 내용
    print('프로그램 종료')

try:
    # f = open('없는파일'.txt)
    a = [1,2]
    # print(a[3])
    # 4/0
except ZeroDivisionError as e:  # e : 오류 내용을 담은 변수
    print("0으로 나눌 수 없습니다", e)
except IndexError as e:
    print("인덱싱 할 수 없습니다.", e)
except Exception as e:
    print('기타 오류 발생', e)
else:
    print('오류가 없네요.')

print('='*80)
try:
    4/0
except ZeroDivisionError as e:
    pass    # 오류 무시

print('='*80)
# raise Exception('오류 일부러 발생시키기')

class MyError(Exception):
    def __str__(self):  #매직 메서드 오류 발생시 내용물 리턴
        return '허용되지 않은 별명입니다.'

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
try:
    say_nick('천사')
    say_nick('바보')

except MyError as e:
    print(e)

print('프로그램 정상 종료')

#내장함수
# print(dir([1,2,3]))
# print()
# print(dir('abc'))
# 유용한 이누머레이트
for i, name in enumerate(['body','foo','bar']):
    print(i, name)

for i, name in enumerate(['body','foo','bar'],1):
    print(i, name)


# print(divmod(7 % 3))

print(eval('1+2'))

#positive.py 
def positive(l): 
    result = [] 
    for i in l: 
        if i > 0: 
            result.append(i) 
    return result

print(positive([1,-3,2,0,-5,6]))

def positive2(x):
    return x > 0

print(list(filter(positive2, [1,-3,2,0,-5,6]))) #filter(함수명, 데이터값)
print(filter(positive2, [1,-3,2,0,-5,6])) #<filter object at 0x00000209BCA24D00>
print('='*80)

print(list("python"))
print(list((1,2,3)))
print(list(range(10)))
print(range(10))
# print(list(123)) # 숫자형은 반복 가능하지 않음 *not iterable

print('='*80)

def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

def two_times2(x):
    return x*2

print(map(two_times2, [1,2,3,4]))

# print(sum([6546,374941654564321646311683214,265467894613216844131331]))

print(list(zip([1, 2, 3], [4, 5, 6])))
print(tuple(zip([1, 2, 3], [4, 5, 6])))
print(dict(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(tuple(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
# print(dict(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))

print( list(range(5)))  # range
print( list(range(5,10)))
print( list(range(1,10,2)))
print( list(range(0,-10,-1)))

# round(number[, ndigits]) 함수는 숫자를 입력받아 반올림해 주는 함수이다.
print(round(4.6))
print(round(5.678, 2)) # round 함수의 두 번째 매개변수는 반올림하여 표시하고 싶은 소수점의 자릿수(ndigits)이다.

# sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수이다.
print( sorted([3, 1, 2]))
print(['a', 'b', 'c'])
print(sorted("zero"))
print(sorted((3, 2, 1)))

#tuple(iterable)은 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수이다. 
# 만약 튜플이 입력으로 들어오면 그대로 돌려준다.
print(tuple("abc"))
print(tuple([1, 2, 3]))
print(tuple((1, 2, 3)))

# type(object)은 입력값의 자료형이 무엇인지 알려 주는 함수이다.
print(type("abc"))
print(type([ ]))
print(type(open("test", 'w')))