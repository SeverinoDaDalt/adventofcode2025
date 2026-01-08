def main(): 
    total = 0
    matrix = []
    with open("inputs/input4.txt", "r") as i_f:
        for line in i_f:
            line = line.strip()
            matrix.append(line)
    len_x = len(matrix[0])
    len_y = len(matrix)
    for i in range(len_x):
        for j in range(len_y):
            if matrix[i][j] == ".":
                continue
            adjacent = 0
            if i-1 >= 0 and j-1 >= 0 and matrix[i-1][j-1] == "@":
                adjacent += 1
            if i-1 >= 0 and j+1 < len_y and matrix[i-1][j+1] == "@":
                adjacent += 1
            if i-1 >= 0 and matrix[i-1][j] == "@":
                adjacent += 1
            if i+1 < len_x and j-1 >= 0 and matrix[i+1][j-1] == "@":
                adjacent += 1
            if i+1 < len_x and j+1 < len_y and matrix[i+1][j+1] == "@":
                adjacent += 1
            if i+1 < len_x and matrix[i+1][j] == "@":
                adjacent += 1
            if j-1 >= 0 and matrix[i][j-1] == "@":
                adjacent += 1
            if j+1 < len_y and matrix[i][j+1] == "@":
                adjacent += 1
            if adjacent < 4:
                total += 1
    print(f"Total is: {total}")


if __name__ == "__main__":
    main()
