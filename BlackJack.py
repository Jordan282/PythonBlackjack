import random

cardSuits = ["Diamonds", "Spades", "Hearts", "Clubs"]
cardList = ["Ace" , "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
deck = [(card, suit) for card in cardList for suit in cardSuits]
balance = 100

while balance > 0:
    def cardValue(card):
        if card[0] in ["Jack", "Queen", "King"]:
            return 10
        elif card[0] == "Ace":
            return 11
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
    
    print(balance)
    random.shuffle(deck)
    playerCards = [deck.pop(), deck.pop()]
    dealerCards = [deck.pop(), deck.pop()]

    while True:
        playerScore = sum(cardValue(card) for card in playerCards)
        dealerScore = sum(cardValue(card) for card in dealerCards)
        print("Player has:", playerCards)
        print("Player has a score of:", playerScore)
        print("\n")

        if playerScore > 21:
            break
    
        playerChoice = input("Would you like to hit or stand?:")
        if playerChoice == "hit":
            newCard = deck.pop()
            playerCards.append(newCard)
        elif playerChoice == "stand":
            break
        else:
            print("Invalid choice or incorrect spelling try again")
            continue

    while dealerScore < 17: 
        newCard = deck.pop()
        #dealerCards.append(newCard)
        dealerScore = dealerScore + cardValue(newCard)
        if dealerScore > 16:
            break
        elif dealerScore < 17:
            continue

    if playerScore > 21:
        print("Player has:", playerCards)
        print("Player has a score of:", playerScore)
        print("\n")
        print("Player is over the score of 21 and busts")
        print("Dealer wins")
    elif dealerScore > 21:
        print("Dealer has:", dealerCards)
        print("Dealers score is:", dealerScore)
        print("Dealer busts")
        print("Player wins!")
        balance = balance + playerBet * 2
    elif dealerScore < playerScore:
        print("Dealer has:", dealerScore, "Player has:", playerScore)
        print("Player wins!")
        balance = balance + playerBet * 2
    elif dealerScore > playerScore:
        print("Dealer has:", dealerScore, "Player has:", playerScore)
        print("Dealer wins!")
    elif playerScore == dealerScore:
        print("Player has:", playerCards)
        print("Player has a score of:", playerScore)
        print("\n")
        print("Dealer has:", dealerCards)
        print("Dealers score is:", dealerScore)
        print("\n")
        print("Both have the same score it's a tie...")
        balance = balance + playerBet

print("Say goodbye to your life savings...")



    




