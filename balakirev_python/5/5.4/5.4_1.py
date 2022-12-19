sentance = input()

if 'ра' not in sentance:
    print(-1)
else:
    for i in range(len(sentance)-1):
        if sentance[i] == 'р' and sentance[i+1] == 'а':
            print(i, end=' ')
