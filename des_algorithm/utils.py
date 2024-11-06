# This code is contributed by Aditya Jain

# Hexadecimal to binary conversion
def hex2bin(s):
	s = s.upper()
	mp = {'0': "0000",
		'1': "0001",
		'2': "0010",
		'3': "0011",
		'4': "0100",
		'5': "0101",
		'6': "0110",
		'7': "0111",
		'8': "1000",
		'9': "1001",
		'A': "1010",
		'B': "1011",
		'C': "1100",
		'D': "1101",
		'E': "1110",
		'F': "1111"}
	bin = ""
	for i in range(len(s)):
		bin = bin + mp[s[i]]
	return bin

# Binary to hexadecimal conversion
def bin2hex(s):
	if any(c not in '01' for c in s):
		return "Invalid binary input. Please enter only '0' or '1'."
	while len(s) % 4 != 0:
		s = '0' + s
	mp = {"0000": '0',
		"0001": '1',
		"0010": '2',
		"0011": '3',
		"0100": '4',
		"0101": '5',
		"0110": '6',
		"0111": '7',
		"1000": '8',
		"1001": '9',
		"1010": 'A',
		"1011": 'B',
		"1100": 'C',
		"1101": 'D',
		"1110": 'E',
		"1111": 'F'}
	hex = ""
	for i in range(0, len(s), 4):
		ch = ""
		ch = ch + s[i]
		ch = ch + s[i + 1]
		ch = ch + s[i + 2]
		ch = ch + s[i + 3]
		hex = hex + mp[ch]

	return hex

# Binary to decimal conversion (accepts string input)
def bin2dec(binary):
    return int(binary, 2)

# Decimal to binary conversion with fixed length
def dec2bin(num, length=4):
    res = bin(num)[2:]
    return res.zfill(length)