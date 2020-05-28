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
    oddsList[x] = round(sumList.coef[x])

  
  return(oddsList)

# totalSize = diceMath(8)

#print(oddsList)


# def chanceHit(mat, defence):


def chanceKill(arm, pAndS, health, numOfAttacks):
  numDice = numOfAttacks*2

  possibleDamage = diceMath(numDice)

  print(possibleDamage)
  
  maxDamage = len(possibleDamage) - 1

  print(maxDamage)

  values = [[]]

  if(maxDamage + numOfAttacks*(pAndS - arm) < health):
    print("too weak")
    return(0)

  

  for x in  range(0, maxDamage):
    values[x] = x
    values[x][x] = possibleDamage[x] - (pAndS - arm)
  

  print(values)


chanceKill(20, 18, 25, 3)










