import re

def read_input(file_path):
    lines = []
    with open(file_path) as f:
        r = re.compile(r'^(?P<min>\d+)-(?P<max>\d+) (?P<char>\w): (?P<pwd>\w+)$')
        for line in f:
            m = r.match(line)
            lines.append(
                {
                    "min": int(m.group('min')),
                    "max": int(m.group('max')),
                    "char": m.group('char'),
                    "pwd": m.group('pwd'),
                }
            )
    return lines

def main(data):
    valid_pwd_count = 0
    for d in data:
        # part 1
        # char_occ = d['pwd'].count(d['char']) 
        # if char_occ >= d['min'] and char_occ <= d['max']:
        #     valid_pwd_count += 1

        if (d['pwd'][d['min']-1] == d['char']) ^ (d['pwd'][d['max']-1] == d['char']):
            valid_pwd_count += 1
            print(d)
            print(d['pwd'][d['min']-1])
            print(d['pwd'][d['max']-1])
    print(valid_pwd_count)


if __name__ == "__main__":
    data = read_input("./input.txt")
    main(data)