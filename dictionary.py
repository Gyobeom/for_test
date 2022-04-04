#dictionary

#리스트와 비슷하나 순서를 따지지 않음
#키와 값이 pair가 원소가 된다

fruits = {'apple':'사과','watermelon':'수박'}
print(fruits['watermelon'])
fruits['kiwi'] = '키위' #삽입
print(fruits)

empty ={}
print(type(fruits), type(empty))

test = [['python',3],['english',2],['dance',1]]
print(test[1][0])
print(dict(test)) #dict함수 리스트에서 딕셔너리로 변환 시켜줌

test1 = ['ab','cd','ef']
print(test1[1][0])
print(dict(test1)) #리스트에서 붙어있는 문자열 2개까지만 딕셔너리 변환가능하고 , 변환시 a : b 이런식으로 변환

test2 = ['ab','cd','ef']
print(test2[1][0])
print(dict(test2)) #dict함수 리스트에서 딕셔너리로 변환 시켜줌


#update()
fruits = {'apple':'사과','watermelon':'수박'}
others = {'strawberry':'딸기','kiwi':'딸기'} #others 딕셔너리를 fruits에 결합하는 update 함수
fruits.update(others)
print(fruits)

#del
del fruits['apple'] #apple 키워드를 딕셔너리에서 삭제하는 del 키워드 apple 딕셔너리가 삭제됨
print(fruits)

#clear함수
# fruits.clear() #딕셔너리는 유지되며 들어있던 원소만 전체 삭제
# print(fruits)

#keys() 딕셔너리 키값을 출력 하는 함수
# print(fruits.keys())

# #items() 딕셔너리에 키, 벨류 값을 출력하는 함수
# print(fruits.items())

#for문으로 딕셔너리 key 값 출력하기
for k in fruits.keys():
    print(k)

#for문에서 items를 이용하여 key값과 value값을 출력
for k, v in fruits.items():
    print(k)
    print(v)

#음식 추천 프로그램 v0.1

# alcohol_foods = {'맥주': '치킨',
#                  '와인': '치즈',
#                  '고량주': '짬뽕',
#                  '소주': '골뱅이소면'}
# alcohol = input('주문하실 술(맥주/와인/소주/고량주)은?')
#
# if alcohol in alcohol_foods.keys():
#     print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))


#음식 추천 프로그램 v0.15

# alcohol_foods = {'맥주': '치킨',
#                  '와인': '치즈',
#                  '고량주': '짬뽕',
#                  '소주': '골뱅이소면'}
#
# while True:
#     alcohol = input('주문하실 술(맥주/와인/소주/고량주/결제)은?')
#     if alcohol == '결제':
#         break
#     if alcohol in alcohol_foods.keys():
#         print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))
#     else:
#         print('{0}는 판매하지 않습니다.메뉴에서 골라주세요'.format(alcohol))

#음식 추천 프로그램 v0.3
# import random
#
# alcohol_foods = {'맥주': '치킨',
#                  '와인': '치즈',
#                  '고량주': '짬뽕',
#                  '소주': '골뱅이소면'}
#
#
# while True:
#     alcohol = input('주문하실 술(맥주/와인/소주/고량주/아무거나/결제)은?')
#     if alcohol == '결제':
#         break
#     if alcohol in alcohol_foods.keys():
#         print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))
#     elif alcohol == '아무거나':
#         alcohol = str(random.choice(list(alcohol_foods)))
#         print('{0}에 어울리는 안주는 {1}입니다.'.format(alcohol, alcohol_foods[alcohol]))
#     else:
#         print('{0}는 판매하지 않습니다.메뉴에서 골라주세요'.format(alcohol))


alcohol_foods = {'맥주': '치킨',
                 '와인': '치즈',
                 '고량주': '짬뽕',
                 '소주': '골뱅이소면'}

#copy()이용시 같은 주소를 이용하지 않아 원본이 수정되지 않음
#copy_alcohol = alcohol_foods

copy_alcohol = alcohol_foods.copy()
copy_alcohol['소주'] = '두부김치'
print(copy_alcohol)

#tuple
#immutable 불변 튜플은 생성 후 값을 추가,수정등을 할 수 없음 상수의 리스트

empty = () #튜플 소괄호 문법
numbers = (1, -9, 7)
print(type(empty))
print(numbers[1])

subjects = ('python','c++','english') #packing 패킹 개수와 언패킹할 개수가 똑같아야함
# for subject in subjects:
#     print(subject)

kim,han,tom = subjects #unpacking 각각 kim,han,tom에 튜플 값이 들어감
print(kim,han,tom)


#패킹 언패킹
a = input()
b = input()

a, b = (b, a)#packing과 unpacking을 동시에 수행
print(a,b)

