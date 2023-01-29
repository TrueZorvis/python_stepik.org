import random
from string import ascii_lowercase, ascii_uppercase


chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
random.seed(1)


def get_password(n):
    while True:
        s = ''
        for _ in range(n):
            indx = random.randint(0, len(chars) - 1)
            s += chars[indx]
        yield s


N = int(input())

g = get_password(N)
for _ in range(5):
    print(next(g))
