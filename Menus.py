import UserConsoleInput as uci
from ConsoleOutputStyle import SetStyle

MENU_ENTERED_HEADER = "\n------[ {0} ]------"

class MenuOption:
    def __init__(self, name, func, style: str = "", desc: str = ""):
        self.name = name
        self.func = func
        self.style = style
        self.desc = desc
    
    def __str__(self):
        return self.name() if callable(self.name) else self.name

    def Execute(self):
        self.func()

class Menu:
    def __init__(self, name, options: list[MenuOption], showGlobalActions: bool = True):
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

def ChangeMenu(newMenu: Menu):
    global currentMenu
    global availableOptions
    currentMenu = newMenu
    availableOptions = currentMenu.GetAvailableActionsFromMenu()
    print(MENU_ENTERED_HEADER.format(currentMenu.name))   

def ExecuteAvailableAction(index: int):
    global availableOptions
    availableOptions[index].Execute()
    
def AvailableOptionSelection():
    global availableOptions
    optionIndex = uci.OptionSelection(availableOptions)
    if optionIndex < 0: return     
    ExecuteAvailableAction(optionIndex)


globalOptions: list[MenuOption] = []   # These can be called from any menu, unless the menu specifies that they are blocked.
currentMenu: Menu = None      # Current menu
availableOptions: list[MenuOption] = []  # All currently available actions (globalActions if they are not blocked + menu options of current menu)