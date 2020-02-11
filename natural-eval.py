"""
ATENTION: Ce programme est expérimental et va provoquer un bug à coup sûr
Ne l'utilisez que pour vérifier vos valeurs

Il permet d'exécuter les programmes en langage naturel du site Kwyk.fr
Et donne les valeurs de chaque variable à chaque étape.
"""

import re
import functools

data = ""

if len(data) == 0:
    inp = input("> ")
    while inp != "":
        data += inp + "\n"
        inp = input("> ")

print("\n======\n")
mainData = {}
inLoop = -1

def isint(var):
    try:
        int(var)
        return True
    except:
        return False

def decoupe(string):
    if len(string) == 1: return string
    string = string.replace(" ", "").replace("\\times", "×")
    string = string[:int(len(string)/3)]
    return string

def lookup(string):
    global mainData

    try:
        return float(string)
    except:
        try:
            return mainData[string]
        except:
            if string == "n":
                n = input("Merci de renseigner l'entier n: ")
                if isint(n):
                    return int(n)
                else:
                    print("n est invalide, ce devrait être un entier !")
                    exit(-1)
            else:
                print("Lookup impossible:", string)
                exit(-1)

def reducer(operator):
    if operator == "+":
        return lambda a, b: a + b
    elif operator == "*":
        return lambda a, b: a * b
    else:
        print("Error: Unsupported")
        exit(-1)

def evaluate(string, u = 0, S = 0):
    global mainData
    
    string = string \
            .replace("×", "*") \
            .replace(",", ".")
    try:
        mode = "+"
        if "*" in string: mode = "*"
        splitted = list(map(lookup, re.split(r"\*|\+", string)))
        reduced = functools.reduce(reducer(mode), splitted)
        return reduced
    except re.error:
        return eval(string)
    return string

endLoopValue = -1
endLoopVariable = -1
splittedData = data.split("\n")
end = len(splittedData)
i = 0
while i < end:
    line = splittedData[i]
    if " ← " in line:
        s = line.split(" ← ")
        variable = decoupe(s[0])
        value = evaluate(decoupe(s[1]))
        mainData[variable] = value
        print(variable, "=", value)
    if line.startswith("Pour"):
        print("Entered a loop!")
        inLoop = i + 1
        s = line.split(" ")
        variable = decoupe(s[1])
        firstValue = evaluate(decoupe(s[4]))
        endLoopVariable = variable
        endLoopValue = evaluate(decoupe(s[6]))
        mainData[variable] = firstValue
        print(variable, "=", firstValue)

    i += 1

    if inLoop > -1:
        if i >= end:
            i = inLoop
            if mainData[endLoopVariable] >= endLoopValue:
                inLoop = -1
            mainData[endLoopVariable] += 1
            print(endLoopVariable, "=", mainData[endLoopVariable])
