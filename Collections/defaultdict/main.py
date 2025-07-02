from collections import defaultdict

A_size, B_size = list(map(int, input().split()))
d_dict = defaultdict(list)
for i in range(1, A_size + 1):
    d_dict[input()].append(str(i))    

for i in range(B_size):
    y = d_dict[input()] or "-1"    
    chk = " ".join(y).replace("- 1", "-1")
    print(chk)
