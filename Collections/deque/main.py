from collections import deque

items = int(input())
de = deque()
for i in range(items):    
    func = input().split()     
    if len(func) != 1:
        getattr(de, func[0],)(func[-1])
    else:        
        getattr(de, func[0],)()

print(" ".join(de))
