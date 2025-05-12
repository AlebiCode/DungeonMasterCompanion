import Characters as chars
from Menus import Menu, MenuOption, ChangeMenu
from UserConsoleInput import GetUserInput, GetUserInputIndex, GetUserInputIndexes

class Combatant:
    def __init__(self, character: chars.Character, hp: int, tmpHp: int, initiative: int):
        self.character = character
        self.hp = hp
        self.tmpHp = tmpHp
        self.initiative = initiative
        
    def __str__(self):
        return str(self.character)
        
    def PrintInfo(self):
        print(f"{self.character.name} Hp {f"{self.hp}+{self.tmpHp}" if self.tmpHp>0 else self.hp}/{self.character.maxHp}")

def GetOptionalIntFromList(intList: list[int], index: int):
    return intList[index] if len(intList) > index else 0

def AddCombatant():
    name = GetUserInput("Enter Name:")
    hpInputtedVals = GetUserInputIndexes("Enter Max Hp, Current Hp (optional) and Temporary Hp (optional):", 3)
    maxHp = GetOptionalIntFromList(hpInputtedVals, 0)
    hp = GetOptionalIntFromList(hpInputtedVals, 1)
    tempHp = GetOptionalIntFromList(hpInputtedVals, 2)
    initiative = GetUserInputIndex("Enter Initiative:")
    combatant = Combatant(chars.Character(name, maxHp), hp, tempHp, initiative)
    combatant.PrintInfo()
    combatants.append()
    combatMenu.options.append(MenuOption(f"{combatant.character.name}", OpenManageCharacterMenu))

def RemoveCombatant():
    pass

def OpenManageCharacterMenu():
    global manageCharaterMenu
    ChangeMenu(manageCharaterMenu)

def BackToCombatMenu():
    ChangeMenu(combatMenu)

combatMenu: Menu
manageCharaterMenu: Menu
combatants: list[Combatant]

def GenerateCombatMenu() -> Menu:
    manageCombatantsMenu = Menu("Manage Combatants", 
                                [
                                    MenuOption("Back", BackToCombatMenu),
                                    MenuOption("Add", AddCombatant),
                                    #load combatant
                                    #remove combatant
                                ])
    combatMenuOptions = [MenuOption("Manage Combatants", lambda: ChangeMenu(manageCombatantsMenu))]
    global combatMenu
    combatMenu = Menu("Combat", combatMenuOptions)
    return combatMenu

def TEMP():
    print("TEMP!!")
#manage combatants
#add
#load
#remove
#group
#save to file

#combatants options
#attack
#heal
#No max hp change support yet!
#remove from fight