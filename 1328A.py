t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    a = l[0]
    b = l[1]

    n = a // b
    if a % b != 0:
        print(b * (n + 1) - a)
    else:
        print(0)
