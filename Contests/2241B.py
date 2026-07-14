t = int(input())

for _ in range(t):
    x = int(input())

    def good(num):
        return(len(set(str(num)))) <= 2
    def is_good(x):
        y = 2
        if "0" in str(x) or len(set(str(x))) == 1:
            print(10)
            return
        while True:

            if good(y) and good(x*y):
                print(y)
                break
            y +=1
    is_good(x)
