import UserConsoleInput as uci
from ConsoleOutputStyle import SetStyle_LessImportant, SetStyle_Default

class Action:
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
    def __init__(self, name: str, *actions: Action):
        self.name = name
        self.actions = actions


def ShowMenus():
    print("Not yet, amigo!")

def PrintActions():
    print()
    i = 0
    global baseActions
    if len(baseActions) > 0: SetStyle_LessImportant()
    for action in availableActions:
        print(f"[{i}] {action.name}")
        i += 1
        if i == len(baseActions): SetStyle_Default()

def ChangeMenu(newMenu: Menu):
    global currentMenu
    global availableActions
    currentMenu = newMenu
    availableActions = baseActions + newMenu.actions    

def ExecuteAvailableAction(index: int):
    availableActions[index].Execute()
    
def AvailableActionSelection():
    PrintActions()
    actionSelection = uci.GetUserInputWord()
    if actionSelection.isdigit():
        index = int(actionSelection)
        if index >= len(availableActions):
            uci.UserInputInvalid(f"\"{index}\" is out range!")
            return
        ExecuteAvailableAction(index)
        return
    else:
        #TODO: POSSIBLE TO ADD ACTION NAME CHECK!!
        pass
    uci.UserInputInvalid("No available choice found!")        
        
        
currentMenu = None
availableActions = None

baseActions = ()
mainMenu = ()
    
def Initialize():
    global baseActions
    global mainMenu
    baseActions = (Action("Show Menus", ShowMenus), )
    mainMenu = Menu("Main Menu")
    ChangeMenu(mainMenu)