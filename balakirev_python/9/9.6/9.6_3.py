def get_sort(d: dict):
    return [d[key] for key in sorted(d, reverse=True)]


d = {'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}
res = get_sort(d)
print(res)
