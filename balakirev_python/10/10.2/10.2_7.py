x_word = input()
key = 123

s = ''
for char in x_word:
    x = ord(char) ^ key
    s += chr(x)

print(s)
