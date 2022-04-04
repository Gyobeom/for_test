import tkinter as tk


def fc2():
    """화씨 온도를 섭씨 온도로 바꿔주는 함수 (엔트리 객체로 부터 입력, 레이블 객체에 출력)"""
    # (100°F − 32) × 5/9 = 37.778°C 화씨 to 섭씨
    # (100°F − 32) × 5 / 9 = 37.778°C
    try:
        f = float(en_input.get())
        c = (f - 32) * (5 / 9)
        lbl_temp.configure(text=f'화씨 {f}도는 섭씨{round(c,4)}')
    except ValueError as e:
        lbl_temp.configure(text='{0}은 숫자가 아닙니다. 숫자를 입력해주세요 \n {1}'.format(en_input.get(), e))
        en_input.delete(0, 'end')


# (100°F − 32) × 5/9 = 37.778°C 화씨 to 섭씨
# (0°C × 9/5) + 32 = 32°F

def c2f():
    """섭씨 온도를 화씨 온도로 바꿔주는 함수 (엔트리 객체로 부터 입력, 레이블 객체에 출력)"""
    try:
        c = float(en_input.get())
        f = (c * (9 / 5)) + 32
        lbl_temp.configure(text=f'섭씨 {c}도는 화씨{round(f, 4)}')
    except ValueError as e:
        lbl_temp.configure(text='{0}은 숫자가 아닙니다. 숫자를 입력해주세요 \n {1}'.format(e.get(), e))
        e.delete(0, 'end')
    # print(f'화씨 {f}도는 섭씨{round(c,4)}')


if __name__ == "__main__":
    help(fc2)
    w = tk.Tk()
    w.title("온도변환프로그램 0.1")
    w.geometry("300x100")

    en_input = tk.Entry(w)
    btn_f2c = tk.Button(w, text="화씨 -> 섭씨", command=fc2)
    btn_c2f = tk.Button(w, text="섭씨 -> 화씨", command=c2f)
    lbl_temp = tk.Label(w, text="온도변환")
    en_input.focus()

    en_input.pack()
    btn_f2c.pack(fill='x')
    btn_c2f.pack(fill='x')
    lbl_temp.pack()

    w.mainloop()
