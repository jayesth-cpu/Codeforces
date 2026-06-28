t = int(input())


for _ in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = all( x>=y for x,y in zip(a,b))
    res = 0

    total_time = sum(a) - sum(b)

    if result:
        print(total_time)

    else:
        a.sort()
        b.sort()
        result = all(x >= y for x, y in zip(a, b))
        if result:
            print(total_time+c)
        else:
            print(-1)