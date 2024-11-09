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
        game_year.askHowManyAcresToSell()









####### SECOND QUESTION SELL LAND


# askHowManyAcresToSell(acresOwned)

####### THIRD QUESTION FEED PEOPLE





###### FOURTH QUESTION PLANT HARVEST











    # other methods go here

#    if __name__ == "__main__":
 #       hammurabi = Hammurabi()
  #      hammurabi.main()
if __name__ == "__main__":
    Play()