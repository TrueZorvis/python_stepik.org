w = list(input().lower())
msg = "палиндром" if w == w[::-1] else "не палиндром"
print(msg)
