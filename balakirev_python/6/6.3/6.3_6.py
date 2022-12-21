names = tuple(input().split())

for name in names:
    if 'ва' in name.lower():
        print(name.lower(), end=' ')
