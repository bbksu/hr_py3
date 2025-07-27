def door_mat(height):
    height = int(height)
    width = height * 3
    midpoint = (height + 1) // 2
    mid_string = ".|."
    for i in range(0, height):
        i = min(height - (i + 1), i)
        center = f"{mid_string * i}{mid_string}{mid_string * i}"
        if i + 1 == midpoint:
            center = "WELCOME"
        dash = "-" * ((width - len(center)) // 2)
        print(f"{dash}{center}{dash}")


if __name__ == '__main__':
    N, M = input().split()
    door_mat(N)
