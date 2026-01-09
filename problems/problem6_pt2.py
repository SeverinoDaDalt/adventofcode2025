def main(): 
    lines = []
    with open("inputs/input6.txt", "r") as i_f:
        for line in i_f:
            line = line.strip("\n")
            if line.strip()[0].isdigit():
                lines.append(line)
            else:
                operands = line.strip().split()
    total = 0
    current_operand = 0
    current_column = 0
    subtotal = 0 if operands[current_operand] == "+" else 1
    for i in range(len(lines[0])):
        number = ""
        for line in lines:
            number += line[i]
        number = number.strip()
        if number == "":
            total += subtotal
            current_operand += 1
            subtotal = 0 if operands[current_operand] == "+" else 1
        elif operands[current_operand] == "+":
            subtotal += int(number)
        else:
            subtotal *= int(number)
        current_column += 1
    if (operands[current_operand] == "+" and subtotal != 0) or (operands[current_operand] == "*" and subtotal != 1):
        total += subtotal
        current_operand += 1
    assert current_operand == len(operands), f"{current_operand=}, {len(operands)=}"
    print(f"Total is: {total}")


if __name__ == "__main__":
    main()
