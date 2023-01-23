lst_in = ['Пушкин: Сказака о рыбаке и рыбке',
          'Есенин: Письмо к женщине',
          'Тургенев: Муму',
          'Пушкин: Евгений Онегин',
          'Есенин: Русь']

lst = [i.split(': ') for i in lst_in]
d = {lst[i][0]: {lst[j][1] for j in range(len(lst)) if lst[j][0] == lst[i][0]} for i in range(len(lst))}
print(d)

d = {}
for item in lst_in:
    author, book = item.split(": ")
    if author not in d:
        d[author] = {book}
    else:
        d[author].add(book)
print(d)
