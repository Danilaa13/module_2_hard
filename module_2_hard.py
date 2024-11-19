def result():
    n = int(input())
    for i in range(1, n+1):
        count = ''
        for j in range(1,21):
            for k in range(1,21):
                if i % (j + k) == 0 and j != k and j < k:
                    count += f'{j}{k}'
    print(n, '-', count)

result()