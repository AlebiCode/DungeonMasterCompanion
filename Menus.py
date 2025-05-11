import UserConsoleInput as uci
from ConsoleOutputStyle import SetStyle_LessImportant, SetStyle_Default

MENU_ENTERED_HEADER = "\n------[ {0} ]------"

class MenuOption:
    def __init__(self, name: str, func, desc: str = ""):
        self.name = name
        self.func = func
        self.desc = desc
        
    def Execute(self):
        self.func()

class Menu:
    # def __init__(self, name, actions):
    #     self.name = name
    #     self.actions = actions
    def __init__(self, name: str, options: tuple[MenuOption], showGlobalActions: bool = True):
        self.name = name
        self.options = options
        self.showGlobalActions = showGlobalActions
        
    def GetAvailableActionsFromMenu(self) -> tuple[MenuOption]:
        if(self.showGlobalActions):
            global globalOptions
            return globalOptions + self.options
        return self.options

def SetGlobalMenuOptions(options: tuple[MenuOption]):
    global globalOptions
    globalOptions = options

def PrintAvailableActions():
    print()
    i = 0
    global globalOptions
    global currentMenu
    global availableOptions
    usedGlobalActionsLen = 0 if currentMenu.showGlobalActions == False else len(globalOptions)
    if usedGlobalActionsLen > 0: SetStyle_LessImportant()
    for action in availableOptions:
        print(f"[{i}] {action.name}")
        i += 1
        if i == usedGlobalActionsLen: SetStyle_Default()

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
    actionSelection = uci.GetFirstWord(uci.GetUserInput())
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


globalOptions: tuple[MenuOption] = ()   # These can be called from any menu, unless the menu specifies that they are blocked.
currentMenu: Menu = None      # Current menu
availableOptions: tuple[MenuOption] = ()  # All currently available actions (globalActions if they are not blocked + menu options of current menu)