import random
import os
import time
from Display import Display
from GameYear import GameYear

    ### GLOBALS ###
    
# wallet = 2800
    #population = 100
    #acresOwned = 1000
    #landValue = 19
    #########
    #acresPlanted = 1000
    #bushelsFed = 0
    #harvest = 3000
    #fertility = 3
    #peopleStarved = 0
    #immigrants = 5
    #buschelRats = 200
    #plagueDeaths = 0
    #bought_land = False
    #game_over = False

    ####  Game Start ####
    #### Title Card ##
Display.title_card()
def Play():
    game_year = GameYear()
    game_over = False
    while (game_over == False):
        
        print(str(game_year.wallet))
        ### FIRST SUMMARY ###       
        Display.royal_report(game_year)
        #game_over = game_year.game_over_check()
        #new year code here 
        game_over = True #for testing

    




###### FIRST QUESTION BUY LAND
        game_year.inventory()
        game_year.askHowManyAcresToSell()


        game_year.inventory()









####### SECOND QUESTION SELL LAND


# askHowManyAcresToSell(acresOwned)

####### THIRD QUESTION FEED PEOPLE





###### FOURTH QUESTION PLANT HARVEST











    # other methods go here
def askHowMuchGrainToFeedPeople(bushels):
  """Asks the players for the amount of grains they want to use to feed the population.
  Also check the input if it's valid and within the available bushels range.
  Arguments:
    bushels: The total number of bushels available for usage.
  Returns:
    The number of bushels the players wants to use to feed the population.
  """
  while True:
    try:
      ask_to_feed_population = int(input("How many bushels you want to use for feeding the population? "))
      if 0 <= ask_to_feed_population <= bushels:
        return ask_to_feed_population
      else:
        print(f"Please enter a number between 0 and available{bushels}.")
    except ValueError:
      print("Invalid input. Please enter a valid number.")
bushels_available =  2800
grain_to_feed_people = askHowMuchGrainToFeedPeople(bushels_available)
print(f"You will use {grain_to_feed_people} bushels to feed the people.")




NEW







#    if __name__ == "__main__":
 #       hammurabi = Hammurabi()
  #      hammurabi.main()
if __name__ == "__main__":
    Play()