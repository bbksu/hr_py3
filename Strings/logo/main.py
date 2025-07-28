def logo(standard):
    length = standard * standard
    letter = "H"
    letter_stack = letter * standard
    max_width = letter_stack * 5
    max_width_size = len(max_width)
    max_shift = len(letter * (standard * 2))
    tips = []
    for i in range(1, standard * 2, 2):
        letters = i * letter
        spaces = max_width_size - len(letters)
        tip = f"{letters:^{max_shift}}{spaces * ' '}"
        tips.append(tip)
    tips = "\n".join(tips)
    print(tips)

    rows = standard + 1
    spaces = max_width_size - len((letter_stack * 2))
    letter_row = []
    for i in range(1, rows + 1):
        letters = f"{letter_stack}{spaces * ' '}{letter_stack}"
        letters = f"{letters:^{max_width_size + standard}}"
        letter_row.append(letters)
    letter_row = "\n".join(letter_row)
    print(letter_row)
    center_shift = len(max_width) + (max_shift - len(letter_stack))
    extend = (standard + 1) // 2
    mid_range = ((length + 1) // 2) - (extend - 1) // 2
    mid_range = (mid_range + extend) - mid_range

    for i in range(mid_range):
        print(f"{max_width:^{center_shift}}")
    print(letter_row)
    tips = tips[::-1].split("\n")
    for i in tips:
        print(f"{i.replace(' ', ''):^{standard * 10}}")


if __name__ == '__main__':
    # logo(int(input()))
    logo(7)
    print()
    logo(5)
