# fp.py
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
    """
    Thực hiện Final Permutation (FP) trên dữ liệu đầu vào 64-bit.

    Parameters:
    - data (str): Chuỗi nhị phân 64-bit cần hoán vị.

    Returns:
    - str: Chuỗi nhị phân 64-bit sau khi hoán vị theo FP_TABLE.
    """
    if len(data) != 64:
        raise ValueError("Input data must be a 64-bit binary string.")
    elif not all(bit in '01' for bit in data):
        raise ValueError("Input data must be a 64-bit binary string composed of 0s and 1s")
    permuted_data = ''.join(data[FP_TABLE[i] - 1] for i in range(64))
    return permuted_data