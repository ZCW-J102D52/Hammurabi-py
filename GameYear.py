
class GameYear:
    def __init__(self,num_of_yrs=1,wallet=2800,acresOwned=1000,population=100,immigrants=5,bushelRats=200,peopleStarved=0,harvest=3000,fertility=3,landValue=19,):
        self.num_of_yrs = num_of_yrs
        self.wallet=wallet
        self.acresOwned=acresOwned
        self.population=population
        self.uprising = False
        #####
        self.peopleStarved = peopleStarved
        self.immigrants = immigrants
        self.harvest = harvest
        self.bushelRats = bushelRats
        self.fertility = fertility
        self.landValue = landValue

    def game_over_check (self):
        if (self.population <= 0):
            return True
        if (self.uprising == True):
            return True
        return False
    def inventory(self):
        inv = "Population: {population}  Money: {wallet}  Acres: {acresOwned}".format(**self.__dict__)
        y=f"YEAR: {self.num_of_yrs}"
        gaps = "  //                                                                                    //"
        edge = "  ////////////////////////////////////////////////////////////////////////////////////////"
        print(edge)
        print(gaps)
        print(f"  //",y.center(82),"//")
        print(f"  //",inv.center(82),"//")
        print (gaps)
        print(edge)
        print()
        print()

    def askHowManyAcresToSell(self):
        print(f"You have {self.acresOwned} acres.")
        land_to_sell = int(input("How many acres do you want to sell? "))
        while(land_to_sell > self.acresOwned):
            # print(str(land_to_sell) + " is more than you own")
            print(f"{land_to_sell} is more than you own")
            land_to_sell = int(input(f"How many acres do you want to sell? You have {self.acresOwned} acres."))
        # bushels = bushels + land_to_sell * 19 needs to be in the playGame method because we do not have wallet in this method
        self.acresOwned = self.acresOwned - land_to_sell
            #### Function still needs the money earned from the sale to be added to the wallet.
        
    # other methods go here
    def askHowMuchGrainToFeedPeople(self):
#   """Asks the players for the amount of grains they want to use to feed the population.
#   Also check the input if it's valid and within the available bushels range.
#   Arguments:
#     bushels: The total number of bushels available for usage.
#   Returns:
#     The number of bushels the players wants to use to feed the population.
#   """
        while (self.population >0):
            try:
                ask_to_feed_population = int(input("How many bushels you want to use for feeding the population? "))
                if ask_to_feed_population <= self.wallet:
                    return ask_to_feed_population
                else:
                    print(f"Please enter a number between 0 and available{self.wallet}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
# bushels_available =  2800
# grain_to_feed_people = askHowMuchGrainToFeedPeople(bushels_available)
# print(f"You will use {grain_to_feed_people} bushels to feed the people.")

        
