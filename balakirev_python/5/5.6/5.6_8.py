n_summ = int(input())

coins = [1, 2, 4, 8, 16, 32, 64]
res = []

while coins:
    current_nominal = coins.pop()
    count = n_summ // current_nominal
    n_summ %= current_nominal
    res += [current_nominal] * count

print(*res)
