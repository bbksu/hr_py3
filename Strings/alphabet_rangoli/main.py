def print_rangoli(size):
    # your code goes here
    alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z")
    length = (size - 1) * 2
    length = length + length + 1

    dashes = length // 2 * "-"
    rangoli = []
    for i in range(size):
        row = "-".join(alphabet[(size - 1) - i:size])
        dash = len(dashes) - len(row) + 1
        row = f"{row}{dash * '-'}"
        rangoli.append((row[:0:-1] + row))
    rangoli = rangoli + rangoli[:-1][::-1]
    print("\n".join(rangoli))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
