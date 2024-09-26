import tkinter as tk
import math

def click(char):
    if char == 'C':  # если нажата кнопка очистки
        expression.set("")
    elif char == '=':  # если нажата кнопка равенства
        try:
            # заменяем спец функции
            result = eval(expression.get().replace('^', '**').replace
                          ('sqrt', 'math.sqrt').replace('log', 'math.log10'))
            expression.set(result)
        except Exception as e:
            expression.set("Ошибка")
    else:  # добавление символов в выражение
        expression.set(expression.get() + str(char))  # Обновляем выражение

root = tk.Tk()
root.configure(background='#C2FFC2')
root.title("Калькулятор")

expression = tk.StringVar()  # хранение выражения

entry = tk.Entry(root, textvariable=expression, width=30, borderwidth=5, background='#FFC2C2')
entry.grid(row=0, column=0, columnspan=4)

# Определяем кнопки для калькулятора
buttons = [
    '7', '8', '9', 'C',  # Кнопки для числа и очистки
    '4', '5', '6', '/',
    '1', '2', '3', '*',
    '0', 'sqrt', 'log', '-',  # Кнопки для операций
    '(', ')', '^', '+',
    '='  # Кнопка для вычисления результата
]

# размещаем кнопки на сетке
row = 1
col = 0
for i in buttons:
    # создание работающей кнопки
    btn = tk.Button(root, text=i, width=7, command=lambda btn=i: click(btn), background= '#FFDEDE')
    btn.grid(row=row, column=col)
    col += 1

    if col > 3:  # переход на след строку
        col = 0
        row += 1

root.mainloop()
