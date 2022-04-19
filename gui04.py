import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def click_photo(ev):
    messagebox.showinfo('좌표', f'({ev.x}, {ev.y})')

def click_next():
    global idx
    idx = idx + 1
    if idx > len(photos)-1:
        idx = 0
    p.configure(file=photos[idx])
    lbl_page.configure(text=f'{idx+1}/{len(photos)}')
    #p = tk.PhotoImage(file=photos[idx])
    #lbl_photo.configure(image=p)
    #lbl_photo.image = p
def click_prev():
    global idx
    idx = idx - 1
    if idx < 0:
        idx = len(photos)-1
    p.configure(file=photos[idx])
    lbl_page.configure(text=f'{idx + 1}/{len(photos)}')

def pg_dw(ev):
    click_next()

def pg_up(ev):
    click_prev()

# 전역변수
photos = ['michael.PNG', 'franklin.PNG', 'trevor.PNG']
idx = 0

w = tk.Tk()
w.title('포토뷰어 v0.2')
w.geometry('500x500')

w.bind('<Next>', pg_dw)
w.bind('<Prior>', pg_up)

p = tk.PhotoImage(file=photos[0])
lbl_photo = ttk.Label(w,image=p)
lbl_page = ttk.Label(w,text=f'{idx+1}/{len(photos)}')
btn_next = ttk.Button(w, text="다음====>", command=click_next)
btn_prev = ttk.Button(w, text="<====이전", command=click_prev)

lbl_photo.bind('<Button>', click_photo)

lbl_photo.grid(row=0, column=0, columnspan=3)
btn_prev.grid(row=1, column=0, sticky=tk.EW)
btn_next.grid(row=1, column=2, sticky=tk.EW)
lbl_page.grid(row=1, column=1)

w.mainloop()


# import tkinter as tk
# from tkinter import messagebox
#
# def popup():
#     if selected.get() == 0:
#         lbl_display.configure(image=p1)
#     elif selected.get() == 1:
#         lbl_display.configure(image=p2)
#     else:
#         lbl_display.configure(image=p3)
#
# w = tk.Tk()
# w.title('라디오버튼 실습')
# w.geometry('500x500')
#
# p1 = tk.PhotoImage(file='michael.PNG')
# p2 = tk.PhotoImage(file='franklin.PNG')
# p3 = tk.PhotoImage(file='trevor.PNG')
#
# selected = tk.IntVar()
# rb_m = tk.Radiobutton(w, text='마이클', command=popup, variable=selected, value=0)
# rb_f = tk.Radiobutton(w, text='프랭클린', command=popup, variable=selected, value=1)
# rb_t = tk.Radiobutton(w, text='트레버', command=popup, variable=selected, value=2)
# lbl_display = tk.Label(w,text='플레이어 선택?')
# lbl_display.configure(image=p1)
# # 위젯 배치
# rb_m.grid(row=0, column=0)
# rb_f.grid(row=0, column=1)
# rb_t.grid(row=0, column=2)
# lbl_display.grid(row=1, column=0, columnspan=3)
# w.mainloop()
