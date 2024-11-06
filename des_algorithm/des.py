from des_algorithm import runIP, runFP, runExpansion, runSubstitution, runPermutation, runGenKey

def runEncryption(plain_text, key):
    if len(plain_text) != 64 or len(key) != 64:
        raise ValueError('Input and key must be 64-bit binary strings.')
    
    round_keys = runGenKey(key)
    permuted_text = runIP(plain_text)
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
    if len(cipher_text) != 64 or len(key) != 64:
        raise ValueError('Input and key must be 64-bit binary strings.')

    round_keys = runGenKey(key)
    permuted_text = runIP(cipher_text)
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
