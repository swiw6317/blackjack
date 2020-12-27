
import random
game_finished=False
who_win=""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

answer = input("Do you want to play blackjack? y or n: ")
def sum_score(list_hand,player):
  global computer_hand
  global game_finished
  score=sum(list_hand)
  if player=="you" or player=="computer":
    if 11 in list_hand:
      if score>21:
       score-=10
    if score>=21:
       game_finished=True
  elif player=="computer_final":
    while score<17:
      computer_hand+= [random.choice(cards)]
      score=sum(list_hand)
      if 11 in list_hand:
       if score>21:
        score-=10
  return score

def win_calc():
 global game_finished
 global who_win
 if your_score==21 and computer_score!=21:
       game_finished=True
       who_win="You Win!"
 elif your_score>computer_score:
       game_finished=True
       who_win="You Win!"
 elif your_score==computer_score:
       game_finished=True
       who_win="Draw"
 elif your_score>21:
       game_finished=True
       who_win="You lost"
 elif your_score<computer_score:
       game_finished=True
       who_win="You lost"
 
computer_hand=[]
your_hand=[]
computer_hand= [random.choice(cards)]
for hand in range(2):
 your_hand+=[random.choice(cards)]
computer_score=sum_score(computer_hand,"computer")
your_score=sum_score(your_hand,"you")

while not game_finished:
  print(f"computer hand: {computer_hand} - computer score:{computer_score}")
  print(f"your hand: {your_hand} - your current score:{your_score}\n")
  next_card_answer=input("Do you want to take a new card? y or n: ")
  if next_card_answer=="y":
     your_hand+= [random.choice(cards)]
     your_score=sum_score(your_hand,"you")
  elif next_card_answer=="n":
     game_finished=True

computer_score=sum_score(computer_hand,"computer_final")
win_calc()
print(f"computer hand: {computer_hand} - computer score:{computer_score}")
print(f"your hand: {your_hand} - your current score:{your_score}\n")
print(who_win)
