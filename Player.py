from Card import Card
class Player:
    def __init__(self):
        self.money = 2
        self.cards = []
        self.numcards = 0

    def deal(self, card):
        self.cards.append(card)
        self.numcards += 1
    
    def getMove(self):
        m = input("  Your move: ")
        m = m.split(" ")
        if len(m) == 1:
            m.extend([None, None])
        elif len(m) == 2:
            m.append(None)
        return {"action": m[0], "role": m[1], "victim": m[2]}
    
    def kill(self):
        numcards -= 1