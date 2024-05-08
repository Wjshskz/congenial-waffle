import tkinter as tk

def button_click(symbol):
    if symbol == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "오류!")
    elif symbol == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, symbol)

# 윈도우 생성
window = tk.Tk()
window.title("간단한 계산기")
window.configure(bg="#add8e6")  # 배경색을 푸른 계열로 설정

# 입력창 생성
entry = tk.Entry(window, width=20, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4)

# 버튼 생성
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0)
]

for (symbol, row, col) in buttons:
    button = tk.Button(window, text=symbol, width=5, height=2, font=("Arial", 14),
                        command=lambda s=symbol: button_click(s))
    button.grid(row=row, column=col)
    button.configure(bg="#87ceeb", fg="black")  # 버튼의 배경색과 글자색을 설정

window.mainloop()

