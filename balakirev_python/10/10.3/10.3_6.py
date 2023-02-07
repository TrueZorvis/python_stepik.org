import random
random.seed(1)

# lst_in = input().split()
lst_in = ['Петров', 'Иванов', 'Сидоров', 'Балакирев', 'Фридман']
s = random.sample(lst_in, 3)
print(*s)
