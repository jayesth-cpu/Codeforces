n = int(input())
count = 1
prev = int(input())
for _ in range(n - 1):
    i = int(input())
    if i != prev:
        count += 1
    prev = i

print(count)
