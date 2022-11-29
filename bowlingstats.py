import sys
import statistics

scores = []
games = int(input("Enter whole number of bowling games played from 1 to 12: "))
gameStr = str(games)
overE = "Error, a single game of bowling can not have a score over 300."
underE = "Error, a single game of bowling can not have a score under 0."

if games > 12:
  print("This program does not support over 10 games.")
  sys.exit()
elif games < 1:
  print("You can not play less than 1 full game of bowling.")
  sys.exit()
else:
  for i in range(0, games):   
    scoreIp = int(input("Enter whole number bowling game score: ")) 
  
    scores.append(scoreIp)

for score in scores:
  if (score > 300):
    print (overE)
    sys.exit()
  elif (score < 0):
    print (underE)
    sys.exit()

def totalScoreP():
  print ("Total score of the " + gameStr + " games of bowling:")
  print (sum(scores))

def totalScoreR():
  return sum(scores)

def avgScoreP():
  print ("Average score of the " + gameStr + " games of bowling:")
  print (statistics.mean(scores))

def medianScore():
  print("Median score of the " + gameStr + " games of bowling:")
  print (statistics.median(scores))

def highestScore():
  print ("Highest score is ")
  print (max(scores))

def modeScores():
  print ("Mode bowling scores are:")
  print (statistics.multimode(scores))

def sortScores():
  scores.sort()
  print ("List of scores from lowest to highest score.")
  print (scores)
  scores.sort(reverse = True)
  print ("List of scores from highest to lowest score.")
  print (scores)  

def perfectGames():
  if ((totalScoreR())/ games == 300):
    print ("You played a total of " + gameStr + " bowling games which all had a perfect score. This mean you had a perfect series.")
  else:
    for scorePerfect in scores:
      if scorePerfect == 300:
        print ("You had a perfect game of bowling.")

totalScoreP()
avgScoreP()
medianScore()
highestScore()
modeScores()
sortScores()
perfectGames()