####################
# SETUP
####################

# ==> IMPORT THE RANDOM LIBRARY
import random

# define constants
CARDS = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

# initialise variables
# ==> ASK THE USER TO INPUT THE NUMBER OF PLAYERS AND STORE IT AS AN INTEGER IN THE VARIABLE num_players
num_players = int(input())
hands = [[random.choice(CARDS), random.choice(CARDS)] for _ in range(num_players)] # initialises every players hand to 2 random cards
player = 0    # represents which player's go it is (player = 0 means player 1's turn)
done = [False for _ in range(num_players)]    # represents if each player has finished drawing cards using Boolean values
bust = [False for _ in range(num_players)]    # represents if each player has gone bust using Boolean values
valid_scores = []
winners = []


####################
# SUBPROGRAMS
####################

def getTotal(pHand):
  # ==> REARRRANGE THE LINES IN THIS SUBPROGRAM TO CALCULATE THE TOTAL VALUE OF THE HAND (PICTURE CARDS ARE WORTH 10)
  subtotal = 0
  for card in pHand:   
    if card == 'J' or card == 'Q' or card == 'K':  
      subtotal += 10    
    elif card == 'A':
      subtotal += 1
    else:
      subtotal += card
  return subtotal


####################
# MAIN PROGRAM
####################

while done != [True for _ in range(num_players)]:   # while there is at least 1 player who hasn't finished

  if done[player] == False:   # if this player isn't done

    print("Player", player + 1)
    input("Ready? ")
    print("Your hand is", hands[player])
    print("Total:", getTotal(hands[player]))

    # ==> ASK THE USER TO EITHER STICK OR TWIST AND STORE THEIR CHOICE IN THE VARIABLE choice
    choice = input("Stick or Twist?")

    if choice[0].lower() == "s":    # if the first character is 's' (case-insensitive) 
      # ==> SET THE PLAYER AS DONE (HINT: LOOK AT LINE 16)
      done[player] = True   

    elif choice[0].lower() == "t":    # if the first character is 't' (case-insensitive) 
      hands[player].append(random.choice(CARDS))    # add another random card to the player's hand

    print("\n"*100)   # 'clear' the terminal for the next player by printing 100 new line characters

    # ==> CHECK IF THE PLAYER'S TOTAL IS GREATER THAN 21 (HINT: LOOK AT LINE 48)
    if getTotal(hands[player]) > 21:
      print("Player", player + 1, "went bust")
      # ==> SET THE PLAYER AS DONE (HINT: LOOK AT LINE 16)
      done[player] = True  
      # ==> SET THE PLAYER AS BUST (HINT: LOOK AT LINE 17)
      bust[player] = True  

  player = (player + 1) % num_players   # move on to the next player with wrap-around


scores = [getTotal(hands[p]) for p in range(num_players)]   # create a list of scores

for index in range(len(scores)):    # loop through the scores
  # ==> CHECK IF PLAYER ISN'T BUST (HINT: LOOK AT LINE 17)
  if bust[index] == False:    
    # ==> ADD THIS SCORE TO THE LIST valid_scores
    valid_scores.append(scores[index])    
  else:
    # ==> ADD 0 TO THE LIST valid_scores
    valid_scores.append(0)    # invalid scores are considered as 0 so the lists match up

# ==> FIND THE MAXIMUM VALUE IN THE LIST valid_scores AND STORE IT IN THE VARIABLE highest_score
highest_score = max(valid_scores)

# ==> CHECK IF THE VARIABLE highest_score IS EQUAL TO 0
if highest_score == 0:
  print("All players went bust")

else:
  for index in range(len(valid_scores)):    # loop through the valid scores
    if valid_scores[index] == highest_score:    # if this player's score is the highest
      winners.append(index + 1)   # add it as a winner (adjusting for 0-based indexing)
      
  print("Winner(s): Player(s)", winners)