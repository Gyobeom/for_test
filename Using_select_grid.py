import tkinter as tk
from tkinter import messagebox

def popup():
    if selected.get() == 0:
        lbl_display.configure(image=p1) #lbl labal 이미지 변경
    elif selected.get() == 1:
        lbl_display.configure(image=p2)
    else:
        lbl_display.configure(image=p3)



w = tk.Tk()
w.title('세 번째 GUI 프로그램')

p1 = tk.PhotoImage(file='michael.PNG')
p2 = tk.PhotoImage(file='franklin.PNG')
p3 = tk.PhotoImage(file='trevor.PNG')

selected = tk.IntVar()
rb_m = tk.Radiobutton(w,text='마이클',command=popup,variable=selected,value=0) #check 버튼은 variable이 동일함.
rb_f = tk.Radiobutton(w,text='프랭클린',command=popup,variable=selected,value=1)#select는 값이다름
rb_t = tk.Radiobutton(w,text='트레버',command=popup,variable=selected,value=2)
lbl_display = tk.Label(w,text='플레이어 선택?')
lbl_display.configure(image=p1)

#위젯 배치
rb_m.grid(row=0,column=0)  #[0:0]
rb_f.grid(row=0,column=1) #[0:1]
rb_t.grid(row=0,column=2) #[0:2]
lbl_display.grid(row=1,column=0,columnspan=3) #3행 합치기

w.mainloop()

