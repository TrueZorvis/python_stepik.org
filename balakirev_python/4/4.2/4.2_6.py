m, n = map(int, input().split())
if m == 2:
    if n == 1:
        print("01.31 02.02")
    elif n == 28:
        print("02.27 03.01")
    else:
        print(f"02.{n-1:02} 02.{n+1:02}")
elif m in [4, 6, 9, 11]:
    if n == 1:
        print(f"{m-1:02}.31 {m:02}.02")
    elif n == 30:
        print(f"{m:02}.29 {m+1:02}.01")
    else:
        print(f"{m:02}.{n-1:02} {m:02}.{n+1:02}")
elif m in [1, 3, 5, 7, 8, 10, 12]:
    if n == 1:
        if m == 3:
            print("02.28 03.02")
        elif m == 8:
            print("07.31 08.02")
        else:
            print(f"{m-1:02}.30 {m:02}.02")
    elif n == 31:
        print(f"{m:02}.30 {m+1:02}.01")
    else:
        print(f"{m:02}.{n-1:02} {m:02}.{n+1:02}")
