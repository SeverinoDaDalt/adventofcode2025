def main(): 
    lines = []
    with open("inputs/input6.txt", "r") as i_f:
        for line in i_f:
            line = line.strip().split()
            if line[0].isdigit():
                lines.append([int(n) for n in line])
            else:
                operands = line
    total = 0
    for i in range(len(operands)):
        if operands[i] == "+":
            subtotal = 0
            for line in lines:
                subtotal += line[i]
        else:
            subtotal = 1
            for line in lines:
                subtotal *= line[i]
        total += subtotal
    print(f"Total is: {total}")


if __name__ == "__main__":
    main()
