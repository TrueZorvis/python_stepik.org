def get_rec_N(n):
    if n == 0:
        return
    get_rec_N(n-1)
    print(n)


N = int(input())
get_rec_N(N)
