class Player:
    def __init__(self, player_num):
        self.money = 2
        self.cards = []
        self.num_cards = 0
        self.dead = False
        self.player_num = player_num

    def deal(self, card):
        self.cards.append(card)
        self.num_cards += 1
    
    def getMove(self):
        m = input("  Your move: ")
        m = m.split(" ")
        if len(m) == 1:
            m.extend([None, None])
        elif len(m) == 2:
            m.append(None)
        return {"action": m[0], "role": m[1], "victim": m[2]}
    
    def kill(self):
        self.num_cards -= 1
        if self.num_cards == 0:
            self.dead = True