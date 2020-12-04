
def read_input(file_path):
    lines = []
    with open(file_path) as f:
        for line in f:
            lines.append([c for c in line.strip()])
    return lines

def main(data, slopes):
    map_width = len(data[0])
    map_height = len(data)

    print(map_width, map_height)

    res = 1
    for slope in slopes:
        row, col = 0, 0
        tree_count = 0
        while row < (map_height-1):
            row += slope[1]
            col = (col + slope[0]) % map_width
            # print(data[row])
            # print("row: {}, col: {}".format(row, col))
            if data[row][col] == '#':
                tree_count += 1
        print("{} tree_count: {}".format(slope, tree_count))
        res *= tree_count
    print("res: {}".format(res))




if __name__ == "__main__":
    data = read_input("./input.txt")
    # main(data, [(3,1)])
    main(data, [(1,1), (3,1), (5,1), (7,1), (1,2)]) 