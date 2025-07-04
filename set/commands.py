

input()
a = set(map(int, input().split()))
commands = int(input())

for i in range(commands):    
    func = input().split()
    print(a)
    print(func)
    if len(func) >1 :
        getattr(a, func[0],)(int(func[-1]))
    else:
        getattr(a, func[0],)()

print(sum(a))
