
class Character:
    def __init__(self, name: str, maxHp: int):
        self.name = name
        self.maxHp = maxHp
        
    def __str__(self):
        return self.name