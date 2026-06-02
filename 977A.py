l = list(map(int, input().split()))
n = l[0]
k = l[1]

while k != 0:
    if n % 10 != 0:
        n -= 1
        k -= 1
    else:
        n //= 10
        k -= 1

print(n)
