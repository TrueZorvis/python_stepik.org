lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

lst1.sort()
lst2.sort(reverse=True)

result = list(map(sum, zip(lst1, lst2)))
print(*result)
