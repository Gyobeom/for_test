import tkinter as tk
from tkinter import messagebox
#
# def popup():
#     messagebox.showinfo("클릭","버튼이 눌렸습니다.")
#     #messagebox.showwarning("경고", "버튼이 눌렸습니다.")
#     #messagebox.showerror("오류", "버튼이 눌렸습니다.")
#     #messagebox.askokcancel("버튼2개","버튼이 눌렸습니다")
#     #messagebox.askyesnocancel("버튼3개","버튼이 눌렸습니다.")
#

# w = tk.Tk()
# w.title('세 번째 GUI 프로그램')
#
# #이미지 준비
# p1 = tk.PhotoImage(file='michael.PNG')
# p2 = tk.PhotoImage(file='franklin.PNG')
# p3 = tk.PhotoImage(file='trevor.PNG')
#
# #레이블 및 버튼에 사용할 이미지 바인딩
# lbl_disp1 = tk.Label(w,image=p1)
# lbl_disp2 = tk.Label(w,image=p2)
# lbl_disp3 = tk.Button(w,image=p3,command=popup)
#
# #위젯배치
# lbl_disp1.pack(side='left')
# lbl_disp2.pack(side='left')
# lbl_disp3.pack()
#
# w.mainloop()

def popup():
    #xxlbl_display.configure(text=f'{type(checked.get())}')
    #if checked.get() == 0:
    if checked.get() == False: #체크버튼 체크 됐는지 확인 코드
        lbl_display.configure(text='체크버튼 OFF')
        messagebox.showinfo("언체크됨",'체크버튼 OFF')  #메세지 박스 출력
    #elif checked.get() == 1:
    elif checked.get() == True:
        lbl_display.configure(text='체크버튼 ON')
        messagebox.showinfo("체크됨",'체크버튼 ON')
    else:
        messagebox.showerror("오류", '실행될 일 없음')


w = tk.Tk()
w.title('체크버튼 실습')
w.geometry('300x100')
#checked = tk.IntVar()# 정수형 객체 변수 지정 , DoubleVar, StrVar, BooleanVar
checked = tk.BooleanVar()


cb_on_off = tk.Checkbutton(w,text='출석체크',variable=checked,command=popup)
lbl_display = tk.Label(w,text='')

cb_on_off.pack()
lbl_display.pack()


w.mainloop()