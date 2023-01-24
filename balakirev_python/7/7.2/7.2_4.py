def is_even(num):
    return num % 2 == 0


while True:
    n = int(input())

    if n == 1:
        break

    if is_even(n):
        print(n)
