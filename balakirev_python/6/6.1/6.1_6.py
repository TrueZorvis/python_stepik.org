d = dict([item.split("=") for item in input().split()])
if 'False' in d:
    del d['False']

if '3' in d:
    del d['3']

print(*sorted(d.items()))
