s = input()
it = iter(s)
while True:
    a = next(it)
    if a == " ":
        break
    else:
        print(a, end='')
