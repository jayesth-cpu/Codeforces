t = int(input())
for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))
    max_val = max(h)
    min_val = min(h)

    print(max_val - min_val + 1)