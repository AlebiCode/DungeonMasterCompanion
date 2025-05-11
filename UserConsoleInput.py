from ConsoleOutputStyle import SetStyle_InvalidInput, SetStyle_Default

#Rules:
#text surrounded by " " is treated as a whole word

inputWords = []

def ObtainWordsFromInput(userInput: str) -> list:
    strLen = len(userInput)
    words = []
    i = 0
    while i < strLen:
        #ignore white spaces
        if userInput[i].isspace():
            i += 1
            continue
        #text surrounded by " " is treated as a whole word
        if userInput[i] == "\"":
            j = i+1
            validLiteralWord = False
            while j < strLen:
                if userInput[j] == "\"" and (j+1 == strLen or userInput[j+1].isspace()):
                    words.append(userInput[i+1:j].strip() if j - i > 1 else "")
                    validLiteralWord = True
                    break
                j += 1
            if validLiteralWord == True:
                i = j+1
                continue
        #get word normally
        j = i+1
        while j < strLen and not userInput[j].isspace():
            j += 1
        words.append(userInput[i:j])
        i = j + 1
    return words

def AskUserForInputIfNone():
    global inputWords
    if len(inputWords) == 0:
        inputWords = ObtainWordsFromInput(input(">>> ").strip())
    #print(f"New Inputted Words: {inputWords}")

def GetUserInputWord() -> str:
    global inputWords
    AskUserForInputIfNone()
    return inputWords.pop(0)

# def GetUserInputFull():
#     global inputWords
#     AskUserForInputIfNone()
#     output = inputWords.copy()
#     inputWords.clear()
#     return output

def UserInputInvalid(reason: str):
    global inputWords
    SetStyle_InvalidInput()
    print(reason)
    SetStyle_Default()
    inputWords.clear()