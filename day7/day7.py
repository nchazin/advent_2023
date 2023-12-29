import sys
from lib.tools import read_input


strength_1 = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13,
}

strength_2 = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.uniq = set(cards)
        self.bid = bid
        self._pairs = -1 
        self._tok = -1 
        self._fok =-1  
        self._all =-1  
        self._score = -1

    @property
    def pairs(self):
        if self._pairs == -1:
            self._pairs = [x for x in self.uniq if self.cards.count(x) == 2]
            if self._pairs == []:
                self._pairs = None

        return self._pairs

    @property
    def tok(self):
        if self._tok == -1:
            self._tok = [x for x in self.uniq if self.cards.count(x) == 3]
            if self._tok == []:
                self._tok = None
        return self._tok

    @property
    def fok(self):
        if self._fok == -1:
            self._fok = [x for x in self.uniq if self.cards.count(x) == 4]
            if self._fok == []:
                self._fok = None

        return self._fok

    @property
    def all(self):
        if self._all == -1:
            self._all = [x for x in self.uniq if self.cards.count(x) == 5]
            if self._all == []:
                self._all = None
        return self._all

    @property
    def score(self):
        if self._score == -1:
            if self.all is not None:
                self._score = 6
            elif self.fok is not None:
                self._score = 5
            elif self.tok is not None and self.pairs is not None:
                self._score = 4
            elif self.tok is not None:
                self._score = 3
            elif self.pairs is not None and len(self.pairs) == 2:
                self._score = 2
            elif self.pairs is not None:
                self._score = 1
            else:
                self._score = 0
        else:
            return self._score

    def __lt__(self, other):
        if self.score < other.score:
            return True
        elif self.score > other.score:
            return False
        else:
            return self.cardlt(other)

    def cardlt(self, other):
        for i in range(len(self.cards)):
            if strength[self.cards[i]] < strength[other.cards[i]]:
                return True
            elif strength[self.cards[i]] > strength[other.cards[i]]:
                return False
        assert False

    def set_joker_score(self):
        joker_count = self.cards.count('J')
        if joker_count == 5:
            self._score = 6
        elif joker_count == 4:
            self._score = 6
        elif joker_count == 3:
            if len(self.uniq)== 2:
                self._score = 6
            else:
                self._score = 5
        elif joker_count == 2:
            #J,J,K,K,K
            if len(self.uniq)== 2:
                self._score = 6
            # J, J, K, K, Q
            elif len(self.uniq) == 3:
                self._score =  5
            # J, J, 2, 3, A
            elif len(self.uniq) == 4:
                self._score = 3
            else:
                print("Else")
        elif joker_count == 1:
            # J, 2,2,2,2
            if len(self.uniq)== 2:
                self._score = 6
            # J, K,K, A, A
            elif len(self.uniq) == 3:
                # J, K,K, K, A
                if self.tok is not None:
                    self._score = 5 
                # J, K,K, A, A
                else:
                    self._score = 4
            # J, K, K,2  , A
            elif len(self.uniq) == 4:
                self._score = 3
            # J, K, Q, A, 2
            elif len(self.uniq) == 5:
                self._score = 1
        # default, do nothing


    def __repr__(self):
        return f"{self.cards} - {self.bid} / {self.score}"


if __name__ == '__main__':
    rows = read_input(sys.argv[1])

    hands = []

    for row in rows:
        row = row.strip()
        cards, bid = row.split(" ")
        hands.append(Hand(cards, int(bid)))

    strength = strength_1
    #property being weird  in __lt__
    for h in hands:
        score = h.score
    shands = sorted(hands)

    sum = 0
    for rank, hand in enumerate(shands):
        sum += hand.bid * (rank + 1)


    print(sum)

    for h in hands:
        h.set_joker_score()

    strength = strength_2
    shands = sorted(hands)

    sum = 0
    for rank, hand in enumerate(shands):
        sum += hand.bid * (rank + 1)
    print(sum)
