
if __name__ == '__main__':
    n = int(input().strip())
    if n & 1 != 0 or (n & 1 == 0 and (6 <= n <= 20)):
        print("Weird")
    elif n & 1 == 0 and ((2 <= n <= 5) or n > 20):
        print("Not Weird")