def main(): 
    total = 0
    ranges = []
    with open("inputs/input5.txt", "r") as i_f:
        for line in i_f:
            line = line.strip()
            if not line:
                break
            range_ = line.split("-")
            range_ = [int(range_[0]), int(range_[1])]
            fused = []
            for r in ranges:
                if (r[0] <= range_[0] <= r[1]) \
                        or (r[0] <= range_[1] <= r[1]) \
                        or (range_[0] <= r[0] <= r[1] <= range_[1]):
                    fused.append(r)
                    range_[0] = min(range_[0], r[0])
                    range_[1] = max(range_[1], r[1])
            for r in fused:
                ranges.remove(r)
            ranges.append(range_)
    for range_ in ranges:
        assert range_[1] >= range_[0], range_
        total += range_[1] - range_[0] + 1
    print(f"Total is: {total}")


if __name__ == "__main__":
    main()
