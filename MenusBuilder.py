# Builds the games menu navigation structure
from Menus import MenuOption, Menu, SetGlobalMenuOptions, ChangeMenu
from Combat import GenerateCombatMenu
from ConsoleOutputStyle import STYLE_LESS_IMPORTANT

menuSelectionMenu: Menu
combatMenu: Menu

def InitializeMenus():
    global combatMenu
    combatMenu = GenerateCombatMenu()
    
    global menuSelectionMenu
    showMenusActions = [MenuOption("Combat", lambda: ChangeMenu(combatMenu))]
    menuSelectionMenu = Menu("Menu Selection", showMenusActions, False)
    
    SetGlobalMenuOptions( [MenuOption("Change Menu", lambda: ChangeMenu(menuSelectionMenu), STYLE_LESS_IMPORTANT), ] )
    ChangeMenu(menuSelectionMenu)