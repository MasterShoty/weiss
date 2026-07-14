import random


class Game:
    """
    Cards are denoted by
    1s - CX
    0s - Non-CXs
    """
    def __init__(self, deck_cx: int = 8, deck_total: int = 50,
                 wr_cx: int = 0, wr_total: int = 0,
                 level: int = 0, clock: int = 0):
        self.dmg: int = 0  # Internal counter for accumulated dmg (includes refreshes)
        self.lost: bool = False

        self.level: int = level
        self.clock: list[int] = [0]*clock
        self.deck: list[int] = ([1] * deck_cx) + ([0] * (deck_total-deck_cx))
        self.waiting: list[int] = ([1] * wr_cx) + ([0] * (wr_total-wr_cx))
        self.resolution: list[int] = []

        self.shuffle_deck()
        # print('--------------------------------------------------')
        # print('START DECK', self.deck)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def game_lost(self):
        self.lost = True
        # raise Exception("Game over")

    def refresh(self):
        self.deck = self.waiting
        self.waiting = []
        if len(self.deck) == 0:
            print('Cannot take refresh damage, game lost')  # Should be rare
            self.game_lost()
            return

        self.shuffle_deck()
        card = self.deck.pop()
        self.clock += [card]
        self.dmg += 1
        self.check_level()

    def check_level(self):
        # Check if we're leveling
        if len(self.clock) >= 7:
            # Perform level up
            new_clock = self.clock[7:]
            old_clock = self.clock[:7]
            # Select a random non-cx to level, it'll disappear into thin air for now
            if 0 in old_clock:
                old_clock.remove(0)
            elif 1 in old_clock:
                old_clock.remove(1)
            else:
                raise ValueError()
            # Assign new clock
            self.level += 1
            self.waiting += old_clock
            self.clock = new_clock

        # Check if level 4
        if self.level > 3:
            self.game_lost()

    def burn(self, x: int):
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

    """
    Burn x, if cancel burn y, up to count times, repeat repeat times
    """
    def cancel_burn(self, x, y, count: int = 1, repeat: int = 1):
        curr_count = 0
        cancelled = self.burn(x) == 0 and x > 0
        while cancelled and curr_count < count:
            curr_count += 1
            for i in range(0, repeat):
                cancelled = self.burn(y) and y > 0

    """
    Shorthand for burns
    """
    def deal_dmg(self, dmg_array):
        for dmg in dmg_array:
            self.burn(dmg)

    """
    Top deck x cards from waiting
    """
    def topdeck(self, x: int):
        i = 0
        while i < x and 0 in self.waiting:
            # Get a non-climax and top deck it
            self.waiting.remove(0)
            self.deck.insert(0, 0)
            i += 1

    """
    Top deck a board character, this inserts a new card into the deck
    """
    def topdeck_opp(self):
        self.deck.insert(0, 0)

    """
    Shuffle_back x non-climax cards from waiting
    """
    def shuffle_back(self, x: int):
        cards = []
        while len(cards) < x and 0 in self.waiting:
            self.waiting.remove(0)
            cards.append(0)

        self.deck += cards
        self.shuffle_deck()

    """
    Check top x for cxs and put into waiting, conditional shuffle
    """
    def moca(self, x: int, shuffle: bool = False):
        clean = [e for e in self.deck[:x] if e != 1]
        cxs = [e for e in self.deck[:x] if e == 1]
        self.deck = clean + self.deck[x:]
        self.waiting += cxs
        if shuffle:
            self.shuffle_deck()
        pass


losses = 0
wins = 0
sample = 50000
for i in range(0, sample):
    # 8 in 30 deck, 10 clean in wr
    # x = Game(8, 30, 0, 10, level=3, clock=0)
    # Triple Marine
    # x.deal_dmg([2, 3, 2, 3, 2, 3])

    # Examples:
    # 8 in 23 deck, 0 cards in wr (fresh deck)
    # x = Game(8, 23, 0, 0, level=2, clock=5)
    # 2 in 9 deck, 6 in 20 wr
    # x = Game(2, 9, 6, 20, level=2, clock=1)

    # 4 Stickers
    # x.deal_dmg([4, 4, 4, 4, 3, 2, 3, 2, 3, 2])
    # TRV, 3 burns
    # x.deal_dmg([2, 2, 3, 3, 4, 3, 1, 1, 1, 1, 1, 3])

    # 3x Itsuki
    # x = Game(7, 20, 0, 0, level=3, clock=0)
    # for i in range(0, 3):
    #     x.burn(3)
    #     x.moca(2)
    #     x.burn(3)

    # 3x Albedo
    x = Game(7, 20, 0, 0, level=3, clock=0)
    x.deal_dmg([3, 3, 3])
    for i in range(0, 3):
        x.cancel_burn(2, 1)

    # Touhou
    # x = Game(3, 6, 4, 20, level=3, clock=0)
    # x.deal_dmg([3, 1, 1, 2, 2, 3, 3, 4])

    # Gay Angels
    # x = Game(4, 9, 4, 25, level=3, clock=0)
    # for i in range(0, 3):
    #     x.burn(3)
    #     x.topdeck(2)
    #     x.burn(4)

    # TODO: Test cancel burn repeat, ie. Cancel burn 2 up to 2 times.

    if x.lost:
        losses += 1
    else:
        wins += 1

print(f'Losses: {losses} | Wins: {wins}')
print(f'{round(losses/sample*100, 2)} % to lose')
print(f'{round(wins/sample*100, 2)} % to live')

