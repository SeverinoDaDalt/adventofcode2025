def main(): 
    total = 0
    current_beams = set()
    with open("inputs/input7.txt", "r") as i_f:
        for line in i_f:
            line = line.strip()
            for i in range(len(line)):
                if line[i] == ".":
                    continue
                elif line[i] == "S":
                    current_beams.add(i)
                elif line[i] == "^":
                    if i in current_beams:
                        current_beams.remove(i)
                        current_beams.add(i-1)
                        current_beams.add(i+1)
                        total += 1
                else:
                    raise ValueError(line[i])
    print(f"Total is: {total}")


if __name__ == "__main__":
    main()
