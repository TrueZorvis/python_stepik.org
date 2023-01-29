def get_simple_num():
    i = 2
    while True:
        j = 1
        cnt = 0
        while j <= i:
            if i % j == 0:
                cnt += 1
            j += 1
        if cnt <= 2:
            yield i
        i += 1


g = get_simple_num()
for _ in range(50):
    print(next(g), end=' ')
