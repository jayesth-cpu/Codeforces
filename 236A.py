a = input()

seen = []

for char in a:
    if char not in seen:
        seen.append(char)

    else:
        continue
if len(seen) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
