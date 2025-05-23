import re
from ConsoleOutputStyle import SetStyle_InvalidInput, SetStyle_Default

#Rules:
#text surrounded by " " is treated as a whole word

NEW_WORD_SEPARATOR = " ."

inputs = []

def ObtainInputsFromString(userInput: str) -> list:
    #return " ".join(userInput.split()).split(NEW_WORD_SEPARATOR) #no regex method
    return re.sub(r'\s+', ' ', userInput.strip()).split(NEW_WORD_SEPARATOR)   #regex method

def AskUserForInputIfNone():
    global inputs
    if len(inputs) == 0:
        inputs = ObtainInputsFromString(input(">>> "))
    #print(f"New Inputted Words: {inputs}")

def GetUserInput(optionalPrint: str = "") -> str:
    if(optionalPrint != ""):
        print(optionalPrint)
    AskUserForInputIfNone()
    global inputs
    return inputs.pop(0)

def GetUserInputIndex(optionalPrint: str = "") -> str:
    userInput = GetFirstWordOfString(GetUserInput(optionalPrint))
    if userInput.isdigit() == False:
        return 0
    return int(userInput)

def GetUserInputIndexes(optionalPrint: str = "", maxAmount = 999) -> str:
    userInputWords = GetWordsOfString(GetUserInput(optionalPrint))
    output: list[int] = []
    for word in userInputWords:
        if word.isdigit() == True:
            output.append(int(word))
            if(len(output) >= maxAmount):
                break
    return output

def OptionSelection(options) -> int:
    if len(options) == 0: return -1
    for i in range(len(options)): print(f"[{i}] {str(options[i])}")
    index = GetUserInputIndex()
    if index < 0:
        UserInputInvalid("No available choice found!")   
        return -1
    elif index >= len(options):
        UserInputInvalid(f"\"{index}\" is out range!")
        return -1
    #TODO: POSSIBLE TO ADD ACTION NAME CHECK!!
    return index

def GetFirstWordOfString(string: str):
    if len(string) == 0: return ""
    return string.split(maxsplit= 1)[0]
    
def GetWordsOfString(string: str):
    return string.split()

def UserInputInvalid(reason: str):
    global inputs
    SetStyle_InvalidInput()
    print(reason)
    SetStyle_Default()
    inputs.clear()
    

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