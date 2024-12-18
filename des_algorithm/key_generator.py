# key_generator.py
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


from .utils import validateNConvert

def permute(key, table, n):
    return ''.join(key[table[i] - 1] for i in range(n))

def shiftLeft(key, shifts):
    if not all(bit in '01' for bit in key):
        raise ValueError("Input key must be a 28-bit binary string composed of 0s and 1s.")
    if len(key) == 0:
        raise ValueError("Input data cannot be an empty string.")
    if not isinstance(shifts, int) or shifts < 0:
        raise ValueError("Shifts must be a non-negative integer.")
    if shifts >= len(key):
        raise ValueError("Shifts must be less than the length of the data.")
    return key[shifts:] + key[:shifts]

def runGenKey(key, output_format='bin'):
    binary_key = validateNConvert(key, 64)
    key_56 = permute(binary_key, PARITY_BIT_DROP_TABLE, 56)
    
    left = key_56[:28]
    right = key_56[28:]
    
    round_keys = []
    for shift in SHIFT_TABLE:
        left = shiftLeft(left, shift)
        right = shiftLeft(right, shift)
        combined_key = left + right
        round_key = permute(combined_key, KEY_COMPRESSION_TABLE, 48)
        if output_format == 'hex':
            round_key = hex(int(round_key, 2))[2:].zfill(12)
        round_keys.append(round_key)
    
    return round_keys
