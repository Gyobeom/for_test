# 변수생성(자료형 자동배정)
# a = '안녕하세요'
# b = 1
# c = 3

# 리스트 생성
# a = []
# b = [1,2,3]
# c = ['life','is','too','short']

# 리스트 인덱싱
# a[0] = a 리스트 첫번째
# a[-1]= 리스트 마지막 값

# 리스트 슬라이싱
# a = [1,2,3,4,5]
# a[0:2] -> 1, 2 -> 마지막 전 리스트까지 포함
# a[:2] == [0:2]
# a[2:] -> 3 , 4, 5  2부터 끝까지

# 리스트 삭제
# del a[1] 1번 배열 리스트 값 삭제

# 리스트 요소추가
# a.append([5,6])
# a -> [1,3,4,[5,6]]

# 리스트 위치반환
# a = [1,2,3]
# a.index(3) -> 2 (3번 값이 들어있는 2번 배열을 돌려줌)

# 튜플 추가생성, 삭제 , 수정 불가능
# t1 = (1,2,'a','b')

# 딕셔너리 생성 key 값 name,phone을 통해 value 값 가져옴
# dic = {'name' : 'pey', 'phone':'01000000000'}
# print( dic['name']) -> pey

# print("I like", end= " ") end = " " 줄바꿈 되지 않고 띄어쓰기됨.
# print("monkey")

# 반복문 for, while
# while num <= 100:
# for x in family:      family = ['mother','farther','gentleman']
# for i in range(8):     8번반복 0 ~ 7  range 마지막 숫자 포함 x
# for i in range(1,8):   7번반복 1 ~ 8  1번부터 7번까지 반복
# items = ['dd','ss','cc','ff']
# for item in items 배열 값으로 돌게 할 수 있음 item에는 items배열값이 들어감.

# format 함수
# print('구구단 {0} x {1} = {2}'.format(a, b, a*b)) .format(대괄호 순서로 변수 대입)


# f-string
# day = '06일'
# printf(f'오늘 며칠이지?{day}')
# 문자열내 대괄호 이용해서 변수 출력

# split() 함수
# a = ['aa.bb.cc.df.f.gg]
# a.split('.')  a -> ['aa','bb','cc','dd]


# strip() 공백제거 , 특정 문자열 제거 strip("v"), strip("\n") 줄바꿈 제거


# 모듈 가져오기
# import tkinter  / from tkinter import *(이름)
# import random ...
# random.randrange(1,7) 1 이상 7미만 랜덤 함수 . 
# random.choic(abc)  abc = [1,3,4,5] abc 리스트 중에서 하나 랜덤 뽑기

# 조건문
# if a > b:
# if ,elif, else

# 윈도우 객체 생성 tkinter
# from tkinter import *
# w = Tk() 객체 생성
# w.title('레이블생성)


# 파일 입출력
# file_IO 파일 확인

# try exception 에러 표시 구문
#  try:                      try 구문 내 동작 수행시 발생하는 에러들을 except에서 적용
#     c = list()
#     c.append('사과')
#     a = int(input())
#     b = int(input())
#     print(a/b)
#     print(c[1])
# except ZeroDivisionError:   ZerpDivisionError가 올경우 해당 print문 출력
#     print('분모에 0이 올 수 없습니다.')
#except ValueError:
#    print('입력된 수는 정수가 아닙니다.')
# except IndexError:
#     print('리스트의 범위를 벗어난 인덱스가 사용되었습니다.')
# except:
#     print('무언가 에러가 발생했습니다.')
# finally:                                     예외 발생여부와 상관없이 실행.
#    print('예외 발생여부 상관없이 항상 실행')
# except Exception as e:  에러코드를 e로 가명을 붙이고 출력할 때 어떤 에러인지 출력.
#     print('무언가 에러가 발생했습니다. :{0}'.format(e))

# TKinter 위젯
# Button	단순한 버튼
# Label	텍스트 혹은 이미지 표시
# CheckButton	체크박스
# Entry	단순한 한 라인 텍스트 박스
# ListBox	리스트 박스
# RadioButton	옵션 버튼
# Message	Label과 비슷하게 텍스트 표시. Label과 달리 자동 래핑 기능이 있다.
# Scale	슬라이스 바
# Scrollbar	스크롤 바
# Text	멀티 라인 텍스트 박스로서 일부 Rich Text 기능 제공
# Menu	메뉴 Pane
# Menubutton	메뉴 버튼
# Toplevel	새 윈도우를 생성할 때 사용. Tk()는 윈도우를 자동으로 생성하지만 추가로 새 윈도우 혹은 다이얼로그를 만들 경우 Toplevel를 사용한다
# Frame	컨테이너 위젯. 다른 위젯들을 그룹화할 때 사용
# Canvas	그래프와 점들로 그림을 그릴 수 있으며, 커스텀 위젯을 만드는데 사용될 수도 있다




# 라벨생성
# lbl_1 = Label(w,text="파이썬을") w객체에 생성되는 레이블이라는 의미
# lbl_1.pack() pack은 객체에서 해당 라벨 보이게만듬.

# 문자열 작음 따옴표 입력한다면
# food = "Python 's favorite food is perl"  큰 따움표로 감싸기 반대로 큰따움표 사용하려면 작은 따옴표로 감싸기

# 입력
# a = input("~~~~~~~~~~")




