import tkinter as tk
import random
"""201644056 이교범"""

student_list = ['이준용','황태결','한승민','김주연','임진수','김광래','고대현','강성모','전유진','조민호','김현호','김준영','이교범','간명해','송민섭']


def numplus():
    try:
        first_num = int(f_input.get())
        second_num = int(s_input.get())
        result = first_num + second_num
        result_lbl.configure(text=f'{result}')
    except ValueError as e:
        result_lbl.configure(text=f'{e}\n은 숫자가 아닙니다.')

def numdevide():
    try:
        first_num = int(f_input.get())
        second_num = int(s_input.get())
        result = first_num / second_num
        result_lbl.configure(text=f'{result}')
    except ZeroDivisionError as e:
        result_lbl.configure(text=f'분모의 0이 올 수 없습니다.\n {e}')

def rand_cal():
    try:
        first_num = random.randrange(0,10)
        second_num = random.randrange(0,10)
        plus_result = first_num + second_num
        devide_result = first_num / second_num
        result_lbl.configure(text=f'첫 번째 수:{first_num}, 두 번째 수: {second_num} \n 더하기결과: {plus_result},나누기 결과:{devide_result}')
    except ZeroDivisionError as e:
        result_lbl.configure(text=f'분모의 0이 올 수 없습니다.\n {e}')

    except ValueError as e:
        result_lbl.configure(text=f'{e}\n은 숫자가 아닙니다.')

def rand_people():
    fp = open('quiz.txt','w',encoding="UTF-8")
    for list in student_list:
        rand_num = random.randrange(0,101)
        fp.write(f'{rand_num},{list}\n')
    fp.close()
    result_lbl.configure(text="quiz.txt파일로 저장했습니다.")




w = tk.Tk()
w.title("lgb_201644056.py")
w.geometry('600x200')

f_input = tk.Entry(w)
s_input = tk.Entry(w)
add_button = tk.Button(w,text="더하기", command=numplus)
devide_button = tk.Button(w,text="나누기",command=numdevide)
random_button = tk.Button(w,text="랜덤번호(각각 0~9 사이의수)",command=rand_cal)
name_random_button = tk.Button(w,text="성명,랜덤번호",command=rand_people)
result_lbl = tk.Label(w,text="결과 확인")



f_input.pack(fill='x')
s_input.pack(fill='x')
add_button.pack(fill='x')
devide_button.pack(fill='x')
random_button.pack(fill='x')
name_random_button.pack(fill='x')
result_lbl.pack(fill='x')


w.mainloop()