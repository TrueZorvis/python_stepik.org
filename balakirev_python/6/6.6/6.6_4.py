lst_in = list(input().split())

setA = {i.lower() for i in lst_in if len(i) >= 3}
print(len(setA))
