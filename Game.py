from Player import Player

from random import shuffle

class Game:
    types = ["assassin", "duke", "contessa", "captain", "ambassador"]
    
    def __init__(self, num_players = 4, turn = 0):
        self.num_players = num_players
        self.players = []
        for i in range(num_players):
            self.players.append(Player(i))
        self.deck = []
        for _ in range(3):
            self.deck.extend(self.types)
        shuffle(self.deck)
        for player in self.players:
            player.deal(self.deck.pop())
            player.deal(self.deck.pop())
        self.open_cards = []
        self.turn = turn
        self.gameover = False

    def play(self):
        i = 0
        while not self.gameover:
            player = self.players[i]
            if not player.dead:
                print("Player {:d}'s turn.".format(i))
                move = player.getMove()

                if move["action"] == "income":
                    player.money += 1
                
                elif move["action"] == "foreignaid":
                    self.foreignaid(player)

                elif move["action"] == "tax":
                    self.tax(player)

                elif move["action"] == "steal":
                    self.steal(player, self.players[move["victim"]])

                elif move["action"] == "look":
                    self.look()

                elif move["action"] == "assassinate":
                    self.assassinate()

                elif move["action"] == "coup":
                    self.coup()

                else:
                    raise ValueError("Illegal action requested")
                
            i = (i + 1) % 4
    
    def foreignaid(self, action_player):
        action_blocked = False
        for block_player in self.players:
            if (not block_player.dead) and block_player != action_player:
                block_input = input("    Player {:d} blocks?: ".format(block_player.player_num))
                if block_input == "y":
                    challenge_input = input("      Player {:d} challenges?: ".format(action_player.player_num))
                    if challenge_input == "y":
                        if "duke" in block_player.cards:
                            print("        challenge fails")
                            action_player.kill()
                            action_blocked = True
                            break
                        else:
                            print("        challenge successful")
                            block_player.kill()
                    elif challenge_input == "n":
                        action_blocked = True
                    else:
                        raise ValueError("Illegal action code")
                elif block_input == "n":
                    pass
                else:
                    raise ValueError("Illegal action code")
        if not action_blocked:
            action_player.money += 2

    def tax(self, action_player):
        action_challenged = False
        for challenge_player in self.players:
            if (not challenge_player.dead) and challenge_player != action_player:
                challenge_input = input("    Player {:d} challenges?: ".format(challenge_player.player_num))
                if challenge_input == "y":
                    if "duke" in action_player.cards:
                        print("        challenge fails")
                        challenge_player.kill()
                        break
                    else:
                        print("        challenge successful")
                        action_player.kill()
                        action_challenged = True
                        break
                elif challenge_input == "n":
                    pass
                else:
                    raise ValueError("Illegal action code")
        if not action_challenged:
            action_player.money += 3

    def steal(self, action_player, victim_player):
        action_blocked = False
        