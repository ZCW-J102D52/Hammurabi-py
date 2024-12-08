from Display import Display
from GameYear import GameYear


####  Game Start ####
#### Title Card ##

if __name__ == "__main__":
        Display.title_card()
        game_year = GameYear()
        game_over = False      
        ### SUMMARY ###       
        
        #game_over = game_year.game_over_check() 

        # game_over = True #for testing
###### FIRST QUESTION BUY LAND

        while (game_over == False):
                Display.royal_report(game_year)
                Display.clear_terminal()
                game_year.inventory()
                game_year.askHowManyAcresToBuy()


# ####### SECOND QUESTION SELL LAND
                Display.clear_terminal()
        
                game_year.inventory()
                game_year.askHowManyAcresToSell()


# ####### THIRD QUESTION FEED PEOPLE
                Display.clear_terminal()
                game_year.inventory()    
                game_year.askHowMuchGrainToFeedPeople()


###### FOURTH QUESTION PLANT HARVEST
                Display.clear_terminal()
                game_year.inventory()
                game_year.askHowManyAcresToPlant()

# ###### Plague Death
                game_year.plagueDeaths() 
# ###### Starvation
                game_over = game_year.starvationDeaths()   
# ###### Uprising
                if (game_over == True):
                        Display.starved()
                if (game_over == False):
                        game_over=game_year.uprising()
# ###### Immigrants 
                        if (game_over == True):
                                Display.eatCake()
                        if (game_over == False):
                                game_year.getImmigrants()
# ###### Harvest
                                game_year.getHarvest()
# ###### RATS
                                game_year.grainEatenByRats()
# ###### Land Value
                                game_year.newCostOfLand()

##### End of Year #####
                                game_over=game_year.endOfYear()
                                if (game_over == True):
                                        Display.youWin()
                                        



