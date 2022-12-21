import sys

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['EvgeniyK: спасибо большое!',
          'LinaTroshka: лайк и подписка!',
          'Sergey Karandeev: крутое видео!',
          'Евгений Соснин: обожаю',
          'EvgeniyK: это повтор?',
          'Sergey Karandeev: нет, это новое видео']

names = set([row.split(': ')[0] for row in lst_in])
print(len(names))
