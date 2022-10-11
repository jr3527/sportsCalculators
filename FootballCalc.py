""""  FootballCalc
      version 1.0 
      By: Jameson Ryley
      12/August/2017   """
import time
#################### variables  ####################
i = 0

#################### create a list of the city names for all of the NFL teams ####################
cityNames = [ "Arizona", "Atlanta", "Baltimore", "Buffalo", "Carolina", "Chicago",
              "Cincinnati", "Cleveland", "Dallas", "Denver", "Detroit", "Green Bay",
              "Houston", "Indianapolis", "Jacksonville", "Kansas City", "Los Angeles Rams",
              "Los Angeles Chargers", "Miami", "Minnesota", "New England", "New Orleans",
              "New York Jets", "New York Giants", "Oakland", "Philadelphia", "Pittsburgh",
              "San Francisco", "Seattle", "Tampa Bay", "Tennessee", "Washington" ]

# program welcome message for the user
print("Welcome to the Football Calculator")
print(time.ctime())

for value in range(32):
      # The user is first asked how many games the team has played or how big is the sample? This is
      # important because the calculations to come are based on this.
      # need to iterate through the array
      try:
        gamesPlayed = float(input("\nEnter how many games " +
                                cityNames[i].title() + " has played: "))
      except ValueError:
            print("You must enter a number! Please try again!")
            gamesPlayed = float(input("Enter how many games " +
                                cityNames[i].title() + " has played: "))


      try:
       rushingYards = float(input("Enter the number of rushing yards for " +
                                 cityNames[i].title() + ": "))
      except ValueError:
        print("You must enter a number! Please try again!")
        rushingYards = float(input("Enter the number of rushing yards for " +
                                 cityNames[i].title() + ": "))
      # the algorithm calls for rushing yards averaged by a team to by times by .08
      # totalRushingYards will be a point equivalent of the teams avg rushing yards times .08
      totalRushingYards = rushingYards * .08

      # rushing attempts for each team is input and the total will be times by .07
      rushingAttempts = float(input("Enter the number of rushing attempts per game for " +
                                    cityNames[i].title() + ": "))
      totalRushingAttempts = rushingAttempts * .07

      passingYards = float(input("Enter the number of passing yards for " +
                                 cityNames[i].title() + ": "))
      totalPassingYards = passingYards * .1

      # passing attempts for each team is input and the total will be times by -.33
      passingAttempts = float(input("Enter the number of passing attempts per game for " +
                                    cityNames[i].title() + ": "))
      totalPassingAttempts =  passingAttempts * -.33

      # interceptions thrown for each team is input and the total will be times by -1.6
      interceptions = float(input("Enter the number of interceptions per game for " +
                                  cityNames[i].title() + ": "))
      totalInterceptions = interceptions / gamesPlayed * -1.6

      # caused interceptions for each team is input and the total will be times by 3.1
      causedInterceptions = float(input("Enter the number of caused interceptions per game for " +
                                        cityNames[i].title() + ": "))
      totalCausedInterceptions = causedInterceptions / gamesPlayed * 3.1

      # fumbles for each team is input and the total will be times by -2.1
      fumbles = float(input("Enter the number of fumbles per game for " + cityNames[i].title() + ": "))
      totalFumbles = fumbles / gamesPlayed * -2.1

      # total caused fumbles for each team is input and the total will be times by 1.9
      causedFumbles = float(input("Enter the number of caused fumbles per game for " + cityNames[i].title() + ": "))
      totalCausedFumbles = causedFumbles / gamesPlayed * 1.9

      # missed field goals for each team is input and the total will be times by -4.2
      missedFieldGoals = float(input("Enter the number of missed field goals per game for " +
                                     cityNames[i].title() + ': '))
      totalMissedFieldGoals = missedFieldGoals / gamesPlayed * -4.2

      # this is the addition of all the calculations to come up with the final projected score
      projectedPoints = totalRushingYards + totalPassingYards + totalRushingAttempts + totalPassingAttempts + \
                        totalInterceptions + totalCausedInterceptions +\
                        totalCausedFumbles +totalFumbles + totalMissedFieldGoals

      # missed field goals for each team is input and the total will be times by -4.2
      testForHomeTeam = int(input("Are they playing at Home? If so, enter 1. If they are away, enter 2: "))

      # this is a test that will add 3 points for the home teams and subtract 3 points for an away team
      if testForHomeTeam == 1:     # if statement for whether user inputs home or away
          projectedPoints = projectedPoints + 3
      else:                        # anything else typed in by the user is considered an away team
          projectedPoints = projectedPoints - 3

      # this is the final print statement for the total for the team
      print(cityNames[i].title() + " has a projected total of: ", projectedPoints)
      i = i + 1       # this is an increment to move the loop to the next city in the teamNames list/array