def is_large(word):
    return len(word) >= 6


lst_in = input().split()

lst = [city for city in lst_in if is_large(city)]
print(*lst)
