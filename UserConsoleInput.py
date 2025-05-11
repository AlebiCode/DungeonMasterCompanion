import re
from ConsoleOutputStyle import SetStyle_InvalidInput, SetStyle_Default

#Rules:
#text surrounded by " " is treated as a whole word

NEW_WORD_SEPARATOR = " ."

inputs = []

def ObtainInputsFromString(userInput: str) -> list:
    #return " ".join(userInput.split()).split(NEW_WORD_SEPARATOR) #no regex method
    return re.sub(r'\s+', ' ', userInput).split(NEW_WORD_SEPARATOR)   #regex method

def AskUserForInputIfNone():
    global inputs
    if len(inputs) == 0:
        inputs = ObtainInputsFromString(input(">>> "))
    #print(f"New Inputted Words: {inputWords}")

def GetUserInput() -> str:
    global inputs
    AskUserForInputIfNone()
    return inputs.pop(0)

def UserInputInvalid(reason: str):
    global inputs
    SetStyle_InvalidInput()
    print(reason)
    SetStyle_Default()
    inputs.clear()
    
def GetFirstWord(string: str):
    return string.split(maxsplit= 1)[0]
    
#OLD----------------------------------------------

# def ObtainWordsFromInput(userInput: str) -> list:
#     strLen = len(userInput)
#     words = []
#     i = 0
#     while i < strLen:
#         #ignore white spaces
#         if userInput[i].isspace():
#             i += 1
#             continue
#         #text surrounded by " " is treated as a whole word
#         if userInput[i] == "\"":
#             j = i+1
#             validLiteralWord = False
#             while j < strLen:
#                 if userInput[j] == "\"" and (j+1 == strLen or userInput[j+1].isspace()):
#                     words.append(userInput[i+1:j].strip() if j - i > 1 else "")
#                     validLiteralWord = True
#                     break
#                 j += 1
#             if validLiteralWord == True:
#                 i = j+1
#                 continue
#         #get word normally
#         j = i+1
#         while j < strLen and not userInput[j].isspace():
#             j += 1
#         words.append(userInput[i:j])
#         i = j + 1
#     return words