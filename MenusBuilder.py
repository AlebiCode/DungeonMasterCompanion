# Builds the games menu navigation structure

from Menus import MenuOption, Menu, SetGlobalMenuOptions, ChangeMenu
from Combat import GenerateCombatMenu

menuSelectionMenu: Menu
combatMenu: Menu

def InitializeMenus():
    global combatMenu
    combatMenu = GenerateCombatMenu()
    
    global menuSelectionMenu
    showMenusActionsTouple = (MenuOption("Combat", lambda: ChangeMenu(combatMenu)), )
    menuSelectionMenu = Menu("Menu Selection", showMenusActionsTouple, False)
    
    SetGlobalMenuOptions( (MenuOption("Change Menu", lambda: ChangeMenu(menuSelectionMenu)), ) )
    ChangeMenu(menuSelectionMenu)