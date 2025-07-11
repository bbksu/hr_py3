# 5 3
# 89 90 78 93 80
# 90 91 85 88 86
# 91 92 83 89 90.5

count = list(map(int, input().split()))

zipped = []
for i in range(count[-1]):
    zipped.append(map(float, input().split()))


for i in zip(*zipped):
    print(sum(i)/len(i))
