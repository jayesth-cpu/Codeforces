n = int(input())
total_solved = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    cnt = 0
    for i in arr:
        cnt += i
    if cnt >= 2:
        total_solved += 1
print(total_solved)
