def len_string(word):
    if len(word) > 10:
        mid_cnt = str(len(word) - 2)
        return word[0] + mid_cnt + word[-1]
    else:
        return word


n = int(input())
for _ in range(n):
    word = input()
    print(len_string(word))
