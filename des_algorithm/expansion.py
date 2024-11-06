# expansion.py
EXPANSION_TABLE = [
    32, 1, 2, 3, 4, 5, 4, 5,
    6, 7, 8, 9, 8, 9, 10, 11,
    12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21,
    22, 23, 24, 25, 24, 25, 26, 27,
    28, 29, 28, 29, 30, 31, 32, 1
]

def runExpansion(data):
    """
    Thực hiện Expansion Permutation (E) để mở rộng 32-bit thành 48-bit.

    Parameters:
    - data (str): Chuỗi nhị phân 32-bit cần mở rộng.

    Returns:
    - str: Chuỗi nhị phân 48-bit sau khi mở rộng theo EXPANSION_TABLE.
    """
    if len(data) != 32:
        raise ValueError("Input data must be a 32-bit binary string.")
    elif not all(bit in '01' for bit in data):
        raise ValueError("Input data must be a 64-bit binary string composed of 0s and 1s")
    expanded_data = ''.join(data[EXPANSION_TABLE[i] - 1] for i in range(48))
    return expanded_data
