def print_formatted(number):
    # your code goes here
    n_string = ""
    m_ax = bin(number)[2:]
    size = len(m_ax)
    for i in range(1, number + 1):
        i = int(i)                
        g = f"{i:>{size}} {oct(i)[2:]:>{size}} {hex(i).upper()[2:]:>{size}} {bin(i)[2:]:>{size}}"

        # bins = f"{bin(i)[2:]:>5}"        
        # hexes = f"{hex(i)[2:]:>{size}}"               
        # print(hexes)
        print(g)
        # print(bins)
        # n_string += g.upper()
    # print(n_string[:-1])

    

if __name__ == '__main__':
    # n = int(input())
    n = 17
    print_formatted(n)