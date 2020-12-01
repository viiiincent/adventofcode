
def read_input(file_path, cast):
    lines = []
    with open(file_path) as f:
        lines = [cast(line.strip()) for line in f]
    return lines

def main(data):
    # print(data)
    i = 0
    while i < len(data)-1:
        # print("i: {}".format(data[i]))
        j = 0
        while j < len(data)-1:
            # print("\tj: {}".format(data[j]))
            k = 0
            while k < len(data)-1:
                # print("\t\tk: {}".format(data[k]))
                if data[i] + data[j] + data[k] == 2020:
                    print("data[i]*data[j]*data[k]: {}".format(data[i]*data[j]*data[k]))
                    exit()
                k += 1
            j += 1
        i += 1

if __name__ == "__main__":
    data = read_input("./input.txt", int)
    main(data)