import time


def get_nod(a, b):
    """Вычисляется НОД для натуральных чисел a и b
    по алгоритму Евклида.
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def test_nod(func):
    # --- Test #1 ---
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print('Test #1 - OK')
    else:
        print('Test #1 - FAIL')

    # --- Test #2 ---
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print('Test #2 - OK')
    else:
        print('Test #2 - FAIL')

    # --- Test #3 ---
    a = 2
    b = 100000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print('Test #3 - OK')
    else:
        print('Test #3 - FAIL')
    print(f"Time Test #3: {dt} sec")

    # --- Test #4 ---
    a = 15
    b = 121050
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 15 and dt < 1:
        print('Test #4 - OK')
    else:
        print('Test #4 - FAIL')
    print(f"Time Test #4: {dt} sec")


test_nod(get_nod)

# res = get_nod(18, 24)
# print(res)
# help(get_nod)
