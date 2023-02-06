import sys

# считывание списка из входного потока (не меняйте переменную lst_in в программе)
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['Номер;Имя;Оценка;Зачет', '1;Портос;5;Да', '2;Арамис;3;Да', '3;Атос;4;Да', "4;д'Артаньян;2;Нет", '5;Балакирев;1;Нет']


def get_tuple(lst: str):
    x = lst.split(';')
    if x[0].isdigit() and x[2].isdigit():
        return x[1], x[3], int(x[2]), int(x[0])
    return x[1], x[3], x[2], x[0]


t_sorted = tuple([get_tuple(item) for item in lst_in])
print(t_sorted)
