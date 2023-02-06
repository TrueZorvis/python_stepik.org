lst_in = input().split()
notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
lst = sorted(lst_in, key=notes.index)
print(*lst)
