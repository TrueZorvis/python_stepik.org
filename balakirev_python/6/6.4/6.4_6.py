import sys

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['Мария',
          'Елена',
          'Екатерина',
          'Александр',
          'Елена',
          'Мария']

print(len(set(lst_in)))
