# app/des_controller.py
from des_algorithm import runIP, runFP, runExpansion, runGenKey, runSubstitution, runPermutation, runEncryption, runDecryption, bin2hex, hex2bin, shift_left
from des_algorithm import SHIFT_TABLE, PARITY_BIT_DROP_TABLE, KEY_COMPRESSION_TABLE

def executeIP(data):
    return runIP(data)

def executeFP(data):
    return runFP(data)

def executeExpansion(data):
    return runExpansion(data)

def executeGenKey(data):
    return runGenKey(data)

def executeSubstitution(data):
    return runSubstitution(data)

def executePermutation(data):
    return runPermutation(data)

def executeEncryption(data, key):
    return runEncryption(data, key)

def executeDecryption(data, key):
    return runDecryption(data, key)

def executeBin2Hex(data):
    return bin2hex(data)

def executeHex2Bin(data):
    return hex2bin(data)

def executeShiftLeft(data, round_number):
    if not isinstance(data, str):
        raise TypeError('Input data must be a string.')
    if not all(bit in '01' for bit in data):
        raise ValueError('Input data must be a binary string composed of 0s and 1s.')
    if len(data) != 28:
        raise ValueError('Input data must be a 28-bit binary string.')
    if not isinstance(round_number, int) or round_number < 0 or round_number >= len(SHIFT_TABLE):
        raise ValueError(f'Round number must be an integer between 0 and {len(SHIFT_TABLE) - 1}.')
    shifts = SHIFT_TABLE[round_number]
    return shift_left(data, shifts)

def executeSplit(data):
    if not isinstance(data, str):
        raise TypeError('Input data must be a string.')
    if len(data) == 0:
        raise ValueError('Input data cannot be an empty string.')
    if not all(bit in '01' for bit in data):
        raise ValueError('Input data must be a binary string composed of 0s and 1s.')
    midpoint = len(data) // 2
    left = data[:midpoint]
    right = data[midpoint:]
    left_result = str('Left: ' + left)
    right_result = str('Right: ' + right)
    result = left_result + '\n' + right_result
    return result

def executePC1(key):
    if len(key) != 64:
        raise ValueError('Input key must be a 64-bit binary string.')
    return ''.join(key[PARITY_BIT_DROP_TABLE[i] - 1] for i in range(56))

def executePC2(key):
    if len(key) != 56:
        raise ValueError('Input key must be a 56-bit binary string.')
    return ''.join(key[KEY_COMPRESSION_TABLE[i] - 1] for i in range(48))

def executeXOR(a, b):
    if len(a) != len(b):
        raise ValueError("Both binary strings must have the same length.")
    result = ''.join('1' if bit_a != bit_b else '0' for bit_a, bit_b in zip(a, b))
    return result