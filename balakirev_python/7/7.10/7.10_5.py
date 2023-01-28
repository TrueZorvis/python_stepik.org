def do_convert(tp='list'):
    def func(string):
        collection = list(map(int, string.split()))
        return collection if tp == 'list' else tuple(collection)
    return func


f = do_convert(input())
lst = f(input())
print(lst)
