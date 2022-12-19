expression = input().replace(' ', '').replace('+', ' +').replace('-', ' -')
num_list = map(int, expression.split())
print(sum(num_list))
