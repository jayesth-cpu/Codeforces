t = int(input())
for _ in range(t):
    k = int(input())
    c = list(map(int,input().split()))
    if max(c) >= 3:
        print("YES")
    elif max(c) == 2:
        if c.count(2) >= 2:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")