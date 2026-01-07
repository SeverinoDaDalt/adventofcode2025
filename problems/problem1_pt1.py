def main():
    with open("inputs/input1.txt", "r") as i_f:
        current_number = 50
        zeros = 0
        for line in i_f:
            line = line.strip()
            rotation, quantity = line[0], int(line[1:])
            if rotation == "L":
                current_number = (current_number - quantity) % 100
            else:
                current_number = (current_number + quantity) % 100
            if current_number == 0:
                zeros += 1
        print(f"Total of zeros: {zeros}")
    

if __name__ == "__main__":
    main()
