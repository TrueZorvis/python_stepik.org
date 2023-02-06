lst = list(set(map(int, input().split())))
lst.sort(reverse=True)
print(*lst[:4])
