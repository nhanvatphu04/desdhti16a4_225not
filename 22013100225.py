
def hex2bin(s):
    s = s.upper()
    mp = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
          '4': '0100', '5': '0101', '6': '0110', '7': '0111',
          '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
          'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    return ''.join(mp[ch] for ch in s)

def bin2hex(s):
    while len(s) % 4 != 0:
        s = '0' + s
    mp = {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
          '0100': '4', '0101': '5', '0110': '6', '0111': '7',
          '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
          '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
    return ''.join(mp[s[i:i + 4]] for i in range(0, len(s), 4))

def bin2dec(binary):
    return int(binary, 2)

def dec2bin(num, length=4):
    res = bin(num)[2:]
    return res.zfill(length)

S_BOXES = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]
]

def runSubstitution(data):
    if len(data) != 48:
        raise ValueError('Input data must be a 48-bit binary string')
    elif not all(bit in '01' for bit in data):
        raise ValueError('Input data must be a 48-bit binary string composed of 0s and 1s')

    output_32bit = ''
    for i in range(8):
        six_bits = data[i*6:(i+1)*6]
        row = bin2dec(six_bits[0] + six_bits[5])
        col = bin2dec(six_bits[1:5])
        sbox_value = S_BOXES[i][row][col]
        output_32bit += dec2bin(sbox_value, 4)

    return output_32bit


P_TABLE = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

def runPermutation(data):
    if len(data) != 32:
        raise ValueError('Input data must be a 32-bit binary string.')
    elif not all(bit in '01' for bit in data):
        raise ValueError('Input data must be a 32-bit binary string composed of 0s and 1s')

    permuted_data = ''.join(data[P_TABLE[i] - 1] for i in range(32))
    return permuted_data

PARITY_BIT_DROP_TABLE = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

KEY_COMPRESSION_TABLE = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

SHIFT_TABLE = [
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]

def permute(key, table, n):
    return ''.join(key[table[i] - 1] for i in range(n))

def shift_left(key, shifts):
    if not all(bit in '01' for bit in key):
        raise ValueError("Input key must be a 28-bit binary string composed of 0s and 1s.")
    if len(key) == 0:
        raise ValueError("Input data cannot be an empty string.")
    if not isinstance(shifts, int) or shifts < 0:
        raise ValueError("Shifts must be a non-negative integer.")
    if shifts >= len(key):
        raise ValueError("Shifts must be less than the length of the data.")
    return key[shifts:] + key[:shifts]

def runGenKey(key):
    if len(key) != 64:
        raise ValueError("Input key must be a 64-bit binary string.")
    elif not all(bit in '01' for bit in key):
        raise ValueError("Input data must be a 64-bit binary string composed of 0s and 1s")
    
    key_56 = permute(key, PARITY_BIT_DROP_TABLE, 56)
    
    left = key_56[:28]
    right = key_56[28:]
    
    round_keys = []
    for shift in SHIFT_TABLE:
        left = shift_left(left, shift)
        right = shift_left(right, shift)
        combined_key = left + right
        round_key = permute(combined_key, KEY_COMPRESSION_TABLE, 48)
        round_keys.append(round_key)
    
    return round_keys


IP_TABLE = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

def runIP(data):
    if len(data) != 64:
        raise ValueError('Input data must be a 64-bit binary string.')
    elif not all(bit in '01' for bit in data):
        raise ValueError('Input data must be a 64-bit binary string composed of 0s and 1s')
    permuted_data = ''.join(data[IP_TABLE[i] - 1] for i in range(64))
    return permuted_data

FP_TABLE = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

def runFP(data):
    if len(data) != 64:
        raise ValueError('Input data must be a 64-bit binary string.')
    elif not all(bit in '01' for bit in data):
        raise ValueError('Input data must be a 64-bit binary string composed of 0s and 1s')
    permuted_data = ''.join(data[FP_TABLE[i] - 1] for i in range(64))
    return permuted_data


EXPANSION_TABLE = [
    32, 1, 2, 3, 4, 5, 4, 5,
    6, 7, 8, 9, 8, 9, 10, 11,
    12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21,
    22, 23, 24, 25, 24, 25, 26, 27,
    28, 29, 28, 29, 30, 31, 32, 1
]

def runExpansion(data):
    if len(data) != 32:
        raise ValueError('Input data must be a 32-bit binary string.')
    elif not all(bit in '01' for bit in data):
        raise ValueError('Input data must be a 64-bit binary string composed of 0s and 1s')
    expanded_data = ''.join(data[EXPANSION_TABLE[i] - 1] for i in range(48))
    return expanded_data

def runEncryption(plain_text, key):
    if len(plain_text) != 64 or len(key) != 64:
        raise ValueError('Input and key must be 64-bit binary strings.')
    
    round_keys = runGenKey(key)
    permuted_text = runIP(plain_text)
    left, right = permuted_text[:32], permuted_text[32:]

    for i in range(16):
        expanded_right = runExpansion(right)
        xored = ''.join(['1' if expanded_right[j] != round_keys[i][j] else '0' for j in range(48)])
        substituted = runSubstitution(xored)
        permuted = runPermutation(substituted)
        new_right = ''.join(['1' if left[j] != permuted[j] else '0' for j in range(32)])
        left, right = right, new_right

    final_text = runFP(right + left)
    return final_text

def runDecryption(cipher_text, key):
    if len(cipher_text) != 64 or len(key) != 64:
        raise ValueError('Input and key must be 64-bit binary strings.')

    round_keys = runGenKey(key)
    permuted_text = runIP(cipher_text)
    left, right = permuted_text[:32], permuted_text[32:]

    for i in range(15, -1, -1):
        expanded_right = runExpansion(right)
        xored = ''.join(['1' if expanded_right[j] != round_keys[i][j] else '0' for j in range(48)])
        substituted = runSubstitution(xored)
        permuted = runPermutation(substituted)
        new_right = ''.join(['1' if left[j] != permuted[j] else '0' for j in range(32)])
        left, right = right, new_right

    final_text = runFP(right + left)
    return final_text

# Ví dụ mã hoá
plain_text = '12f073a11025ecc7'
key = '22103100225c16a4'

plain_text_bin = hex2bin(plain_text)
key_bin = hex2bin(key)
cipher_text_bin = runEncryption(plain_text_bin, key_bin)

print('\nEncryption')
print('Plain text (hexadecimal):', plain_text)
print('Plain text (binary):', plain_text_bin)
print('Cipher text (hexadecimal):', bin2hex(cipher_text_bin))
print('Cipher text (binary):', cipher_text_bin)

# Ví dụ giải mã
cipher_text = '429c854fe454bd8a'
cipher_text_bin = hex2bin(cipher_text)

decrypted_text_bin = runDecryption(cipher_text_bin, key_bin)
decrypted_text_hex = bin2hex(decrypted_text_bin)

print('\nDecryption')
print('Cipher text (hexadecimal):', cipher_text)
print('Cipher text (binary):', cipher_text_bin)
print('Decrypted text (hexadecimal):', decrypted_text_hex)
print('Decrypted text (binary):', decrypted_text_bin)