from math import atan, degrees

a = int(input())
b = int(input())

degree = u'\N{DEGREE SIGN}'
print(f"{str(round(degrees(atan(a / b))))}{degree}")
