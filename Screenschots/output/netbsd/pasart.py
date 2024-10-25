def basic_round(n):
    """Округление по правилам BASIC: округляет вверх при .5"""
    return int(n + 0.5) if n > 0 else int(n - 0.5)


def print_header():
    print(" " * 24 + "PASART")
    print(" " * 18 + "CREATIVE COMPUTING")
    print(" " * 16 + "MORRISTOWN   NEW JERSEY")
    print("\n" * 2)


def initialize_p_array(size):
    # Создаем массив с индексами, начинающимися с 1
    return [[0] * (size + 1) for _ in range(size + 1)]


def pascal_triangle(t, q):
    p = initialize_p_array(t)

    # Создание треугольника Паскаля
    for r in range(1, t + 1):
        for c in range(1, t + 1):
            if r == 1 or c == 1:
                p[r][c] = 1
            else:
                p[r][c] = basic_round(p[r][c - 1] + p[r - 1][c])

    # Вывод треугольника Паскаля с художественным эффектом
    for r in range(1, t + 1):
        for c in range(1, t + 1):
            if p[r][c] != 0 and p[r][c] % q != 0:
                print("* ", end="")
            else:
                print("  ", end="")
        print()


def double_pascal_art(t, q):
    p = initialize_p_array(t)
    z = t

    # Верхняя левая половина
    n = z
    for r in range(1, n + 1):
        for c in range(1, z):
            if r == 1 or c == 1:
                p[r][c] = 1
            else:
                p[r][c] = basic_round(p[r][c - 1] + p[r - 1][c])
        z -= 1

    # Нижняя правая половина
    z = n
    n = 2
    for r in range(z, 0, -1):
        for c in range(z, n - 1, -1):
            if r == z or c == z:
                p[r][c] = 1
            else:
                p[r][c] = basic_round(p[r][c + 1] + p[r + 1][c])
        n += 1

    # Заполнение всех пустых элементов нулями
    for r in range(1, t + 1):
        for c in range(1, t + 1):
            if p[r][c] == 0:
                p[r][c] = 1

    # Вывод двойного треугольника Паскаля
    for r in range(1, t + 1):
        for c in range(1, t + 1):
            # Условие для вывода только крайних точек на диагонали
            if r + c == t + 1 and (r == 1 or r == t):
                print("* ", end="")
            elif r + c != t + 1:
                if p[r][c] != 0 and p[r][c] % q != 0:
                    print("* ", end="")
                else:
                    print("  ", end="")
            else:
                print("  ", end="")  # Пустое место на диагонали
        print()


def four_corners_pascal_art(t, q):
    p = initialize_p_array(t)
    y = t
    z = y // 2
    z1 = z
    z2 = z1
    z3 = z2
    x4 = z3
    x5 = x4

    # Верхний левый угол
    for i in range(1, z1 + 1):
        for j in range(1, z + 1):
            if i == 1 or j == 1:
                p[i][j] = 1
            else:
                p[i][j] = basic_round(p[i][j - 1] + p[i - 1][j])
        z -= 1

    # Верхний правый угол
    for i in range(1, z1 + 1):
        for j in range(y, x5, -1):
            if i == 1 or j == y:
                p[i][j] = 1
            else:
                p[i][j] = basic_round(p[i][j + 1] + p[i - 1][j])
        x5 += 1

    # Нижний левый угол
    for i in range(y, x4, -1):
        for j in range(1, z2 + 1):
            if i == y or j == 1:
                p[i][j] = 1
            else:
                p[i][j] = basic_round(p[i][j - 1] + p[i + 1][j])
        z2 -= 1

    # Нижний правый угол
    for i in range(y, z3, -1):
        for j in range(y, z3, -1):
            if i == y or j == y:
                p[i][j] = 1
            else:
                p[i][j] = basic_round(p[i][j + 1] + p[i + 1][j])
        z3 += 1

    # Вывод четырехугольного рисунка
    for r in range(1, t + 1):
        for c in range(1, t + 1):
            if p[r][c] != 0 and p[r][c] % q != 0:
                print("* ", end="")
            else:
                print("  ", end="")
        print()


def main():
    print_header()
    print("THIS PROGRAM CREATES ARTIST DESIGNS BASED ON PASCAL'S TRIANGLE.")
    print("YOU HAVE 3 BASIC TYPES OF DESIGNS TO SELECT FROM:")
    print("1. A SINGLE PASCAL'S TRIANGLE (PLAYED WITH AN ARTISTIC FLARE)")
    print("2. TWO 'ARTSY' PASCAL'S TRIANGLES PRINTED BACK TO BACK")
    print("3. FOUR 'ARTSY' TRIANGLES IN THE CORNER OF")
    print("   A SQUARE ARRAY.")

    while True:
        try:
            o = int(input("WHAT'S YOUR PLEASURE? 1, 2 OR 3: "))
            if o in [1, 2, 3]:
                break
        except ValueError:
            continue

    q = int(input("WHICH MULTIPLES DO YOU WANT REPRESENTED WITH BLANKS: "))
    while True:
        try:
            t = int(input("HOW MANY ROWS AND COLUMNS IN THE ARRAY (36 IS MAXIMUM): "))
            if 1 <= t <= 36:
                break
        except ValueError:
            continue

    if o == 1:
        pascal_triangle(t, q)
    elif o == 2:
        double_pascal_art(t, q)
    elif o == 3:
        four_corners_pascal_art(t, q)


if __name__ == "__main__":
    main()
