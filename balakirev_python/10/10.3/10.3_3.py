import random
random.seed(1)

a, b = map(int, input().split())
print(random.randint(a, b))
