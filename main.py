from numpy.polynomial import Polynomial as P
from numpy.polynomial.polynomial import Polynomial as powerVal

import timeit

import big_o



def diceMath(x):
  diceSize = 6
  diceQuantity = x
  dropLowest = False
  diceTotal = diceSize**diceQuantity
  diceRange = diceSize*x
  a = diceSize + 1

  if(dropLowest == True):
    diceMin = (diceSize - diceSize +1)*(diceQuantity-1)
    diceMax = (diceQuantity-1)*diceSize
    
  if(dropLowest == False):
    diceMin = (diceSize - diceSize +1)*(diceQuantity)
    diceMax = (diceQuantity)*diceSize 

  refList = [[0]*a for i in range(a)]
  masterList = [[0]] * a
  powerList = [[]] * a
  diffList = [[]] * a
  sumList = 0
  oddsList = [0] * (diceRange+1)

  for x in range(0, a-1):
    refList[x][x+1] = 1
    refList[x] = P(refList[x])

  for x in range(0, a):
    tempList = [0] * (x +1)
    tempListOne = [1] * (a - x - 1)
    masterList[x] = tempList + tempListOne

  for x in range(0, a):
    powerList[x] = (P(masterList[x]))**diceQuantity

  
  if(dropLowest == True):
    for x in range(0, a-1):
      diffList[x] = ((powerList[x] - powerList[x+1])//refList[x])

    for x in range(0, a-1):
      sumList += diffList[x]

  if(dropLowest == False):
    sumList = powerList[0]

  
  for x in range(diceMin, diceMax+1):
    #  oddsList[x] = round(sumList.coef[x]/diceTotal, 4)*100
    oddsList[x] = round(sumList.coef[x]/diceTotal, 4)

  # print(oddsList)
  return(oddsList)



def chanceToHit(mat, defence):

  rollRequired = defence - mat
  rollResult = diceMath(2)
  oddsToHit = 0

  # print(rollRequired)
  # print(rollResult)
 
  for x in range(rollRequired, len(rollResult)):
    oddsToHit += rollResult[x]
  
  return(oddsToHit)


  



def chanceToDamage(arm, pAndS, health, numOfAttacks):
  numDice = numOfAttacks*2

  possibleDamage = diceMath(numDice)

  totalChanceKill = 0
  
  maxDamage = len(possibleDamage) - 1
  
  damage = [0]*maxDamage
  chanceOfDamage = [0]*maxDamage 

  if(maxDamage + numOfAttacks*(pAndS - arm) < health):
    print("too weak")
    return(0)
  
  for x in  range(0, maxDamage):
    damage[x] = x+1 + ((pAndS - arm)*numOfAttacks)
    chanceOfDamage[x]= (possibleDamage[x])

  for x in range(damage.index(health+1), len(possibleDamage)  ):
    totalChanceKill += possibleDamage[x]
  
  return(totalChanceKill)


def chanceToKill(mat, defense, arm, pAndS, health, numAttacks):

  chanceHit = chanceToHit(mat, defense)
  # chanceDamage = 0
  odds = 0
#HOW DO I HANDLE THE ODDS OF KILLING IN 1 HIT VS KILLING IN TWO? IF THERE ARE TWO ATTACKS, HOW DO I HANDLE THE CHANCE THAT 5 DAMAGE WILL BE DEALT IN JUST ONE HIT?? MAYBE ASK MARTIN, HES A GOOD DUDE
  for x in range(numAttacks, 0, -1):
    # odds += (chanceToDamage(arm, pAndS, health, x) - chanceToDamage(arm, pAndS, health, x-1))*chanceHit**x
    odds += ((chanceToDamage(arm, pAndS, health, x))*(chanceHit**x))

    print(x)
    print(chanceToDamage(arm, pAndS, health, x))
    # print(chanceToDamage(arm, pAndS, health, x-1))
    print(chanceHit)
    print(odds)
    print("loop")
    # print(odds)


  # print(chanceDamage)
  # print(chanceHit)

  print(odds)
  return(odds)


chanceToKill(6, 12, 18, 18, 5, 2 )








