def main(): 
    total = 0
    with open("inputs/input3.txt", "r") as i_f:
        for line in i_f:
            line = line.strip()
            digits = [int(l) for l in line]
            current_max_v = -1
            current_max_i = -1
            for i, d in enumerate(digits[:-1]):
                if d > current_max_v:
                    current_max_v = d
                    current_max_i = i
            assert current_max_i >= 0
            current_max_v_units = -1
            current_max_i_units = -1
            for j, d in enumerate(digits[current_max_i+1:]):
                if d > current_max_v_units:
                    current_max_v_units = d
                    current_max_i_units = i
            assert current_max_i_units >= 0
            value = current_max_v * 10 + current_max_v_units
            total += value
    print(f"Total is: {total}")


if __name__ == "__main__":
    main()
