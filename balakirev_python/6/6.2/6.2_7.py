things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

max_weight = int(input()) * 1000
current_weight = 0
get_things = []

while current_weight < max_weight:
    if len(things) == 0:
        break

    value_max = 0
    key_max = None
    for k, v in things.items():
        if v > value_max:
            value_max = v
            key_max = k

    if current_weight + value_max <= max_weight:
        get_things.append(key_max)
        things.pop(key_max)
        current_weight += value_max
    else:
        things.pop(key_max)

print(*get_things)






