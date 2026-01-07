def main():
    with open("inputs/input1.txt", "r") as i_f:
        current_number = 50
        zeros = 0
        for i, line in enumerate(i_f):
            original_number = current_number
            line = line.strip()
            rotation, quantity = line[0], int(line[1:])
            complete_rotations, remainder = quantity // 100, quantity % 100
            zeros += complete_rotations
            if rotation == "L":
                current_number -= remainder
            else:
                current_number += remainder
            if (current_number >= 100 or current_number <= 0) and remainder != 0 and original_number != 0:
                zeros += 1
            current_number = current_number % 100
    print(f"Total of zeros: {zeros}")
    

if __name__ == "__main__":
    main()
