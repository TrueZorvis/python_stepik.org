names = input().split()
msg = 'НЕТ'
i = 0
while i < len(names):
    name = names[i].lower()
    if name[0] == name[-1]:
        msg = 'ДА'
        break
    i += 1
print(msg)
