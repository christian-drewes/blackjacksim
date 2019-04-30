class Player:
    def __init__(self):
        self.playerHand = []
        self.handVal = 0
        self.isDone = False
        self.hasAce = False
        self.wins = 0

    def getHasAce(self):
        return self.hasAce
    
    def addCard(self, card):
        self.playerHand.append(card)

    def getHand(self):
        tempHand = []
        for i in self.playerHand:
            tempHand.append(i[0])
        print('your hand is ', tempHand)

    def getHandVal(self):
        # Check if over 21
        self.handVal = 0
        for i in self.playerHand:
            self.handVal += i[1]
        # Check for aces
        self.checkAce()
        if self.handVal > 21:
            #this means that the player has busted
            self.handVal = 0
        return self.handVal
    
    def checkAce(self):
        #Are there aces in the hand if there is then over 21 change aces until under or bust
        #if 'A' in self.playerHand:
            for i in self.playerHand:
                if i[0] == 'A':
                    self.hasAce = True
                if self.handVal > 21 and i[0] == 'A':
                    i[1] = 1
                    self.handVal = 0
                    for j in self.playerHand:
                        self.handVal += j[1]