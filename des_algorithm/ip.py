# des_algorithm/ip.py

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
    """
    Thực hiện Initial Permutation (IP) trên dữ liệu đầu vào 64-bit.

    Parameters:
    - data (str): Chuỗi nhị phân 64-bit cần hoán vị.

    Returns:
    - str: Chuỗi nhị phân 64-bit sau khi hoán vị theo IP_TABLE.
    """
    if len(data) != 64:
        raise ValueError("Input data must be a 64-bit binary string.")
    elif not all(bit in '01' for bit in data):
        raise ValueError("Input data must be a 64-bit binary string composed of 0s and 1s")
    permuted_data = ''.join(data[IP_TABLE[i] - 1] for i in range(64))
    return permuted_data