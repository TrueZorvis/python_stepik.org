c = list(input().split())
if 'Москва' in c:
    c.remove('Москва')
print(*c)
