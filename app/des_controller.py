# app/des_controller.py
from des_algorithm import runIP, runFP, runExpansion, runGenKey, runSubstitution, runPermutation, runEncryption, runDecryption, bin2hex, hex2bin

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