def main(): 
    total = 0
    with open("inputs/input3.txt", "r") as i_f:
        for line in i_f:
            line = line.strip()
            digits = [int(l) for l in line]
            fdd = []
            previous_i = -1
            for i in range(12):
                best_v = -1
                best_i = -1
                max_i = i - 11 if i != 11 else None
                for j, d in enumerate(digits[previous_i+1:max_i]):
                    if d > best_v:
                        best_v = d
                        best_i = j + previous_i+1
                assert best_i >= 0, max_i
                previous_i = best_i
                fdd.append(str(best_v))
            value = int("".join(fdd))
            total += value
    print(f"Total is: {total}")


if __name__ == "__main__":
    main()
