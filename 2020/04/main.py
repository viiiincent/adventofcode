import re

def read_input(file_path):
	passports = []
	with open(file_path) as f:
		p = {}
		for line in f:
			# print(line)
			if line == "\n":
				passports.append(p)
				p = {}
				continue

			data = line.strip().split(' ')
			for d in data:
				key, val = d.split(":")
				p[key] = val
	passports.append(p)
	return passports

def is_valid_byr(byr):
	byr = int(byr)
	return byr >= 1920 and byr <= 2002

def is_valid_iyr(iyr):
	iyr = int(iyr)
	return iyr >= 2010 and iyr <= 2020

def is_valid_eyr(eyr):
	eyr = int(eyr)
	return eyr >= 2020 and eyr <= 2030

def is_valid_hgt(hgt):
	m = re.match(r'^(\d+)(cm|in)$', hgt)
	if m:
		if m.group(2) == 'cm':
			return int(m.group(1)) >= 150 and int(m.group(1)) <= 193
		elif m.group(2) == 'in':	
			return int(m.group(1)) >= 59 and int(m.group(1)) <= 76
	return False

def is_valid_hcl(hcl):
	return re.match(r'^#([0-9]|[a-f]){6}$', hcl)

def is_valid_ecl(ecl):
	return re.match(r'amb|blu|brn|gry|grn|hzl|oth', ecl)

def is_valid_pid(pid):
	return re.match(r'^\d{9}$', pid)

def main(data):
	valid_count = 0
	for passport in data:
		# PART 1
		# if  len(passport) == 8 or \
		# 	len(passport) == 7 and 'cid' not in passport:
		# 	valid_count += 1

		# PART 2
		if 'byr' not in passport or not is_valid_byr(passport['byr']):
			continue
		if 'iyr' not in passport or not is_valid_iyr(passport['iyr']):
			continue
		if 'eyr' not in passport or not is_valid_eyr(passport['eyr']):
			continue
		if 'hgt' not in passport or not is_valid_hgt(passport['hgt']):
			continue
		if 'hcl' not in passport or not is_valid_hcl(passport['hcl']):
			continue
		if 'ecl' not in passport or not is_valid_ecl(passport['ecl']):
			continue
		if 'pid' not in passport or not is_valid_pid(passport['pid']):
			continue

		valid_count += 1
	print(valid_count)

if __name__ == "__main__":
	data = read_input("./input.txt")
	main(data)