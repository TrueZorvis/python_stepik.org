def is_odd(num):
    return num % 2 != 0


lst_in = map(int, input().split())

lst = [n for n in lst_in if is_odd(n)]
print(*lst)
