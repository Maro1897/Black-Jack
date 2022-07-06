
import random
from art import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card = random.choice(cards)
  return random_card


def calculete_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    sum(cards).remove(11)
    sum(cards).append(1)
  return sum(cards)
def compare(user_score, computer_score):
  if user_score == computer_score:
    return draw
  elif computer_score == 0:
    return "You lose computer has black jack"
  elif user_score == 0:
    return "You win, you have black jack"
  elif user_score>21:
    return "You lose"
  elif computer_score>21:
    return "You win"
  elif user_score>computer_score:
    return "You win"
  else:
    return "You lose"

def play_game():
  user_cards = []
  computer_cards = []
  is_game_over = False
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score = calculete_score(user_cards)
    computer_score = calculete_score(computer_cards)
    print(f"Your cards : {user_cards} current score : {user_score}")
    print(computer_cards[0])
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal=input("Type 'y' to take another card or 'n' to pass: ")
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  while computer_score !=0 and computer_score <17:
    computer_cards.append(deal_card())
    computer_score=calculete_score(computer_cards)
  
  print(user_score, computer_score, compare(user_score, computer_score))

while input("Do you want to play? Press 'y' for yes or 'n' for no"):
  play_game()
