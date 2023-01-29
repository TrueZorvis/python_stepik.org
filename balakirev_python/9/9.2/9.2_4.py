import random
from string import ascii_lowercase, ascii_uppercase


chars = ascii_lowercase + ascii_uppercase
random.seed(1)


def get_email(n):
    while True:
        s = ''
        for _ in range(n):
            indx = random.randint(0, len(chars) - 1)
            s += chars[indx]
        yield s + '@mail.ru'


N = int(input())

g = get_email(N)
for _ in range(5):
    print(next(g))
