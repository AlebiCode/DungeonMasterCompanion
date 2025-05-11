from colorama import Fore, Back, Style

currentStyle = ""

def ResetStyle():
    global currentStyle
    currentStyle = Style.RESET_ALL
    print(Style.RESET_ALL, end= "", sep= "")

def SetStyle(fore = Fore.WHITE, back = Back.BLACK, style = Style.NORMAL):
    fullStyle = fore + back + style
    global currentStyle
    if(currentStyle != fullStyle):
        currentStyle = fullStyle
        print(fullStyle, end= "", sep= "")

def SetStyle_Default():
    ResetStyle()

def SetStyle_MainTitle():
    SetStyle(Fore.GREEN, style= Style.BRIGHT)

def SetStyle_LessImportant():
    SetStyle(Fore.BLACK, style= Style.BRIGHT)

def SetStyle_InvalidInput():
    SetStyle(Fore.RED, style= Style.BRIGHT)