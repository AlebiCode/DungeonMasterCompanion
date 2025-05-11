import Menus

def SayHello():
    print("Henlo!")

def GenerateCombatMenu() -> Menus.Menu:
    options = (Menus.MenuOption("SayHello", SayHello), Menus.MenuOption("SAY HELLO", SayHello))
    return Menus.Menu("Combat", options, True)