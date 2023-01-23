setA = set(map(int, input().split()))
setB = {2}
res = setA & setB
print('ДОПУЩЕН') if len(res) == 0 else print('НЕ ДОПУЩЕН')
