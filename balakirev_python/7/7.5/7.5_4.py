def get_biggest_city(*args):
    # biggest = args[0]
    # for city in args[1:]:
    #     if len(city) > len(biggest):
    #         biggest = city
    # return biggest

    return max(args, key=len)


print(get_biggest_city('Питер', 'Москва', 'Самара', 'Воронеж'))
