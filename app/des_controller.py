# app/des_controller.py
from des_algorithm import (runIP, runFP, runExpansion, runGenKey, runSubstitution, 
                         runPermutation, runEncryption, runDecryption, bin2hex, hex2bin, 
                         shiftLeft, validateNConvert)
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
    if not all(bit in '01' for bit in data):
        raise ValueError("Invalid binary input. Must contain only 0s and 1s.")
    return bin2hex(data)

def executeHex2Bin(data):
    if not all(c in '0123456789ABCDEFabcdef' for c in data):
        raise ValueError("Invalid hex input. Must contain only hex characters (0-9, A-F).")
    return hex2bin(data)

def executeShiftLeft(data, round_number):
    try:
        binary_data = validateNConvert(data, 28)
        if not isinstance(round_number, int) or round_number < 0 or round_number >= len(SHIFT_TABLE):
            raise ValueError(f'Round number must be an integer between 0 and {len(SHIFT_TABLE) - 1}.')
        shifts = SHIFT_TABLE[round_number]
        return shiftLeft(binary_data, shifts)
    except ValueError as e:
        raise ValueError(str(e))

def executeSplit(data):
    try:
        is_binary = all(bit in '01' for bit in data)
        is_hex = all(c in '0123456789ABCDEFabcdef' for c in data)
        if not (is_binary or is_hex):
            raise ValueError('Input must be either binary or hexadecimal.')
        binary_data = data if is_binary else hex2bin(data)
        if len(binary_data) % 2 != 0:
            raise ValueError('Input length must be even.')
        mid = len(binary_data) // 2
        left = binary_data[:mid]
        right = binary_data[mid:]
        return f'Left: {left}\nRight: {right}'
    except ValueError as e:
        raise ValueError(str(e))

def executePC1(key):
    try:
        binary_key = validateNConvert(key, 64)
        return ''.join(binary_key[PARITY_BIT_DROP_TABLE[i] - 1] for i in range(56))
    except ValueError as e:
        raise ValueError(str(e))

def executePC2(key):
    try:
        binary_key = validateNConvert(key, 56)
        return ''.join(binary_key[KEY_COMPRESSION_TABLE[i] - 1] for i in range(48))
    except ValueError as e:
        raise ValueError(str(e))

def executeXOR(a, b):
    try:
        is_a_binary = all(bit in '01' for bit in a)
        is_b_binary = all(bit in '01' for bit in b)
        is_a_hex = all(c in '0123456789ABCDEFabcdef' for c in a)
        is_b_hex = all(c in '0123456789ABCDEFabcdef' for c in b)
        if not ((is_a_binary or is_a_hex) and (is_b_binary or is_b_hex)):
            raise ValueError('Inputs must be either binary or hexadecimal.')
        if is_a_hex:
            a = hex2bin(a)
        if is_b_hex:
            b = hex2bin(b)
        if len(a) != len(b):
            raise ValueError("Both inputs must have the same length.")
        return ''.join('1' if bit_a != bit_b else '0' for bit_a, bit_b in zip(a, b))
    except Exception as e:
        raise ValueError(str(e))