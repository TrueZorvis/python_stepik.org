a = input()
b = input()
c = int(input())
d = float(input())
book = [a, b, c, d]
del(book[2])
book[1] = "Пушкин"
book[-1] = book[-1] * 2
print(book)
