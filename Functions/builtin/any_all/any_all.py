# 5
# 12 9 61 5 14

_, Y = input(), map(int, input().split())
print(all([any(filter(lambda x: str(x) == str(x)[::-1], Y)), all(i > 0 for i in Y)]))
