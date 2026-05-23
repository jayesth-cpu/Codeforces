a = list(map(int, input().split()))
n = a[0]
k = a[1]
b = list(map(int, input().split()))
for _ in range(n):
    cnt = 0
    for i in range(n):
        if b[i] > k and b[i] != b[i - 1] or b[i] == k:
            cnt += 1

print(cnt)
