from collections import deque

#items = int(input())
items = 6

dat = ["append 1",
"append 2",
"append 3",
"appendleft 4",
"pop",
"popleft"]

de = deque()
cls = globals()["de"]


for i in range(items):    
    func = dat[i].split()    
    if len(func) != 1:
        getattr(de, func[0],)(func[-1])
    else:        
        getattr(de, func[0],)()

print(" ".join(de))
