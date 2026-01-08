def main(): 
    total = 0
    ranges = []
    with open("inputs/input5.txt", "r") as i_f:
        for line in i_f:
            line = line.strip()
            if not line:
                break
            range_ = line.split("-")
            ranges.append([int(range_[0]), int(range_[1])])
        for line in i_f:
            value = int(line.strip())
            found = False
            for range_ in ranges:
                if range_[0] <= value <= range_[1]:
                    found = True
                    break
            if found:
                total += 1
    print(f"Total is: {total}")


if __name__ == "__main__":
    main()
