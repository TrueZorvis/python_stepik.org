N = int(input())

lst = [i for i in range(1, N + 1) if N % i == 0]

print(*lst)
