import sys

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['ножницы=100', 'котелок=500', 'спички=20', 'зажигалка=40', 'зеркальце=50']

d = {item.split('=')[0]: int(item.split('=')[1]) for item in lst_in}
lst = sorted(d.keys(), key=lambda x: d[x], reverse=True)
print(*lst)
