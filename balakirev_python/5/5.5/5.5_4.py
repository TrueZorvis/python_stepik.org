s = input()
it = iter(s)
i = 0
while i<len(s):
    i += 1
    print(next(it), end=' ')
