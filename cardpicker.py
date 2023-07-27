#Mechanics of card picker:
#Player has the option to pick a specific card or be given one at random
#Cards player has received will be added to his deck of cards

import random

Spades = ['S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'SJ', 'SQ', 'SK', 'SA']
Hearts = ['H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'HJ', 'HQ', 'HK', 'HA']
Clubs = ['C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'CJ', 'CQ', 'CK', 'CA']
Diamonds = ['D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'DJ', 'DQ', 'DK', 'DA']
fullDeckOfCards = Spades + Hearts + Clubs + Diamonds
playerDeck = []

def cardPicker():
    
    def playerPicks():
        print("You chose to pick a card")
        print("The following is the format in picking a card: ")
        print("Suits: Spades = S, Hearts = H, Clubs = C, Diamonds = D")
        print("Ranks: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A")
        print("Example: If you want Ace of Spades, type 'SA'")
        chosenCard = str(input("Pick a card: "))

        playerDeck.append(chosenCard)
        fullDeckOfCards.remove(chosenCard)

        print("Your current deck: " + str(playerDeck))
        pickAgain()
    
    def playerPicksAgain():
        chosenCard = str(input("Pick a card: "))

        if chosenCard in playerDeck:
            print("Pick another card, you already have that: ")
            playerPicksAgain()
        else:

            playerDeck.append(chosenCard)
            fullDeckOfCards.remove(chosenCard)

            print("Your current deck: " + str(playerDeck))
            pickAgain()

    def randomPicks():
        randomCard = random.choice(fullDeckOfCards)
        print("You were randomly assigned: " + randomCard)

        playerDeck.append(randomCard)
        fullDeckOfCards.remove(randomCard)

        print("Your current deck: " + str(playerDeck))
        pickAgain()

    def pickAgain():

        while True:
            print("Would you like to pick a card or be given one in random? (P/R)")
            print("(type Q to end the program)")
            playerChoice = str(input("Enter your choice: "))
            
            if playerChoice == 'P':
                playerPicksAgain()
                break
            elif playerChoice == 'R':
                randomPicks()
                break
            elif playerChoice == 'Q':
                break

            else:
                print("Invalid choice. Please enter 'P', 'R', or 'Q'")


    while True:
        print("Would you like to pick a card or be given one at random? (P/R)")
        playerChoice = input("Enter your choice: ")

        if playerChoice == 'P':
            playerPicks()
            break  
        elif playerChoice == 'R':
            randomPicks()
            break
        elif playerChoice == 'Q':
            break  
        else:
            print("Invalid choice. Please enter 'P', 'R', 'Q'")
    
cardPicker()