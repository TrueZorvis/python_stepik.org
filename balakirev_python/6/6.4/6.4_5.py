s = set([c for c in input() if c.isdigit()])
if len(s) > 0:
    print(*sorted(s))
else:
    print('НЕТ')
