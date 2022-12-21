import sys

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = ['Главная home',
          'Python learn-python',
          'Java learn-java',
          'PHP learn-php']

menu = tuple([tuple(item.split()) for item in lst_in])

print(menu)
