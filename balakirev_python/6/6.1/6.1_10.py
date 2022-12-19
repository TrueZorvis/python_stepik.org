import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
# lst_in = ['ustanovka-i-zapusk-yazyka', 'ustanovka-i-poryadok-raboty-pycharm',
#           'peremennyye-operator-prisvaivaniya-tipy-dannykh', 'arifmeticheskiye-operatsii',
#           'ustanovka-i-poryadok-raboty-pycharm']

d = {}
for item in lst_in:
    if item in d:
        print(f"Взято из кэша: HTML-страница для адреса {d[item]}")
    else:
        d[item] = item
        print(f"HTML-страница для адреса {d[item]}")
