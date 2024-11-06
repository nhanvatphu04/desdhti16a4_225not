# permutation.py

# Bảng hoán vị P (Permutation P) trong DES
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
    """
    Thực hiện hoán vị P trên dữ liệu đầu vào 32-bit.

    Parameters:
    - data (str): Chuỗi nhị phân 32-bit cần hoán vị.

    Returns:
    - str: Chuỗi nhị phân 32-bit sau khi hoán vị theo P_TABLE.
    """
    if len(data) != 32:
        raise ValueError("Input data must be a 32-bit binary string.")
    elif not all(bit in '01' for bit in data):
        raise ValueError("Input data must be a 32-bit binary string composed of 0s and 1s")
    
    # Áp dụng hoán vị dựa trên P_TABLE
    permuted_data = ''.join(data[P_TABLE[i] - 1] for i in range(32))
    return permuted_data
