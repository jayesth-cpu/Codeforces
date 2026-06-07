t = int(input())
for _ in range(t):
    k = int(input())
    b = list(map(int,input().split()))
    valid = False
    for i in range(k):
        for j in range(k):
            if i == j:
                continue
            x,y = b[i],b[j]
            if x<y:
                continue
            
            seq = [x,y]
            for i in range(2,k):
                # final_seq = seq[-2] % seq[-1]
                if seq[-1] == 0:
                    valid = False
                    break
                seq.append(seq[-2] % seq[-1])
                
            if sorted(seq) == sorted(b):
                print(x,y)
                valid = True
                break
        if valid:
            break
    if not valid:
        print(-1)
            
        
    
        
            
    