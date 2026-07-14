t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    left_cnt, right_cnt = 0, 0
    for i in range(n):
        if s[i] == "#":
            left_cnt += 1
        else:
            break
    for i in range(n-1, -1,-1):
        if s[i] == "#":
            right_cnt += 1
        else:
            break
    left_time = (left_cnt + 1) // 2
    right_time = (right_cnt + 1) // 2
    time = max(left_time, right_time)
    print(time)

    """
5
7
#*##*##
8
########
8
********
8
#*****##
6
*#####

    """
