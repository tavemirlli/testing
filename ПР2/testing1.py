import math

def lines():
    while True:
        try:
            a = float(input("Введите длину первой стороны треугольника: "))
            b = float(input("Введите длину второй стороны треугольника: "))
            c = float(input("Введите длину третьей стороны треугольника: "))

            # Проверка условий
            if a <= 0 or b <= 0 or c <= 0:
                raise ValueError("Длина стороны не может быть меньше или равна 0.")
            if a + b <= c or a + c <= b or b + c <= a:
                raise ValueError("Сумма любых двух сторон должна быть больше третьей.")

            return a, b, c
        except ValueError as e:
            print(e)
            print("Пожалуйста, введите правильные значения.")

def type(a, b, c):
    if a == b == c:
        return "равносторонний"
    elif a == b or b == c or a == c:
        return "равнобедренный"
    else:
        return "разносторонний"

def pl(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def main():
    a, b, c = lines()
    t_type = type(a, b, c)
    area = pl(a, b, c)

    print(f"\nВид треугольника: {t_type}")
    print(f"Площадь треугольника: {area:.2f}")

if __name__ == "__main__":
    main()
