def n_plus_up_to_m(n,m):
    assert m >= n, f"n: {n}; m: {m}"
    return (m**2 + m)//2 - ((n-1)**2 + n-1)//2 


def main(): 
    with open("inputs/input2.txt", "r") as i_f:
        all_ = i_f.read()
    total = 0
    ranges_t = all_.split(",")
    ranges = []
    for range_t in ranges_t:
        range_ = range_t.split("-")
        min_, max_ = int(range_[0]), int(range_[1])
        min_digits = len(str(min_))
        max_digits = len(str(max_))
        for n_digits in range(min_digits, max_digits + 1):
            if n_digits % 2 == 1:
                continue
            half_size = n_digits // 2
            if n_digits == min_digits:
                half0 = int(str(min_)[:half_size])
                half1 = int(str(min_)[half_size:])
                if half0 >= half1:
                    max_lower_half = half0
                else:
                    max_lower_half = half0 + 1
            else:
                max_lower_half = int("1" + "0"*(half_size-1))
            if n_digits == max_digits:
                half0 = int(str(max_)[:half_size])
                half1 = int(str(max_)[half_size:])
                if half0 <= half1:
                    min_higher_half = half0
                else:
                    min_higher_half = half0 - 1
            else:
                min_higher_half = int("9"*half_size)
            if max_lower_half > min_higher_half:
                continue
            half_sub_total = n_plus_up_to_m(max_lower_half, min_higher_half)
            sub_total = half_sub_total * 10**half_size + half_sub_total
            total += sub_total
    print(f"Total is: {total}")


if __name__ == "__main__":
    main()
