a = list(map(int, input().split()))
n = a[0]
k = a[1]
b = list(map(int, input().split()))

"""since index starts from 0, we need to take k-1"""
cutoff_score = b[k - 1]
cnt = 0
for i in b:
    if i > 0 and i >= cutoff_score:
        cnt += 1

print(cnt)
