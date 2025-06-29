def stack(lengths, cubes):
    if lengths[0] >= lengths[-1]:
        cubes.append(lengths[0])
        lengths.pop(0)
    else:
        cubes.append(lengths[-1])
        lengths.pop(-1)
    return lengths


def stackable_cube(lengths):
    cubes = []
    while True:
        if len(lengths) == 0:
            if sorted(cubes, reverse=True) == cubes:
                return "Yes"
            else:
                return "No"
        lengths = stack(lengths, cubes)


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        int(input())
        blocks = list(map(int, input().split()))
        print(stackable_cube(blocks))
