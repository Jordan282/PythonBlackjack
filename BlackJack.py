import random

#cardSuits = ["Diamonds", "Spades", "Hearts", "Clubs"]
##cardList = ["Ace" , "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
#deck = [(card, suit) for card in cardList for suit in cardSuits]
### Moved deck to while loop since list would runn out if the game went on for long enough... Now puts cards back in deck and shuffles for no duplicate cards.
balance = 100
splitHand1 = 0
splitHand2 = 0
playerScore = 0
splitHand1Value = 0
splitHand2Value = 0

def dealingDealerCards(dealerScore, dealerCards):
        while dealerScore < 17: 
            newCard = deck.pop()
            dealerCards.append(newCard)
            dealerScore = dealerScore + cardValue(newCard)
            if dealerScore > 16:
                return dealerScore
            elif dealerScore < 17:
                continue
    
def gameResult(dealerScore, playerScore, playerBet, playerChoice, balance, splitHand1, splitHand2):
    if playerChoice == "split":
        while True:
            print("\n")
            if splitHand1Value > 21:
                print("Player busts hand 1.")
            elif dealerScore > 21:
                print("Dealer busts... player wins!")
                balance = balance + playerBet * 2
            elif splitHand1Value > dealerScore:
                print("Player has", splitHand1)
                print("Dealer has", dealerCards)
                print("Player has", splitHand1Value,"and Dealer", dealerScore)
                print("Player wins!")
                balance = balance + playerBet * 2
            elif dealerScore > splitHand1Value:
                print("Player has", splitHand1)
                print("Dealer has", dealerCards)
                print("Player has", splitHand1Value,"and Dealer", dealerScore)
                print("Dealer wins!")
            break

        while True:
            print("\n")
            if splitHand2Value > 21:
                print("Player busts hand 1.")
            elif dealerScore > 21:
                print("Dealer busts... player wins!")
                balance = balance + playerBet * 2
            elif splitHand2Value > dealerScore:
                print("Player has", splitHand2)
                print("Dealer has", dealerCards)
                print("Player has", splitHand2Value,"and Dealer", dealerScore)
                print("Player wins!")
                balance = balance + playerBet * 2
            elif dealerScore > splitHand2Value:
                print("Player has", splitHand2)
                print("Dealer has", dealerCards)
                print("Player has", splitHand2Value,"and Dealer", dealerScore)
                print("Dealer wins!")
            break
    
    elif playerScore > 21:
        print("Player has:", playerCards)
        print("Player has a score of:", playerScore)
        print("\n")
        print("Player is over the score of 21 and busts")
        print("Dealer wins")

    elif dealerScore > 21:
        print("Dealer has:", dealerCards)
        print("Dealers score is:", dealerScore)
        print("\n")
        print("Dealer busts")
        print("Player wins!")
        if playerChoice == "double down":
            balance = balance + playerBet * 4    
        else:
            balance = balance + playerBet * 2
    elif dealerScore < playerScore:
        print("Player has:", playerCards)
        print("Dealer has:", dealerCards)
        print("\n")
        print("Dealer has:", dealerScore, "Player has:", playerScore)
        print("Player wins!")
        if playerChoice == "double down":
            balance = playerBet * 4 + balance    
        else:
            balance = balance + playerBet * 2

    elif dealerScore > playerScore:
        print("Player has:", playerCards)
        print("Dealer has:", dealerCards)
        print("\n")
        print("Dealer has:", dealerScore, "Player has:", playerScore)
        print("\n")
        print("Dealer wins!")

    elif playerScore == dealerScore:
        print("Player has:", playerCards)
        print("Dealer has:", dealerCards)
        print("\n")
        print("Dealer has:", dealerScore, "Player has:", playerScore)
        print("\n")
        print("Both have the same score it's a tie...")
        if playerChoice == "double down":
            balance = balance + playerBet * 2
        else:
            balance = balance + playerBet

    return balance

def splitHand1Function(playerCards, deck, dealerCards):
    hand1 = [playerCards[0], deck.pop()]
    
    #print(hand1), print(hand2), print("\n"), print(hand1Score), print(hand2Score) ##Testing for seperate split hands

    while True:
        hand1Score = sum(cardValue(card) for card in hand1)

        if hand1Score > 21:
            print("Player has", hand1)
            print("Player has a score of", hand1Score )
            input("This hand has busted press enter to continue to next hand")
            break
        print("Dealer has ", dealerCards[0],"and ???")
        print("\n")
        print("Player has", hand1)
        print("Player has a score of", hand1Score )

        hand1Choice = input("Would you like to hit or stand?")
        if hand1Choice == "hit":
            newCard = deck.pop()
            hand1.append(newCard)
        elif hand1Choice == "stand":
            break
        else:
            input("That is not an option please press enter and try again")
    print(hand1)
    input()
    return hand1
    

def splitHand2Function(playerCards, deck, dealerCards):
    hand2 = [playerCards[1], deck.pop()]
        
    while True:  
        hand2Score = sum(cardValue(card) for card in hand2)

        if hand2Score > 21:
            print("Player has", hand2)
            print("Player has a score of", hand2Score )
            input("This hand has busted press enter to continue to next hand")
            break

        print("Dealer has ", dealerCards[0],"and ???")
        print("\n")
        print("Player has", hand2)
        print("Player has a score of", hand2Score )

        hand2Choice = input("Would you like to hit or stand?")
        if hand2Choice == "hit":
            newCard = deck.pop()
            hand2.append(newCard)
        elif hand2Choice == "stand":
            break
        else:
            input("That is not an option please press enter and try again")
    return hand2


def splitCheck(playerCards):
    splitCardValueList = [cardValue(card) for card in playerCards]
    return splitCardValueList




while balance > 0:
    def cardValue(card):
        if card[0] in ["Jack", "Queen", "King"]:
            return 10
        elif card[0] == "Ace":
            if playerScore or splitHand1Value or splitHand2Value < 11:
                return 11
            else:
                return 1
        else:
            return int(card[0])
    
    playerBetstr = input("How much would you like to bet? You have {balance}:".format(balance=balance))
    playerBet = int(playerBetstr)
    if playerBet > balance:
        print("That's to much please bet within your limits")
        continue
    elif playerBet < 1:
        print("That's to little please bet more")
        continue    
    else:
        balance = balance - playerBet
    cardSuits = ["Diamonds", "Spades", "Hearts", "Clubs"]
    cardList = ["Ace" , "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    deck = [(card, suit) for card in cardList for suit in cardSuits]    
    random.shuffle(deck)
    playerCards = [deck.pop(), deck.pop()]
    dealerCards = [deck.pop(), deck.pop()]

    while True:
        playerScore = sum(cardValue(card) for card in playerCards)
        dealerScore = sum(cardValue(card) for card in dealerCards)
        
        print("Dealer has ", dealerCards[0],"and ???")
        print("\n")
        print("Player has:", playerCards)
        print("Player has a score of:", playerScore)
        
        

        if playerScore > 21:
            break
        
        #print(balance), input() ###Test for double down

        playerChoice = input("Would you like to hit, stand, double down, or split?:")
        if playerChoice == "hit":
            newCard = deck.pop()
            playerCards.append(newCard)
        elif playerChoice == "stand":
            break
        elif playerChoice == "double down":
            balance = balance - playerBet
            if balance < 1:
                print("You do not have enough money to double down")
                balance = balance + playerBet
                continue
            elif balance > 0:
                newCard = deck.pop()
                playerCards.append(newCard)
                playerScore = sum(cardValue(card) for card in playerCards)
                print("\n")
                print("Player has:", playerCards)
                input("You now have {playerScore} total... press enter to continue.".format(playerScore=playerScore))
                break
        elif playerChoice == "split":
            splitCardValueList = splitCheck(playerCards)
            splitCardValue1 = splitCardValueList[0]
            splitCardValue2 = splitCardValueList[1]
            balance = balance - playerBet
            if balance < 1:
                print("Sorry you do not have enough money to split")
                balance = balance + playerBet
                continue
            
            if splitCardValue1 == splitCardValue2:
                print("You can split")
                splitHand1 = splitHand1Function(playerCards, deck, dealerCards)
                splitHand2 = splitHand2Function(playerCards, deck, dealerCards)
                splitHand1Value = sum(cardValue(card) for card in splitHand1)
                splitHand2Value = sum(cardValue(card) for card in splitHand2)
                break
            else:
                print("These cards are not the same value you cannot split")
                continue
        else:
            print("Invalid choice or incorrect spelling try again")
            continue
    
    if dealerScore < 17:
        dealerScore = dealingDealerCards(dealerScore, dealerCards)
    balance = gameResult(dealerScore, playerScore, playerBet, playerChoice, balance, splitHand1, splitHand2) 
    
print("Say goodbye to your life savings...")



    





