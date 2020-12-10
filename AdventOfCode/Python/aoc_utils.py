# Code for custom input parsing from the input file. 
# It will allow for autodownloading of the correct input file but only if the input file does not already exist.
import os.path
from __main__ import __file__
day = os.path.basename(__file__)[0:2]
path = os.path.dirname(__file__)
input_path = path[0:-7] + "/Inputs/" + day + ".txt"
if(not os.path.isfile(input_path)): #downloads the file if (and only if) it does not exist
    os.system(f"cd {path};cd ..;advent")
def removeEmpties(inputList):
    return [line for line in inputList if line!=""]
def readlines(removeEnd = True):
    with open(input_path, "r") as file:
        lines = file.readlines()
    if removeEnd: lines = [line.strip() for line in lines]
    return removeEmpties(lines)
def readSplittedLine(separator):
    with open(input_path,"r") as file:
        text = file.read()
    return removeEmpties(text.split(separator))
def readSplittedIntLine(separator):
    items = readSplittedLine(separator)
    return map(int,items)
def readParagraphs():
    with open(input_path,"r") as file:
        text = file.read()
    sections = text.split("\n\n")
    sections = [section.replace("\n", " ") for section in sections]
    return removeEmpties(sections)
def readints():
    return [int(line) for line in readlines()]
def readall():
    with open(input_path,"r") as file:
        text = file.read()
    return text