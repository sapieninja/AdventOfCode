# Code for custom input parsing from the input file. 
import fileinput 
def removeempties(inputList):
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
def readsplittedline(separator):
    text = read()
    return removeEmpties(text.split(separator))
def readsplittedintline():
    items = readSplittedLine(",")
    return list(map(int,items))
def readparagraphs():
    text = ""
    for line in readlines():
        text += line + "\n"
    sections = text.split("\n\n")
    sections = [section.split("\n") for section in sections]
    return removeEmpties(sections)

