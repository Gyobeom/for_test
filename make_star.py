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

# for i in range(5):
#     print('{:<5}'.format('*' * (i+1)))
#
# for i in range(5):
#     for j in range(i+1):
#         print('*',end="")
#     print('')
#
#     *
#     **
#     ***
#     ****
#     *****
#
# for i in range(6,0,-1):
#     print('{:<5}'.format('*' * (i-1)))
#
# for i in range(5,0,-1):
#     for j in range(i):
#         print('*',end="")
#     print('')
#
# *****
# ****
# ***
# **
# *
#
#
# for i in range(6,0,-1):
#     print('{:>5}'.format('*' * (i-1)))
#
# for i in range(5):
#     for j in range(i):
#         print(' ',end="")
#     for j in range(5-i):
#         print('*',end="")
#     print('')
#
# *****
#  ****
#   ***
#    **
#     *
#
# for i in range(5):
#     print('{:>5}'.format('*' * (i+1)))
#
# for i in range(1,6):
#     for j in range(5-i):
#         print(' ',end="")
#     for j in range(i):
#         print('*',end="")
#     print('')
#
#     *
#    **
#   ***
#  ****
# *****
#
# for i in range(1, 11, 2):
#     print('{:^10}'.format('*' * i))
#
# for i in range(1,6):
#     for j in range(5-i):
#         print(' ',end="")
#     for j in range(1,i*2,1):
#         print('*',end="")
#     print('')
#
#     *
#    ***
#   *****
#  *******
# *********
#
# for i in range(1, 11, 2):
#     print('{:^10}'.format('*' * i))
# for i in range(9, 0, -2):
#     print('{:^10}'.format('*' * i))
#
# for i in range(1,6):
#     for j in range(5-i):
#         print(' ',end="")
#     for j in range(1,i*2,1):
#         print('*',end="")
#     print('')
# for i in range(5):
#     for j in range(i):
#         print(' ',end="")
#     for j in range(10,1+i*2,-1):
#         print('*',end="")
#     print('')
#
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *
#
#
# for i in range(9, 0, -2):
#     print('{:^10}'.format('*' * i))
#
# for i in range(3, 11, 2):
#     print('{:^10}'.format('*' * i))
#
# for i in range(5):
#     for j in range(i):
#         print(' ',end="")
#     for j in range(10,1+i*2,-1):
#         print('*',end="")
#     print('')
# for i in range(2,6):
#     for j in range(5-i):
#         print(' ',end="")
#     for j in range(1,i*2,1):
#         print('*',end="")
#     print('')
#
# *********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********