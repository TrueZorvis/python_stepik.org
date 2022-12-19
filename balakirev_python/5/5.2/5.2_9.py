import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

i = 0
l = list()
while i < len(lst_in):
    title = lst_in[i]
    if len(title.split()) == 1:
        l.append(title)
    i += 1
print(*l)
