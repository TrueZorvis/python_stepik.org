listA = input().split()
listB = input().split()

setA = set(listA)
setB = set(listB)

print('ДА') if setA <= setB else print('НЕТ')
