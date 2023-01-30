import sys

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = ['зонт=1000',
          'палатка=10000',
          'спички=22',
          'котелок=543']

tp = tuple(map(lambda x: tuple(x.split('=')), lst_in))
fl = filter(lambda x: int(x[1]) > 500, tp)

for el in list(fl):
    print(el[0], end=' ')
