import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while play == "y" :  
  user_cards = []
  comp = []
  c1 = random.choice(cards)
  c2 = random.choice(cards)
  user_cards += [c1]
  user_cards += [c2]
  print(f"  Your cards: {user_cards}, current score: {c1+c2}")
  comp1 = random.choice(cards)
  comp += [comp1]
  print(f"  Computer's first card: {comp1}")
  play1 = input("Type 'y' to get another card, type 'n' to pass: ")
  c3 = 0
  if play1=="y" :
    c3 = random.choice(cards)
    user_cards += [c3]
  print(f"  Your cards: {user_cards}, current score: {c1+c2+c3}")
  print(f"  Computer's first card: {comp1}")
  print(f"Your final hand: {user_cards}, final score: {c1+c2+c3}")
  comp2 = random.choice(cards)
  comp += [comp2]
  if comp1+comp2 < c1+c2+c3 or comp1+comp2<17:
    comp3 = random.choice(cards)
    comp += [comp3]
    score = comp1 + comp2 + comp3
  print(f"Computer's final hand: {comp}, final score: {score}")
  if 11 in user_cards and c1+c2+c3>21:
   c1 = c1 - 10
  if 11 in comp and score>21:
   score = score - 10
  if c1+c2+c3 > 21:
   print("You went over. You lose 😭")
  elif score>21:
    print("You win!")
  elif score>c1+c2+c3:
   print("You lose 😭")
  else:
   print("You win!")
   play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
