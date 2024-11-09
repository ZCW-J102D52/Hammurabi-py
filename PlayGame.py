import random
import os
import time

class Hammurabi:
    def __init__(self):
        self.rand = random.Random()

    def main(self):
        self.playGame()

    ### GLOBALS ###
    year = 1
    wallet = 2800
    population = 100
    acresOwned = 1000
    landValue = 19
    #########
    acresPlanted = 1000
    bushelsFed = 0
    harvest = 3000
    fertility = 3
    peopleStarved = 0
    immigrants = 5
    buschelRats = 200
    plagueDeaths = 0

    first_line = "O great Hammurabi! You are in year "+str(year)+" of your ten year rule."
    second_line = "In the previous year "+str(peopleStarved)+" people starved to death."
    third_line = "In the previous year, "+str(immigrants)+" people entered the kingdom."
    fourth_line = "The population is now "+str(population)+"."
    fifth_line = "We harvested "+str(harvest)+" bushels at "+str(fertility)+" bushels per acre."
    sixth_line = "Rats destroyed "+str(buschelRats)+" leaving "+str(wallet)+" bushels in storage."
    seventh_line = "The city owns "+str(acresOwned)+" acres of land."
    eighth_line = "Land is currently worth "+str(landValue)+" bushels per acre."
    gaps = "  //                                                                                    //"
    edge = "  ////////////////////////////////////////////////////////////////////////////////////////"


    ##def playGame(self):


    ##### Part One Questions Functions #####
    def sanityCheck(func):
        print("O great Hammurabi, you jest! That is impossible.")
        return func
    
    def clear_terminal():
        ##clears the screen
        os.system('cls' if os.name == 'nt' else 'clear')
    
    ####  Game Start ####
    #### Title Card ##
    print("  ////////////////////////////////////////////////////////////////////////////////////////")
    print("  //                                                                                    //")
    print("  //   ##  ##    ###    ##   ##  ##   ##  ##   ##  ######     ###    ######    ######   //")
    print("  //   ##  ##   ## ##   ### ###  ### ###  ##   ##   ##  ##   ## ##    ##  ##     ##     //")
    print("  //   ##  ##  ##   ##  #######  #######  ##   ##   ##  ##  ##   ##   ##  ##     ##     //")
    print("  //   ######  ##   ##  ## # ##  ## # ##  ##   ##   #####   ##   ##   #####      ##     //")
    print("  //   ##  ##  #######  ##   ##  ##   ##  ##   ##   ## ##   #######   ##  ##     ##     //")
    print("  //   ##  ##  ##   ##  ##   ##  ##   ##  ##   ##   ## ##   ##   ##   ##  ##     ##     //")
    print("  //   ##  ##  ##   ##  ### ###  ### ###   #####   #### ##  ##   ##  ######    ######   //")
    print("  //                                                                                    //")
    print("  ////////////////////////////////////////////////////////////////////////////////////////")
    print("                                    A game by Data 5.2")
    time.sleep(2)
    clear_terminal()
       
   
    def royal_report(y1,y2,y3,y4,y5,y6,y7,y8,e,g):
        print(e)
        print(g)
        print("  //",y1.center(82),"//")
        print("  //",y2.center(82),"//")
        print("  //",y3.center(82),"//")
        print("  //",y4.center(82),"//")
        print("  //",y5.center(82),"//")
        print("  //",y6.center(82),"//")
        print("  //",y7.center(82),"//")
        print("  //",y8.center(82),"//")
        print(g)
        print(e)

    royal_report(first_line,second_line,third_line,fourth_line,fifth_line,sixth_line,seventh_line,eighth_line,edge,gaps)
    
   

    # other methods go here

#    if __name__ == "__main__":
 #       hammurabi = Hammurabi()
  #      hammurabi.main()
