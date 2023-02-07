lst_in = list(map(int, input().split()))
print('отчислен' if any(map(lambda x: x < 3, lst_in)) else 'учится')
