import sys

# считывание списка из входного потока
# lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']

d = {}
for item in lst_in:
    day, name = item.split()
    d.setdefault(int(day), []).append(name)

for k, v in d.items():
    print(f"{k}: {', '.join(v)}")
