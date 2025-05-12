import Menus
from ConsoleOutputStyle import SetStyle_MainTitle, SetStyle_Default
from MenusBuilder import InitializeMenus

APP_NAME = "Dungeon Master Companion"
APP_VERSION = "0.1"

# APPLICATION FLOW STARTS HERE!
0
SetStyle_MainTitle()
print(f"""
       ____________________________________
      |                                    |
      |   Henlo!!! Welcome to the DMC!!!   |
      |____________________________________|
      version: {APP_VERSION}
      """
      )
SetStyle_Default()

print("Navigate menus by inputting the desired option index.")
InitializeMenus()
while True:
    Menus.AvailableActionSelection()