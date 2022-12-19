lst_in = [[1, 0, 0, 0, 0],
          [0, 0, 1, 0, 1],
          [0, 0, 0, 0, 0],
          [0, 1, 0, 1, 0],
          [0, 0, 0, 0, 0]]

for i in range(len(lst_in) - 1):
    res = 0
    for j in range(len(lst_in[0]) - 1):
        res = sum([lst_in[i][j], lst_in[i][j + 1], lst_in[i + 1][j], lst_in[i + 1][j + 1]])
        if res > 1:
            break
    if res > 1:
        break

print("НЕТ" if res > 1 else "ДА")


