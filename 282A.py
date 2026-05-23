n = int(input())
count = 0
for _ in range(n):
    a = input()
    if a == "X++" or a == "++X":
        count += 1
    else:
        count -= 1

print(count)
