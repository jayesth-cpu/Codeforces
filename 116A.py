n = int(input())
count = 0
max_count = 0
for _ in range(n):
    l = list(map(int, input().split()))
    a = l[0]
    b = l[1]
    count += b
    count -= a
    max_count = max(max_count, count)

print(max_count)
