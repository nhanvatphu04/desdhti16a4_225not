# app/des_controller.py
from des_algorithm import runIP, runFP, runExpansion, runGenKey, runSubstitution, runPermutation

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