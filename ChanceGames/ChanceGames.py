import random
import os
import math

money = 100

# function for Coin Flip
def coinFlip(betAmount, prediction, money):
  coinNum = random.randint(1,2)

  if coinNum == 1:
    coin = "Heads"
    print("Coin: Heads")
    if prediction == coin:
      print("+{}".format(betAmount))
      money += betAmount
    else:
      print("-{}".format(betAmount))
      money -= betAmount
  elif coinNum == 2:
    coin = "Tails"
    print("Coin: Tails")
    if prediction == coin:
      print("+{}".format(betAmount))
      money += betAmount
    else:
      print("-{}".format(betAmount))
      money -= betAmount
  return (money)

# function for ChoHan
def choHan(betAmount, prediction, money):
  diceOne = random.randint(1,6)
  diceTwo = random.randint(1,6)

  diceTotal = diceOne + diceTwo
  dicePredict = diceTotal % 2

  print("Dice total is {}".format(diceTotal))
  if dicePredict == 0:
    dice = "Even"
    if prediction == dice:
      print("+{}".format(betAmount))
      money += betAmount
    else:
      print("-{}".format(betAmount))
      money -= betAmount
  elif dicePredict > 0:
    dice = "Odd"
    if prediction == dice:
      print("+{}".format(betAmount))
      money += betAmount
    else:
      print("-{}".format(betAmount))
      money -= betAmount
  return money

# function for HigherLower
def higherLower(betAmount, prediction, playerNum, money):
  opponent = random.randint(1,10)
  player = playerNum

  print("Opponents number: {}".format(opponent))
  print("Your number: {}".format(player))
  print()
  
  
  if opponent > player:
      if prediction == 'lower':
        print("Your opponent wins!")
        print("-{}".format(betAmount))
        money -= betAmount
      elif prediction == 'higher':
        print("You win!")
        print("+{}".format(betAmount))
        money += betAmount
      elif prediction == 'equal':
        print("Your opponent wins!")
        print("-{}".format(betAmount))
        money -= betAmount
  elif opponent < player:
      if prediction == 'lower':
          print("You win!")
          print("+{}".format(betAmount))
          money += betAmount
      elif prediction == 'higher':
          print("Your opponent wins!")
          print("-{}".format(betAmount))
          money -= betAmount
      elif prediction == 'equal':
          print("Your opponent wins!")
          print("-{}".format(betAmount))
          money -= betAmount
  elif opponent == player:
      if prediction == 'lower':
          print("Your opponent wins!")
          print("-{}".format(betAmount))
          money -= betAmount
      elif prediction == 'higher':
          print("Your opponent wins!")
          print("-{}".format(betAmount))
          money -= betAmount
      elif prediction == 'equal':
          print("You win!")
          print("+{}".format(betAmount))
          money += betAmount
     

  return money
    
    
   

running = True


while running == True:

  print("Welcome to the games of chance! Our games are ChoHan, Coin Flip, and HigherLower")

  gameChoice = input("Please choose which game you would like to play. ").lower()
  print()
  print("Your current money: {}".format(money))
  print()
  print()

  if (gameChoice != "coin flip") and (gameChoice != "chohan") and (gameChoice != "higherlower"):
      gameChoice = input("That is not a game option, please choose again.")
      print()

  if gameChoice == "coin flip":
      print("You are playing Coin Flip")
      playerBet = int(input("Please enter your bet amount: "))
      
      if playerBet > money:
          playerBet = int(input("You don't have that much! Please choose a different amount. "))
      
      if playerBet <= 0:
          playerBet = int(input("I'm sorry, you can not bet that amount, please choose a different amount. "))

      print()

      print("In Coin Flip you must choose head or tails. If your guess is correct, you win!")
      print()
      playerPrediction = input("Do you guess heads or tails? ").capitalize()

      if (playerPrediction != 'Heads') and (playerPrediction != 'Tails'):
          playerPrediction = input("That is not an answer, please choose heads or tails. ")

      print()

      money = coinFlip(playerBet, playerPrediction, money)
      print()

  if gameChoice == "chohan":
      print("You are playing ChoHan")
      playerBet = int(input("Please enter your bet amount: "))

      if playerBet > money:
          playerBet = int(input("You don't have that much! Please choose a different amount! "))
      
      if playerBet <= 0:
          playerBet = int(input("I'm sorry, you can not bet that amount, please choose a different amount! "))

      print()
      print("In Chohan you will roll two die. The outcome of those dice will be added together. You must guess if the sum is an even or odd number. If your guess if correct, you win!")
      print()
      playerPrediction = input("Do you guess even or odd? ").capitalize()

      if (playerPrediction != 'Even') and (playerPrediction != 'Odd'):
          playerPrediction = input("That is not an answer, please choose even or odd. ")

      print()

      money = choHan(playerBet, playerPrediction, money)
      print()

  if gameChoice == "higherlower":
      print("You are playing HigherLower, good luck!")
      playerBet = int(input("Please enter your bet amount: "))

      if playerBet > money:
          playerBet = int(input("You don't have that much! Please choose a different amount! "))
      
      if playerBet <= 0:
          playerBet = int(input("I'm sorry, you can not bet that amount, please choose a different amount! "))

      print()
      print("In HigherLower you must choose a number between 1 and 10. Your opponent (computer) will also generate a number between 1 and 10. You then guess if your number is higher, lower, or equal to your opponents. Only if you are correct, you win!")
      print()
      playerNumber = int(input("Please choose your number 1-10: "))

      if (playerNumber > 10) or (playerNumber < 1):
          playerNumber = int(input("Please choose a number between 1 and 10. "))

      print("You chose ", playerNumber)
      print()
      playerPrediction = input("Will your opponents number be higher, lower, or equal? ").lower()

      if (playerPrediction != 'higher') and (playerPrediction != 'lower') and (playerPrediction != 'equal'):
          playerPrediction = input("That is not an answer, please choose higher, lower, or equal. ")

      print()

      money = higherLower(playerBet, playerPrediction, playerNumber, money)
      print()

  stop = input("Press ENTER to continue")
  print()
