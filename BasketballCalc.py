""""  BasketballCalc
      version 1.0
      By: Jameson Ryley
      13/January/2017   """
import time

# program welcome message for the user
print("Welcome to the Basketball Calculator \n")
print(time.ctime())
    #The user is asked to enter the city name of the team

cityName = input("\nWhat is the city name of the Team?: ")


# The user is first prompted for the first statistics which are Three Point shot attempts and percentage per game
while True:
    try:
        twoPointAttempts = float(input("Enter the number of Two Point shots per game for " +
                                 cityName + ": "))
        break

    except ValueError:
        print("Oops! That was not a valid number. Try again!")

# the algorithm calls for two point shot attempts averaged by a team to by times their two points percentage
while True:
    try:
        twoPointPercentage = float(input("Enter the Two Point shot percentage per game for " +
                                     cityName  + ". This must be a decimal to two places! Ex.- .43: "))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again!")

totalTwoPoints = twoPointAttempts * twoPointPercentage * 2

# The user is prompted for the second statistics which are Three Point shot attempts and percentage per game

while True:
    try:
        threePointAttempts = float(input("Enter the number of Three Point shots per game for " +
                                       cityName + ": "))
        break

    except ValueError:
        print("Oops! That was not a valid number. Try again!")

# the algorithm calls for three point shot attempts averaged by a team to by times their three point percentage
while True:
    try:
        threePointPercentage = float(input("Enter the Three Point shot percentage per game for " +
                                         cityName + " This must be a decimal to two places! Ex.- .43: "))
        break
    except ValueError:
        print("Oops! That was not a valid number. Try again!")

totalThreePoints = threePointAttempts * threePointPercentage * 3

while True:
    try:
# The user is prompted for the second statistics which are Three Point shot attempts and percentage per game
        freeThrowAttempts = float(input("Enter the number of Free Throw Attempts per game for " +
                                      cityName + ": "))
        break

    except ValueError:
        print("Oops! That was not a valid number. Try again!")
# the algorithm calls for free throw shot attempts and free throw averages per game
while True:
    try:
        freeThrowPercentage = float(input("Enter the Free Throw percentage per game for " +
                                        cityName + " This must be a decimal to two places! Ex.- .43: "))
        break

    except ValueError:
        print("Oops! That was not a valid number. Try again!")
totalFreeThrowPoints = freeThrowAttempts * freeThrowPercentage


# this is the addition of all the calculations to come up with the final projected score for each city
projectedPoints = totalTwoPoints + totalThreePoints + totalFreeThrowPoints

# If they are playing at home they get +4 points. It is -4 for an away team.
testForHomeTeam = int(input("Enter 1 if they are playing at Home? Otherwise, enter 2:"))

# this is a test that will add 3 points for the home teams and subtract 3 points for an away team
if testForHomeTeam == 1:     # if statement for whether user inputs home or away
    projectedPoints = projectedPoints + 4
else:                        # anything else typed in by the user is considered an away team
    projectedPoints = projectedPoints - 4

# this is the final print statement for the total for the team
print( cityName + " has a projected total of: ", projectedPoints)