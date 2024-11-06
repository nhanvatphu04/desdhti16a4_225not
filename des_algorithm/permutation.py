# permutation.py
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
