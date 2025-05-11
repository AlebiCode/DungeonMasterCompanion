import ActionsNavigation as actnav
from ConsoleOutputStyle import SetStyle_MainTitle, SetStyle_Default
from colorama import Fore, Back, Style

APP_NAME = "Dungeon Master Companion"
VERSION = "0.1"


actnav.Initialize()

SetStyle_MainTitle()
print(f"""
       ____________________________________
      |                                    |
      |   Henlo!!! Welcome to the DMC!!!   |
      |____________________________________|
      version: {VERSION}
      """
      )
SetStyle_Default()

print("Navigate menus by inputting the desired action index.")
while True:
    actnav.AvailableActionSelection()