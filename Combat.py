import Characters as chars
from Menus import Menu, MenuOption, ChangeMenu
import UserConsoleInput as uci
import ConsoleOutputStyle as cos

class Combatant:
    #combat stats:
    damageDealt: int = 0
    overkillDamageDealt: int = 0
    defeatingBlowsDealt: int = 0
    damageReceived: int = 0
    overkillDamageReceived: int = 0
    defeatingBlowsRecieved: int = 0
    healing: int = 0
    
    def __init__(self, character: chars.Character, hp: int, tmpHp: int, initiative: int):
        self.character = character
        self.hp = hp
        self.tmpHp = tmpHp
        self.initiative = initiative
    def __str__(self):
        return str(self.character)
        
    def GetInfo(self) -> str:
        return f"{cos.Fore.BLACK}{cos.Back.WHITE} {self.character.name} {cos.Back.RED} Hp {f" {self.hp}+{self.tmpHp}" if self.tmpHp>0 else self.hp}/{self.character.maxHp} {cos.Style.RESET_ALL} Init {self.initiative}"

    def ResetStats(self):
        self.damageDealt = self.overkillDamageDealt = self.defeatingBlowsDealt = 0 
        self.damageReceived = self.overkillDamageReceived = self.defeatingBlowsRecieved = 0
        self.healing = 0

    def GetCombatStatsInString(self) -> str:
        return f"""{self.GetInfo()}
    Dealt {self.damageDealt} damage (+{self.overkillDamageDealt} overkill) and {self.defeatingBlowsDealt} defeating blows.
    Received {self.damageReceived} damage (+{self.overkillDamageReceived} overkill) and {self.defeatingBlowsRecieved} defeating blows.
    Given {self.healing} healing.
    """

    def DealDamage(self, other, damage: int):
        isTrackedDamage = self != other
        damagesDone = other.RecieveDamage(damage, isTrackedDamage)
        if isTrackedDamage:
            self.damageDealt += damagesDone[0]
            self.overkillDamageDealt += damagesDone[1]
            self.defeatingBlowsDealt += damagesDone[2]
    def RecieveDamage(self, damage: int, isTrackedDamage: bool = True) -> tuple[int, int, int]:    
        '''
        Returns tuple (hp damage actually recieved, overkill damage, if the creature dropped to 0 hit points).
        '''
        _tmpHpDmg = min(damage, self.tmpHp)
        self.tmpHp -= _tmpHpDmg
        damage -= _tmpHpDmg
        _hpDmg = min(damage, self.hp)
        self.hp -= _hpDmg
        damage -= _hpDmg
        isDefeatingBlow = self.hp == 0
        if isTrackedDamage:
            self.damageReceived += _tmpHpDmg + _hpDmg
            self.overkillDamageReceived += damage
            self.defeatingBlowsRecieved += isDefeatingBlow
        return (_tmpHpDmg + _hpDmg, damage, isDefeatingBlow)
    
    def Heal(self, other, heal: int, isTemporaryHp: bool):
        self.healing += other.RecieveHealing(heal, isTemporaryHp)
    def RecieveHealing(self, heal: int, isTemporaryHp: bool) -> int:
        '''
        Returns healing actually recieved.
        '''
        if isTemporaryHp:
            actualHealing = max(heal - self.tmpHp, 0)
            self.tmpHp += actualHealing
        else:
            actualHealing = min(heal, self.character.maxHp - self.hp)
            self.hp += actualHealing
        return actualHealing
    
    
    
def GetOptionalIntFromList(intList: list[int], index: int):
    return intList[index] if len(intList) > index else -1

def AddCombatant():
    name = uci.GetUserInput("Enter Name:")
    if name == "": name = "Nessuno"
    hpInputtedVals = uci.GetUserInputIndexes("Enter Max Hp, Current Hp (optional) and Temporary Hp (optional):", 3)
    maxHp = max(GetOptionalIntFromList(hpInputtedVals, 0), 0)
    hp = GetOptionalIntFromList(hpInputtedVals, 1)
    hp = min(hp, maxHp) if hp >= 0 else maxHp 
    tempHp = max(GetOptionalIntFromList(hpInputtedVals, 2), 0)
    initiative = uci.GetUserInputIndex("Enter Initiative:")
    addition = Combatant(chars.Character(name, maxHp), hp, tempHp, initiative)
    placement = 0
    evensAmount = 0
    global combatants
    for combatant in combatants:
        if addition.initiative < combatant.initiative:
            break
        elif addition.initiative == combatant.initiative:
            evensAmount += 1
        else:
            placement += 1
    if evensAmount > 0:
        print(f"Multiple combatants with an initiative of {addition.initiative}.")
        options = []
        indexOfEven = 0
        for indexOfEven in range(0, evensAmount):
            options.append(f"Go before {combatants[placement+indexOfEven]}")
        options.append("Go last")
        selection = max(0, uci.OptionSelection(options))
        placement += selection
    combatants.insert(placement, addition)
    global baseCombatMenuOptions
    combatMenu.options.insert(baseCombatMenuOptions + placement, MenuOption(lambda: addition.GetInfo(), lambda: OpenCharacterActionsMenu(addition)))
    print(f"Added {addition.GetInfo()}.")

def RemoveCombatant():
    print("Choose combatant to remove:")
    global combatants
    index = uci.OptionSelection(combatants)
    if index < 0: return
    removed = combatants.pop(index)
    global baseCombatMenuOptions
    combatMenu.options.pop(baseCombatMenuOptions + index)
    print(f"Removed {removed.GetInfo()}.")

def OpenCharacterActionsMenu(combatant: Combatant):
    global selectedCombatant
    selectedCombatant = combatant
    global characterActionsMenu
    ChangeMenu(characterActionsMenu)

def DealDamage():
    global combatants
    print("Select target:")
    targetIndex = uci.OptionSelection([combatant.GetInfo() for combatant in combatants])
    if targetIndex < 0: return
    amount = uci.GetUserInputIndex("Enter damage:")
    target = combatants[targetIndex]
    selectedCombatant.DealDamage(target, max(amount, 0))
    print(f"{TargetingToString(selectedCombatant, target, "hits")} for {amount} damage.")
    if target.hp == 0:
        cos.SetStyle(f"{cos.Fore.YELLOW}")
        print(f"{target} is defeated!")
        cos.SetStyle_Default()
def Heal():
    global combatants
    print("Select target:")
    targetIndex = uci.OptionSelection(combatants)
    if targetIndex < 0: return
    print("Select healing type:")
    isTemporary = uci.OptionSelection(["Hit Points", "Temporary Hit Points"]) == 1
    amount = uci.GetUserInputIndex("Enter heal:")
    target = combatants[targetIndex]
    selectedCombatant.Heal(target, max(amount, 0), isTemporary)
    print(f"{TargetingToString(selectedCombatant, target, "heals")} by {amount}.")

def TargetingToString(source: Combatant, destination: Combatant, verb: str):
    return f"{source.character.name} {verb} {destination.character.name if source != destination else "themselves"}"

def PrintSelectedCombatantInfos():
    PrintCombatantInfos(selectedCombatant)

def PrintCombatantInfos(combatant: Combatant):
    print(f"- - - - - - - -{combatant.GetCombatStatsInString()}")

def EndCombat():
    print("\n------------END OF COMBAT------------\n")
    for comb in combatants:
        PrintCombatantInfos(comb)
        comb.ResetStats()
    print("\n------------All combat stats reset------------\n")


#TODO: dont increase some stats in case of self damage!
    
combatMenu: Menu
baseCombatMenuOptions: int
combatants: list[Combatant] = []

characterActionsMenu: Menu
selectedCombatant: Combatant

def GenerateCombatMenu() -> Menu:
    backToCombatMenu = lambda: ChangeMenu(combatMenu)
    global characterActionsMenu
    characterActionsMenu = Menu("Combatant Actions",
                                [
                                    MenuOption("Back", backToCombatMenu),
                                    MenuOption("Deal damage", DealDamage),
                                    MenuOption("Heal", Heal),
                                    MenuOption("Print infos", PrintSelectedCombatantInfos),
                                ],
                                False
                                )
    manageCombatantsMenu = Menu("Manage Fight", 
                                [
                                    MenuOption("Back", backToCombatMenu),
                                    MenuOption("Add Combatant", AddCombatant),
                                    #TODO load combatant(s)
                                    #TODO save combatant(s)
                                    MenuOption("Remove Combatant", RemoveCombatant),
                                    MenuOption("End this Fight", EndCombat)
                                ],
                                False
                                )
    combatMenuOptions = [MenuOption("Manage Fight", lambda: ChangeMenu(manageCombatantsMenu))]
    global baseCombatMenuOptions
    baseCombatMenuOptions = len(combatMenuOptions)
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