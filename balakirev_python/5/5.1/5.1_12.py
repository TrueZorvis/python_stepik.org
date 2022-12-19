n = 99
while n < 1000:
    n += 1
    if n % 47 == 43 and n % 3 == 0:
        print(n, end=' ')
