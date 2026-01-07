def main(): 
    with open("inputs/input2.txt", "r") as i_f:
        all_ = i_f.read()
    total = 0
    ranges_t = all_.split(",")
    ranges = []
    for range_t in ranges_t:
        range_ = range_t.split("-")
        min_, max_ = int(range_[0]), int(range_[1])
        for number in range(min_, max_+1):
            n_digits = len(str(number))
            is_silly = False
            for d in range(1, n_digits//2+1):
                if n_digits % d > 0:
                    continue
                pattern = str(number)[:d]
                if all([pattern == str(number)[i*d:(i+1)*d] for i in range(n_digits//d)]):
                    is_silly = True
                    break
            if is_silly:
                total += number
    print(f"Total is: {total}")


if __name__ == "__main__":
    main()
