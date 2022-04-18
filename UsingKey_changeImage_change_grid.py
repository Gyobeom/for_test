import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def click_photo(ev):
    messagebox.showinfo('좌표',f'({ev.x}, {ev.y})')



def click_next():

    global idx  #현재 몇번째 파일 인지 확인하기 위하여 전역변수로 사용.
    idx = idx + 1
    if idx > len(photos)-1:
        idx = 0
    p.configure(file=photos[idx])
    lbl_page.configure(text=f'{idx+1}/{len(photos)}')

def click_prev():
    global idx
    idx = idx - 1
    if idx < 0:
        idx = len(photos)-1
    p.configure(file=photos[idx])
    lbl_page.configure(text=f'{idx + 1}/{len(photos)}')

def pg_dw(ev): #down키 클릭시 사용되는 함수.
    click_next()
def pg_up(ev): #Up키 클릭시 사용되는 함수.
    click_prev()

#전역 변수
photos = ['michael.PNG','franklin.PNG','trevor.PNG']  #사진을 가지고 있는 배열값.
idx = 0

w = tk.Tk()
w.title('포토뷰어 v0.2')
#w.geometry('500x500')


w.bind('<Next>', pg_up)
w.bind('<Prior>',pg_dw)



p = tk.PhotoImage(file = photos[0])
lbl_photo = tk.Label(w,image=p)
lbl_page = tk.Label(w,text=f'{idx+1}/{len(photos)}')
btn_next = tk.Button(w,text='다음======>',command=click_next)
btn_prev = tk.Button(w,text='<======이전',command=click_prev)


lbl_photo.bind('<Button-1>',click_photo)


lbl_photo.grid(row=0 ,column=0,columnspan=3)
lbl_page.grid(row=1,column=1,sticky=tk.EW)
btn_prev.grid(row=1,column=0,sticky=tk.EW)#EW match_parent
btn_next.grid(row=1,column=2,sticky=tk.EW)

#위젯 배치


w.mainloop()