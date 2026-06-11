n = int(input())
a = list(map(int, input().split()))

max_val = max(a)
max_index = a.index(max_val)

min_val = min(a)
min_index = 0
for i in range(n):
    if a[i] == min_val:
        min_index = i
        
        
moves = max_index + (n-1- min_index)
if max_index > min_index:
    moves -=1
    
print(moves)