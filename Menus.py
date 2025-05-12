import UserConsoleInput as uci
from ConsoleOutputStyle import SetStyle

MENU_ENTERED_HEADER = "\n------[ {0} ]------"

class MenuOption:
    def __init__(self, name: str, func, style: str = "", desc: str = ""):
        self.name = name
        self.func = func
        self.style = style
        self.desc = desc
    
    def __str__(self):
        return self.name
    
    def Execute(self):
        self.func()

class Menu:
    def __init__(self, name: str, options: list[MenuOption], showGlobalActions: bool = True):
        self.name = name
        self.options = options
        self.showGlobalActions = showGlobalActions
        
    def GetAvailableActionsFromMenu(self) -> list[MenuOption]:
        if(self.showGlobalActions):
            global globalOptions
            return globalOptions + self.options
        return self.options

def SetGlobalMenuOptions(options: list[MenuOption]):
    global globalOptions
    globalOptions = options

def PrintAvailableActions():
    print()
    i = 0
    global globalOptions
    global currentMenu
    global availableOptions
    for option in availableOptions:
        SetStyle(option.style)
        print(f"[{i}] {option.name}")
        i += 1

def ChangeMenu(newMenu: Menu):
    global currentMenu
    global availableOptions
    currentMenu = newMenu
    availableOptions = currentMenu.GetAvailableActionsFromMenu()
    print(MENU_ENTERED_HEADER.format(currentMenu.name))   

def ExecuteAvailableAction(index: int):
    global availableOptions
    availableOptions[index].Execute()
    
def AvailableActionSelection():
    PrintAvailableActions()
    actionSelection = uci.GetFirstWordOfString(uci.GetUserInput())
    if actionSelection.isdigit():
        index = int(actionSelection)
        global availableOptions
        if index >= len(availableOptions):
            uci.UserInputInvalid(f"\"{index}\" is out range!")
            return
        ExecuteAvailableAction(index)
        return
    else:
        #TODO: POSSIBLE TO ADD ACTION NAME CHECK!!
        pass
    uci.UserInputInvalid("No available choice found!")        


globalOptions: list[MenuOption] = []   # These can be called from any menu, unless the menu specifies that they are blocked.
currentMenu: Menu = None      # Current menu
availableOptions: list[MenuOption] = []  # All currently available actions (globalActions if they are not blocked + menu options of current menu)