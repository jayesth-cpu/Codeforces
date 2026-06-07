t = int(input())
for _ in range(t):
    n = int(input())
    valid = False
    for a in range(n+1):
        b = n-a
        if str(a) == str(a)[::-1] and b % 12 == 0:
            print(a,b)
            valid = True
            break
            
    if not valid:
        print(-1)