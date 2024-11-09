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
    
    def askHowManyAcresToSell(self):
        print("You have " + str(self.acresOwned) + " acres.")
        land_to_sell = int(input("How many acres do you want to sell? "))
        while(land_to_sell > self.acresOwned):
            print(str(land_to_sell) + " is more than you own")
            land_to_sell = int(input("How many acres do you want to sell? You have " + str(self.acresOwned) + " acres."))
        # bushels = bushels + land_to_sell * 19 needs to be in the playGame method because we do not have wallet in this method
            self.acresOwned = self.acresOwned - land_to_sell
            #### Function still needs the money earned from the sale to be added to the wallet.

        
