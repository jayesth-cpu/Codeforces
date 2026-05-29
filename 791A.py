l = list(map(int, input().split()))
a = l[0]
b = l[1]
count = 0
while a <= b:
    a *= 3
    b *= 2
    count += 1

print(count)
