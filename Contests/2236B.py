t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    s = list(map(int, list(input())))
    
    for i in range(n-k):
        if s[i] == 1:
            s[i] = 0
            if s[i+k] == 0:
                s[i+k] = 1
            else:
                s[i+k] = 0
                
    if sum(s) == 0:
        print("YES")
    else:
        print("NO")