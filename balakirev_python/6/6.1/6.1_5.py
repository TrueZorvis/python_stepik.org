# input: "вологда=город house=дом True=1 5=отлично 9=божественно"
d = dict(item.split('=') for item in input().split())
print('ДА' if 'house' in d and 'True' in d and '5' in d else 'НЕТ')
