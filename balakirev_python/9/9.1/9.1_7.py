from string import ascii_lowercase

g = (x + y for x in ascii_lowercase for y in ascii_lowercase)

# for _ in range(50):
#     print(next(g), end=' ')

print(*(next(g) for _ in range(50)))
