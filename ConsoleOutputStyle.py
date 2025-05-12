from colorama import Fore, Back, Style

DEFAULT_STYLE_SYMBOL = ""

STYLE_LESS_IMPORTANT = Fore.BLACK + Style.BRIGHT
STYLE_INVALID = Fore.RED + Style.BRIGHT
STYLE_MAIN_TITLE = Fore.GREEN + Style.BRIGHT


currentStyle = ""


def SetStyle(style: str):
    global currentStyle
    if(currentStyle == style):
        return
    currentStyle = style
    if style == DEFAULT_STYLE_SYMBOL:
        print(Style.RESET_ALL, end= "", sep= "")
    else:
        print(currentStyle, end= "", sep= "")

def ResetStyle():
    SetStyle(DEFAULT_STYLE_SYMBOL)

def SetStyle_Default():
    ResetStyle()
    
def SetStyle_InvalidInput():
    SetStyle(STYLE_INVALID)

def SetStyle_MainTitle():
    SetStyle(STYLE_MAIN_TITLE)


# def SetStyle(fore = Fore.WHITE, back = Back.BLACK, style = Style.NORMAL):
#     fullStyle = fore + back + style
#     global currentStyle
#     if(currentStyle != fullStyle):
#         if fullStyle == "":
#             ResetStyle()
#         else:
#             currentStyle = fullStyle
#             print(fullStyle, end= "", sep= "")