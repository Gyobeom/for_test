#함수 return 이용시 아무런 값도 리턴하지 않는경우 NONE으로 전달됨
# def test(name):
#     print('hi' + name)
#     return
#
# print(test('brian'))


# def minus(a, b):
#     """두 수의 차를 구하는 함수"""
#     return a - b
#
# print(minus(5,3))
#
# help(minus)#함수 내용 확인 가능

#가변 매개변수 #*values <- 하나밖에 사용을 못하고 , 가변매개변수 뒤에 일반 매개변수 못옴
# def print_even(times, *values):
#     for value in values:
#         print(times * value)
#
# print_even(2, -9, 11, 7, 100, 6)

#기본 매개변수 times =3  기본매개변수 뒤에 일반 매개변수 올 수 없음

#재귀 함수
# def factorial_recursion(n):
#     """
#     팩토리얼 by 재귀
#     f(3)= 3 * f(2)
#         = 3 * 2 * f(1)
#         = 3 * 2 * 1 * f(0)
#         = 3 * 2 * 1 * 1
#     """
#     if n == 0:
#         return 1
#     else:
#         return n * factorial_recursion(n-1)
#
# print(factorial_recursion(6))

#
# def factorial_loop(n):
#     """
#     팩토리얼 함수 by 반복문
#     """
#     result = 1
#     for i in range(1,n+1):
#         result = result * i
#     return result
#
# print(factorial_loop(5))


#fibonacci
# def fibo_recursion(n):
#     """
#     f(1) = 1
#     f(2) = 1
#     f(n) = f(n-1) + f(n-2)
#     """
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     else:
#         return fibo_recursion(n - 1) + fibo_recursion(n - 2)
#
# for i in range(1, 7):
#     print('피보나치 {0} : {1}'.format(i,fibo_recursion(i)))


#함수의 매개변수로 함수 전달하기

# 함수 메모리 주소를 전달 함
# def print_hi(hi):
#     for i in range(5):
#         hi()
#
# def hi():
#     print('hello~')
#
# print_hi(hi)

#map(함수 , 순환가능한 자료구조)
#리스트, 딕셔너리 ,문자열, 범위 range

#def square(n):
#    return n * n

#def odd(n):
#    return n % 2 == 1

# result = []
# for k in range(1,6):
#     result.append(square(k))
# print(result)

#print(list(map(square,[1,2,3,4,5])))

#filter(함수,순환가능한 자료구조) ,true일 때만 작동

#print(list(filter(odd,[1,2,3,4,5])))

#람다함수 ,제너레이터

#module
#math, random

