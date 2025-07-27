def door_mat(height):
    height = int(height)
    width = height * 3
    midpoint = (height + 1) // 2
    mid = ".|."
    i = 0
    rev = False
    while True:
        center = f"{mid * i}{mid}{mid * i}"
        if i + 1 == midpoint:
            rev = True
            center = "WELCOME"
        size = width - len(center)
        dash = "-" * (size // 2)
        shape = f"{dash}{center}{dash}"
        print(shape)
        if rev:
            i -= 1
        else:
            i += 1        
        if i < 0:
            break


if __name__ == '__main__':
    N, M = input().split()
    door_mat(N)   
