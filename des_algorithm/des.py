from des_algorithm import runIP, runFP, runExpansion, runSubstitution, runPermutation, runGenKey
from .utils import validateNConvert

def runEncryption(plain_text, key):
    binary_text = validateNConvert(plain_text, 64)
    binary_key = validateNConvert(key, 64)
    
    round_keys = runGenKey(binary_key)
    permuted_text = runIP(binary_text)
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
    binary_text = validateNConvert(cipher_text, 64)
    binary_key = validateNConvert(key, 64)
    
    round_keys = runGenKey(binary_key)
    permuted_text = runIP(binary_text)
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
