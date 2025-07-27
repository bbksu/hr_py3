def print_formatted(number):
    size = len(bin(number)[2:])
    for i in range(1, number + 1):
        i = int(i)
        print(f"{i:>{size}} {oct(i)[2:]:>{size}} {hex(i).upper()[2:]:>{size}} {bin(i)[2:]:>{size}}")


if __name__ == '__main__':
    n = int(input())    
    print_formatted(n)