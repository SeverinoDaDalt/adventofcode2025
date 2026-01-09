def main(): 
    with open("inputs/input7.txt", "r") as i_f:
        for line in i_f:
            npaths_per_beam = [0] * len(line.strip())
            break
    with open("inputs/input7.txt", "r") as i_f:
        for line in i_f:
            line = line.strip()
            for i in range(len(line)):
                if line[i] == ".":
                    continue
                elif line[i] == "S":
                    npaths_per_beam[i] = 1
                elif line[i] == "^":
                    if npaths_per_beam[i]:
                        npaths_per_beam[i-1] += npaths_per_beam[i]
                        npaths_per_beam[i+1] += npaths_per_beam[i]
                        npaths_per_beam[i] = 0
                else:
                    raise ValueError(line[i])
    total = sum(npaths_per_beam)
    print(f"Total is: {total}")


if __name__ == "__main__":
    main()
