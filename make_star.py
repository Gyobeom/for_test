import tkinter as tk


def fc2():
    stars = ''
    n = int(en_input.get())
    for line in range(1, n+1, 1):
        for space in range(n-line, 0 , -1):
            stars = stars + " "
        for star in range(1, line*2):
            stars = stars + '*'
        stars = stars + '\n'

    lbl_temp.configure(text=stars)

w = tk.Tk()
w.title("별찍기 프로그램 0.1")
w.geometry("500x500")

en_input = tk.Entry(w)
btn_f2c = tk.Button(w, text="별찍어보기", command=fc2)
lbl_temp = tk.Label(w)


en_input.pack()
btn_f2c.pack(fill='x')
lbl_temp.pack()

w.mainloop()






# n = int(input("별 찍기 :"))
#
# for line in range(1, n+1, 1):
#     for space in range(n-line, 0 , -1):
#         print(" ",end="")
#     for star in range(1, line*2, 1):
#         print("*",end='')
#     print()