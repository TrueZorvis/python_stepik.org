# in: house=дом car=машина men=человек tree=дерево
# out: (('house', 'дом'), ('car', 'машина'), ('men', 'человек'), ('tree', 'дерево'))
tp = tuple(map(lambda x: tuple(x.split('=')), input().split()))
print(tp)
