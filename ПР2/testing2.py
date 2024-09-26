import math

def line():
    while True:
        try:
            a = float(input("Введите длину первой стороны : "))
            b = float(input("Введите длину второй стороны : "))
            c = float(input("Введите длину третьей стороны : "))


            if a <= 0 or b <= 0 or c <= 0:
                raise ValueError(
                    "Длина стороны треугольника не может быть числом меньше или равным нулю, введите правильные "
                    "значения.")
            if a + b <= c or a + c <= b or b + c <= a:
                raise ValueError("Сумма любых двух сторон должна быть больше третьей. Введите правильные  значения.")

            return a, b, c
        except ValueError as e:
            print(e)


def type(a, b, c):

    a2 = a ** 2
    b2 = b ** 2
    c2 = c ** 2

    if a2 + b2 > c2 and a2 + c2 > b2 and b2 + c2 > a2:
        return "остроугольный"
    elif a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2:
        return "прямоугольный"
    else:
        return "тупоугольный"


def pl(a, b, c):

    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def main():
    a, b, c = line()
    t_type = type(a, b, c)
    area = pl(a, b, c)

    print(f"\nВид треугольника: {t_type}")
    print(f"Площадь треугольника: {area:.2f}")


if __name__ == "__main__":
    main()
