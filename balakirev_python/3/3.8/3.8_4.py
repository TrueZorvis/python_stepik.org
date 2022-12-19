lst = list(input())
lst.remove("+")
lst[0] = "8"
lst.remove("-")
lst.remove("-")
print("".join(lst))
