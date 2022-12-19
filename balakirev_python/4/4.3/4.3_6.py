m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']
a, b, c = map(int, input().split())
a1 = '#' + m[a-1] if a == 1 or a == 4 else m[a-1]
b1 = '#' + m[b-1] if b == 1 or b == 4 else m[b-1]
c1 = '#' + m[c-1] if c == 1 or c == 4 else m[c-1]
print(a1, b1, c1)
