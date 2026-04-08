import random


class Game():
    """
    1s - CX
    0s - Non-CXs
    """
    def __init__(self, deck_cx, deck_total, wr_cx, wr_total, level, clock):
        self.resolution = []
        self.dmg = 0
        self.lost = 0

        self.level = level
        self.clock = [0]*clock
        self.deck = ([1] * deck_cx) + ([0] * (deck_total-deck_cx))
        random.shuffle(self.deck)
        # print('--------------------------------------------------')
        # print('START DECK', self.deck)
        self.waiting = ([1] * wr_cx) + ([0] * (wr_total-wr_cx))

    def refresh(self):
        self.deck = self.waiting
        self.waiting = []
        random.shuffle(self.deck)
        self.dmg += 1
        try:
            card = self.deck.pop()
        except:
            print('Cannot take refresh damage, game lost')  # Should be rare
            self.game_lost()
            return
        self.clock += [card]
        self.check_level()

    def game_lost(self):
        self.lost = 1
        raise Exception("Game over")

    def check_level(self):
        # Check if we're leveling
        if len(self.clock) >= 7:
            # Perform level up
            new_clock = self.clock[7:]
            old_clock = self.clock[:7]
            # Select a random non-cx to level, it'll disappear into thin air for now
            idx = old_clock.index(0)
            old_clock.pop(idx)

            # Assign new clock
            self.level += 1
            self.waiting += old_clock
            self.clock = new_clock

            # Check if level 4
            if self.level > 3:
                # print('Leveled to 4')
                self.game_lost()

    def burn(self, x):
        for i in range(0, x):
            if len(self.deck) > 0:
                card = self.deck.pop(0)
            else:
                # Refresh
                while len(self.deck) == 0:
                    self.refresh()
                card = self.deck.pop(0)

            self.resolution += [card]

            # Cancel
            if card:
                self.waiting += self.resolution
                self.resolution = []
                return 0

        # Resolve dmg
        self.clock += self.resolution
        self.resolution = []
        self.dmg += x
        self.check_level()
        return x

    def deal_dmg(self, dmg_array):
        for dmg in dmg_array:
            try:
                self.burn(dmg)
            except:
                # Losing will throw a game loss exception
                break
        # print('Took', self.dmg)
        # print(f'Level {self.level}-{len(self.clock)} | {self.clock}')
        self.dmg = 0


losses = 0
wins = 0
sample = 10000
for i in range(0, sample):
    # 8 in 30 deck, 10 clean in wr
    x = Game(8, 30, 0, 10, level=3, clock=0)
    # Triple Marine
    x.deal_dmg([2, 3, 2, 3, 2, 3])

    # Examples:
    # 8 in 23 deck, 0 cards in wr (fresh deck)
    # x = Game(8, 23, 0, 0, level=2, clock=5)
    # 2 in 9 deck, 6 in 20 wr
    # x = Game(2, 9, 6, 20, level=2, clock=1)

    # 4 Stickers
    # x.deal_dmg([4, 4, 4, 4, 3, 2, 3, 2, 3, 2])
    # TRV, 3 burns
    # x.deal_dmg([2, 2, 3, 3, 4, 3, 1, 1, 1, 1, 1, 3])

    if x.lost:
        losses += 1
    else:
        wins += 1

print(f'Losses: {losses} | Wins: {wins}')
print(f'{round(losses/sample*100, 2)} % to lose')
print(f'{round(wins/sample*100, 2)} % to live')

