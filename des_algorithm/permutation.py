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

from .utils import validateNConvert

def runPermutation(data):
    binary_data = validateNConvert(data, 32)
    permuted_data = ''.join(binary_data[P_TABLE[i] - 1] for i in range(32))
    return permuted_data
