import sys


def get_cheapest_items(d: dict):
    return [d[key] for key in sorted(d)[:3]]


# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = ['смартфон:120000', 'яблоко:2', 'сумка:560', 'брюки:2500', 'линейка:10', 'бумага:500']

d = {int(item.split(':')[1]): item.split(':')[0] for item in lst_in}
res = get_cheapest_items(d)
print(*res)
