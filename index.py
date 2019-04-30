import random
import db
import graph
from player import Player

deck = []

deckCopy = []

p1Wins = 0
p2Wins = 0
d1Wins = 0
d2Wins = 0

#dont hit on
limit = 12 

#initialize player and dealer
playerOne = Player()
playerAlt = Player()
dealer = Player()
dealerAlt = Player()

def gameReset():
    global deck
    global deckCopy
    global playerOne
    global playerAlt
    global dealer
    global dealerAlt
    global p1Wins
    global p2Wins
    global d1Wins
    global d2Wins

    deck = [['A', 11], ['2', 2], ['3', 3], ['4', 4], ['5', 5], ['6', 6],
        ['7', 7], ['8', 8], ['9', 9], ['10', 10], ['J', 10], ['Q', 10], ['K', 10]]*4

    p1Wins += playerOne.wins
    p2Wins += playerAlt.wins
    d1Wins += dealer.wins
    d2Wins += dealerAlt.wins

    deckCopy = []
    playerOne = Player()
    playerAlt = Player()
    dealer = Player()
    dealerAlt = Player()

def initializeGame():
    #shuffle the deck
    random.shuffle(deck)
    deckCopy = list(deck)

    # Deal out cards
    playerOne.addCard(deck.pop())
    playerAlt.addCard(deckCopy.pop())
    dealer.addCard(deck.pop())
    dealerAlt.addCard(deckCopy.pop())
    playerOne.addCard(deck.pop())
    playerAlt.addCard(deckCopy.pop())
    dealer.addCard(deck.pop())
    dealerAlt.addCard(deckCopy.pop())

    playerOne.getHand()
    playerAlt.getHand()
    dealer.getHand()
    dealerAlt.getHand()

def playerAndDealerTurn():
    #Check if player stays on 17 or less
    checkPlayerDecision(playerOne)
    #Check if player stays on 12 or less
    print(len(deck))

    checkPlayerDecision(playerAlt)

    checkPlayerDecision(dealer, limit)

    checkPlayerDecision(dealerAlt)

def checkPlayerDecision(p, lim = 17):
    #Checking card value and making a decision based off that
    playerStay = False
    while not playerStay:
        val = p.getHandVal()
        if val > 21 or p.getHandVal() == 0:
            playerStay = True
        elif p.getHasAce() and val < 17:
            p.addCard(deck.pop())
        elif val >= lim:
            playerStay = True
        else:
            p.addCard(deck.pop())

def checkWinner(p, d):
        
    if p.getHandVal() > d.getHandVal():
        #player wins
        print("Player wins")
        p.wins += 1
        return "win"
    elif p.getHandVal() < d.getHandVal():
        #dealer wins
        print("dealer wins")
        d.wins += 1
        return "loss"
    else:
        #TIE
        print("Tie")
        return "tie"

if __name__ == '__main__':
    db.createTable()
    iteration = 0
    while iteration < 100:
        gameReset()
        initializeGame()
        print(len(deck))
        playerAndDealerTurn()
        db.insertData(iteration+1, checkWinner(playerOne, dealer), checkWinner(playerAlt, dealerAlt))

        # Print final hand
        playerOne.getHand()
        playerAlt.getHand()
        dealer.getHand()
        dealerAlt.getHand()

        iteration += 1
    graph.createGraph(p1Wins, d1Wins, p2Wins, d2Wins)
