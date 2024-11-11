import math
import random


class GameYear:
    def __init__(self,num_of_yrs=1,wallet=2800,belltoll="",plagueDead = 0,ohNo=10,acresOwned=1000,acresPlanted=1000,population=100,immigrants=5,bushelRats=200,howManyPeopleStarved=0,harvest=3000,fertility=3,landValue=19,bushelsFed=0):
        self.num_of_yrs = num_of_yrs
        self.wallet=wallet
        self.acresOwned=acresOwned
        self.population=population
        #####
        self.immigrants = immigrants
        self.harvest = harvest
        self.bushelRats = bushelRats
        self.fertility = fertility
        self.landValue = landValue
        self.bushelsFed = bushelsFed
        self.acresPlanted = acresPlanted
        self.howManyPeopleStarved = howManyPeopleStarved
        self.bought = False
        self.ohNo = ohNo
        self.plagueDead = plagueDead
        self.belltoll = belltoll

    def game_over_check (self):
        if (self.population <= 0):
            return True
        if (self.uprising == True):
            return True
        return False
    def inventory(self):
        inv = "Population: {population}  Bushels: {wallet}  Acres: {acresOwned}".format(**self.__dict__)
        y=f"YEAR:  {self.num_of_yrs}"
        gaps = "  //                                                                                    //"
        edge = "  ////////////////////////////////////////////////////////////////////////////////////////"
        print(edge)
        print(gaps)
        print(f"  //",y.center(82),"//")
        print(f"  //",inv.center(82),"//")
        print (gaps)
        print(edge)
        print()

    def endOfYear(self):
        self.num_of_yrs = self.num_of_yrs + 1
        if (self.num_of_yrs == 11):
            GameYear.youWin()

    def youWin(self):
        print("YOU WIN!!")

    def upLoss():
        print("Too many people starved and your people rose up, you lose")
    def noPop(self):
        print("All the citizens are dead. You lose")

        ######### Gabi ########
    def askHowManyAcresToSell(self):
        
        ## Could you please add a if that checks if self.bought == false, else pass? That way no one
        #can buy and sell on the same turn.
        if self.bought == True:
            pass
        else:
            print(f"You have {self.acresOwned} acres.")
            print(f"Land is valued at {self.landValue} bushels an acre.")
            land_to_sell = int(input("How many acres do you want to sell? "))
            while(land_to_sell > self.acresOwned):
            # print(str(land_to_sell) + " is more than you own")
                print(f"{land_to_sell} is more than you own")
                land_to_sell = int(input(f"How many acres do you want to sell? You have {self.acresOwned} acres."))
        # bushels = bushels + land_to_sell * 19 needs to be in the playGame method because we do not have wallet in this method
            self.acresOwned = self.acresOwned - land_to_sell
            self.wallet = self.wallet + land_to_sell * self.landValue

    def plagueDeaths(self):
        chanceOfPlagues = random.randint(1,100)
        if chanceOfPlagues < 16:
            # print("Plague got you this year. Half your population is dead.")
            ### I commented out the prints because this outcome is announced in the royal report
            self.ohNo = 20
            self.plagueDead = self.population  // 2
            return self.plagueDead
        else:
            # print("Good news! No plagues this year")
            return self.population    
        
        
    def starvationDeaths(self):
        minToSurvive = self.population * 20  #the min. to survive is the number of people * 20 bushels
        #Number of deaths due starvation
        if self.bushelsFed < minToSurvive:
            self.howManyPeopleStarved = math.ceil((minToSurvive - self.bushelsFed)/20) #math.ceil round up the number of dead people.
            # print("This many people starved " + str(howManyPeopleStarved)) 
            self.population = self.population-self.howManyPeopleStarved
            if self.population == 0:
                return True         
        return False
        
    def uprising(self):
        if self.howManyPeopleStarved > (self.population+self.howManyPeopleStarved* 0.45):
            return True  
        
        return False

        ####### Sharmin #######
    def askHowMuchGrainToFeedPeople(self):
        while True:
            pantry = int(input("How many bushels do you want to use for the people?  "))
            if pantry>self.wallet:
                print("As much as I wish it were true, it is not possible.")
                print("Please decree a new number, O Hammurabi.")
            if pantry<0:
                print("We cannot take from their homes. They depend on us, we must give.")
            if pantry>0 and pantry<= self.wallet:
                self.wallet = self.wallet - pantry
                self.bushelsFed = pantry
                return self.bushelsFed
    
    def getHarvest(self):
        self.fertility = random.randint(1, 7)
        self.harvest = self.acresPlanted * self.fertility

######## ULAS ##########

    def askHowManyAcresToPlant(self):
        while True:
            plan = int(input("How many acres you want to plant?"))
            if plan > self.acresOwned:
                print("You don't have enough acres!")
            elif plan > 10 * self.population:
                print("You don't have enough population!")
            elif 2*plan >self.wallet:
                print("You don't have enough grain!")
            else: 
                self.wallet = self.wallet - 2*plan
                self.acresPlanted = plan  
                return plan   
        
        

    def grainEatenByRats(self):
        x = random.randint(0, 100)
        if(x>40):
            self.bushelRats = 0
        else:
            loss = random.randint(1, 3)
            self.bushelRats = int((loss/10) * self.wallet)
            self.wallet = self.wallet - loss
            
    def newCostOfLand(self):
        self.landValue = random.randint(17, 23)

###### Maisha #######
    def askHowManyAcresToBuy(self):
        while True:  
            print(f"Land value is {self.landValue} per acre.")
            acres = int(input("How many acres of land would you like to buy?  "))
            if acres > 0 and acres * self.landValue <= self.wallet:
                self.bought = True
                self.acresOwned += acres
                self.wallet -= acres * self.landValue
                return acres
            elif acres < 0:
                print("Must enter a positive number to buy land.")
            elif self.landValue*acres > self.wallet:
                print("You don't have enough bushels to purchase. Try again! ")
            elif acres == 0:
                self.bought ==False
                return acres
        

    def getImmigrants(self):
        if self.howManyPeopleStarved == 0:
            self.immigrants = int((( 20*self.acresOwned + self.wallet) // (100 * self.population) + 1))
            self.population += self.immigrants 
