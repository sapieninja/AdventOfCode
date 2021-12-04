# Code for custom input parsing from the input file. 
import fileinput 
def removeEmpties(inputList):
    return [line for line in inputList if line!=""]
def readlines(removeEnd = True):
    lines = fileinput.input()
    if removeEnd: lines = [line.strip() for line in lines]
    return lines
def readints():
    return list(map(int,readlines()))
def read():
    output = ""
    for x in readlines():
        output += x
    return output
def readSplittedLine(separator):
    text = read()
    return removeEmpties(text.split(separator))
def readSplittedIntLine():
    items = readSplittedLine(",")
    return list(map(int,items))
def readParagraphs():
    text = ""
    for line in readlines():
        text += line + "\n"
    sections = text.split("\n\n")
    return removeEmpties(sections)

