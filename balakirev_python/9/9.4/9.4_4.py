set_in1 = set(map(int, input().split()))
set_in2 = set(map(int, input().split()))

set_in = set_in1.intersection(set_in2)
flt = filter(lambda x: x % 2 == 0, set_in)
print(*sorted(flt))
