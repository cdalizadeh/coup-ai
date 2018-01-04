from Player import Player
from Card import Card

from random import shuffle

class Game:
    types = ["assassin", "duke", "contessa", "captain", "ambassador"]
    
    def __init__(self, nplayers = 4, turn = 0):
        self.nplayers = nplayers
        self.players = []
        for _ in range(nplayers):
            self.players.append(Player())
        self.deck = []
        for _ in range(3):
            self.deck.extend(self.types)
        shuffle(self.deck)
        for player in self.players:
            player.deal(self.deck.pop())
            player.deal(self.deck.pop())
        self.turn = turn
        self.gameover = False

    def play(self):
        i = 0
        while not self.gameover:
            print("Player {:d}'s turn.".format(i))
            player = self.players[i]

            if player.numcards > 0:
                move = player.getMove()

                if move["action"] == "income":
                    player.money += 1
                
                elif move["action"] == "foreignaid":
                    pass

                elif move["action"] == "tax":
                    pass

                elif move["action"] == "steal":
                    pass

                elif move["action"] == "look":
                    pass

                elif move["action"] == "assassinate":
                    pass

                elif move["action"] == "coup":
                    self.players[move["victim"]].kill

                else:
                    raise ValueError("Illegal action requested")
                
                i = (i + 1) % 4

