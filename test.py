import tkinter as tk

def fc2():
    text = ''
    n = int(en_input.get())
    for i in range(n):
        text = text + '안녕하세요'
        text += '\n'

    lbl_temp.configure(text=text)


w = tk.Tk()
w.title('문자열 찍어보기')
w.geometry('500x500')

en_input = tk.Entry(w)
btn_string = tk.Button(w, text="문자열 찍기", command=fc2)
lbl_temp = tk.Label(w)

en_input.pack()
btn_string.pack()
lbl_temp.pack()

w.mainloop()

