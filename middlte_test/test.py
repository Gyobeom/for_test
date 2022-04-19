import tkinter as tk
from tkinter import ttk


def save():
    name = n_input.get()
    phone_num = p_input.get()
    if selected.get() == 0:
        echecked = "남자"
    else:
        echecked = "여자"

    fp = open('test.txt', 'w',encoding="UTF-8")
    fp.write(f'{name},{phone_num},{echecked}')
    fp.close()



w = tk.Tk()
w.title('201644056_테스트')
#w.geometry("500x500")

w.bind('<Return>',save)
selected = tk.IntVar()

lbl_name = tk.Label(w,text="이름 : ")
n_input =tk.Entry(w)
s_button = ttk.Button(w,text="저장",command=save)
lbl_name1 = tk.Label(w,text="전화번호 :")
p_input =tk.Entry(w)
lbl_name2 = tk.Label(w,text="주소 :")
a_input =tk.Entry(w)
sex_label = tk.Label(w,text="성별 ")
sex = tk.Radiobutton(w,text='남',variable=selected,value=0)
sex_1 = tk.Radiobutton(w,text='여',variable=selected,value=1)

lbl_name.grid(row=0,column=0,sticky=tk.W)
n_input.grid(row=0,column=1)
lbl_name1.grid(row=1,column=0,sticky=tk.W)
p_input.grid(row=1,column=1)
lbl_name2.grid(row=2,column=0,sticky=tk.W)
sex_label.grid(row=3,column=0,sticky=tk.W)
a_input.grid(row=2,column=1,sticky=tk.W)

sex_1.grid(row=3,column=1)
sex.grid(row=3,column=1,sticky=tk.W)

s_button.grid(row=4,column=1,sticky=tk.E)

w.mainloop()