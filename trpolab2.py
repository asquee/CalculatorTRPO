import math

class S:
    def __init__(self, x):
        self.x = x

    def __add__(self, B):  # Сумма
        return S(self.x + B.x)

    def inv(self):  # Инверсия
        return S(-self.x)

    def __mul__(self, B):  # Произведение
        return S(self.x * B.x)

    def __pow__(self, B):  # Степень
        return S(self.x ** B.x)

    def root(self, B):  # Степенной корень √[b](a)
        if self.x < 0 and B.x % 2 == 0:
            print("Ошибка: нельзя извлечь корень четной степени из отрицательного числа!")
            return S(float('nan'))
        return S(self.x ** (1 / B.x))

    def sin(self):
        return S(math.sin(self.x))

    def cos(self):
        return S(math.cos(self.x))

    def tan(self):
        return S(math.tan(self.x))

    def __str__(self):
        return f"{self.x}"


class V:
    def __init__(self, arr):
        self.arr = arr

    def __add__(self, B):  # Поэлементное сложение
        return V([a + b for a, b in zip(self.arr, B.arr)])

    def __mul__(self, B):  # Поэлементное умножение
        return V([a * b for a, b in zip(self.arr, B.arr)])

    def __str__(self):
        return str(self.arr)


class M:
    def __init__(self, data):
        self.data = data

    def __add__(self, B):  # Поэлементное сложение
        res = []
        for i in range(len(self.data)):
            row = [a + b for a, b in zip(self.data[i], B.data[i])]
            res.append(row)
        return M(res)

    def __mul__(self, B):  # Поэлементное умножение
        res = []
        for i in range(len(self.data)):
            row = [a * b for a, b in zip(self.data[i], B.data[i])]
            res.append(row)
        return M(res)

    def __str__(self):
        return str(self.data)


# Функции ввода
def input_scalar(name):
    val = float(input(f"{name} = "))
    return S(val)


def input_vector(name):
    s = input(f"{name} = ")
    vals = [float(x) for x in s.split()]
    return V(vals)


def input_matrix(name):
    print(f"матрица {name} (каждая строка через пробел, пустая строка для завершения):")
    data = []
    while True:
        line = input()
        if not line:
            break
        row = [float(x) for x in line.split()]
        data.append(row)
    return M(data)


# Меню
def main():
    print("математический калькулятор")
    print("1. скаляры")
    print("2. векторы")
    print("3. матрицы")
    print("0. выход")

    while True:
        c = input("\nВыбор: ")

        if c == '0':
            print("Выход")
            break

        elif c == '1':
            print("\nСкаляры")
            a = input_scalar("a")
            b = input_scalar("b")

            print(f"\na = {a}")
            print(f"b = {b}")
            print(f"a + b = {a + b}")
            print(f"инверсия a: {a.inv()}")
            print(f"инверсия b: {b.inv()}")
            print(f"a * b = {a * b}")
            print(f"a ^ b = {a ** b}")
            print(f"√[b](a) = {a.root(b)}") 
            print(f"sin(a) = {a.sin()}")
            print(f"cos(a) = {a.cos()}")
            print(f"tan(a) = {a.tan()}")

        elif c == '2':
            print("\n Векторы")
            v1 = input_vector("v1")
            v2 = input_vector("v2")

            print(f"\nv1 = {v1}")
            print(f"v2 = {v2}")

            if len(v1.arr) == len(v2.arr):
                print(f"v1 + v2 = {v1 + v2}")
                print(f"v1 * v2 = {v1 * v2}")
            else:
                print("векторы разной длины")

        elif c == '3':
            print("\nМатрицы")
            A = input_matrix("A")
            B = input_matrix("B")

            print(f"\nA:")
            print(A)
            print(f"\nB:")
            print(B)

            # Проверяем одинаковость размеров
            a_rows, a_cols = len(A.data), len(A.data[0]) if A.data else 0
            b_rows, b_cols = len(B.data), len(B.data[0]) if B.data else 0

            if a_rows == b_rows and a_cols == b_cols:
                print(f"\nA + B:")
                print(A + B)
                print(f"\nA * B:")
                print(A * B)
            else:
                print("матрицы разного размера")

        else:
            print("надо выбрать от 1 до 3")


if __name__ == "__main__":
    main()
