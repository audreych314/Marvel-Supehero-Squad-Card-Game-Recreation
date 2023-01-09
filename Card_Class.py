class Card():
    def __init__(self, name, level, attack, type, blocks, img):
        self.level = level
        self.type = type
        self.blocks = blocks
        self.img = img
        self.name = name
        self.attack = attack
    def getLevel(self):
        return self.level
    def getAttack(self):
        return self.attack
    def getType(self):
        answer = ""
        for s in self.type:
            answer += s + " "
        return answer
    def getName(self):
        return self.name
    def getBlocks(self):
        return self.blocks
    def getImage(self):
        return self.img
    def __repr__(self):
        return (f'{self.name}, Level: {self.level}, ' +\
            f'Attack: {self.attack}, ' +\
            f'Type: {self.type}, Blocks: {self.blocks}\n')

