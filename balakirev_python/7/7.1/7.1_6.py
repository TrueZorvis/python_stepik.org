def print_message(lst):
    print(f"Min = {min(lst)}, max = {max(lst)}, sum = {sum(lst)}")


lst_in = list(map(int, input().split()))
print_message(lst_in)
