'''
-.-.-.-.-.-.-.-.-.-.-.-.Blackjack Project.-.-.-.-.-.-.-.-.-.-.-.-

Our Blackjack House Rules

# The deck is unlimited in size. 
# There are no jokers. 
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:

# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
'''
from art import logo
import random
from replit import clear
#The deal_card() function returns a random card from the deck.
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  #11 is the Ace.
  card = random.choice(cards)
  return card
  
#calculate_score() that takes a List of cards as input
#Check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
#calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  elif sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
  
#compare() passes in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  if user_score == computer_score:
    return "It's a draw! 😒"
  elif computer_score == 0:
    return "Lose! Opponent has blackjack 😱"
  elif user_score == 0:
    return "Win with a blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose! 😭"
  elif computer_score > 21:
    return "Opponent went over. You win! 🤩"
  elif user_score > computer_score:
      return "You win! 😁"
  else:
      return "You lose! 😤"
    
#Deal the user and computer 2 cards each using deal_card() and append().
def play_blackjack():
  print(logo)
  user_cards = []
  computer_cards = []
  
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    #If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    #The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"  Your cards: {user_cards}, Current score: {sum(user_cards)}")
    print(computer_cards)
    print(f"  Computers first card: {computer_cards[0]}")
    
    #If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    if computer_score == 0 or user_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      elif user_should_deal == 'n':
        is_game_over = True
      else:
        print("Please provide a valid input")
  
  #Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"  Your final hand: {user_cards}, Final score: {user_score}")
  print(f"  Your final hand: {computer_cards}, Final score: {computer_score}")
  print(compare(user_score, computer_score))

#Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
play_more = True

while play_more:
  if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    play_blackjack()
  else:
    print("See you later, friend! 🤝")
    play_more = False
