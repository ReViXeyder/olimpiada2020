n = int(input())
for g in range(n):
    for k in range(n):
        if g * 2 + k * 4 == n:
            print(g, k)
