# Code for custom input parsing from the input file. 
import fileinput 
def removeEmpties(inputList):
    return [line for line in inputList if line!=""]
def readLines(removeEnd = True) -> list[str]:
    lines = fileinput.input()
    if removeEnd: lines = [line.strip() for line in lines]
    return lines
def numericGrid(separator = ","):
    splittedLines = readSplittedLines()
    return [list(map(int,x)) for x in splittedLines]
def readInts():
    return list(map(int,readLines()))
def read():
    output = ""
    for x in readLines():
        output += x
    return output
def readSplittedLine(separator):
    text = read()
    return removeEmpties(text.split(separator))
def readSplittedIntLine():
    items = readSplittedLine(",")
    return list(map(int,items))
def readSplittedLines(separator=",") -> list[list[str]]:
    lines = readLines()
    toReturn : list[list[str]] = [line.split(separator) for line in lines]
    return toReturn
def readParagraphs():
    text = ""
    for line in readLines():
        text += line + "\n"
    sections = text.split("\n\n")
    sections = [removeEmpties(section.split("\n")) for section in sections]
    return removeEmpties(sections)
def readIntParagraphs() -> list[list[int]]:
    paragraphs = readParagraphs()
    toReturn = []
    for paragraph in paragraphs:
        toReturn.append(list(map(int,paragraph)))
    return toReturn
#evil demon function that is kind of useful
def convInt(into): 
    try:
        return int(into)
    except:
        return [convInt(i) for i in into]
