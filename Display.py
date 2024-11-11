import os
import time

class Display:
    def title_card():
        Display.clear_terminal()
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
        Display.clear_terminal()

    def royal_report(self):
        Display.clear_terminal()
        
        Display.format_royal_report(self)
        time.sleep(3)
        print("")
        input("Press Enter to Continue".center(88)).lower()
        Display.clear_terminal()
    
    def format_royal_report(self):
        first_line = f"O great Hammurabi! You are in year {self.num_of_yrs} of your 10 year rule."
        second_line = f"In the previous year {self.howManyPeopleStarved} people starved to death."
        third_line = f"In the previous year, {self.immigrants} people entered the kingdom."
        fourth_line = f"The population is now {self.population}."
        fifth_line = f"We harvested {self.harvest} bushels at {self.fertility} bushels per acre from {self.acresPlanted} acres."
        sixth_line = f"Rats destroyed {self.bushelRats} leaving {self.wallet} bushels in storage."
        seventh_line = f"{Display.ohNosoDead(self)}"
        eighth_line = f"The city owns {self.acresOwned} acres of land."
        nineth_line = f"Land is currently worth {self.landValue} bushels per acre."
        gaps = "  //                                                                                    //"
        edge = "  ////////////////////////////////////////////////////////////////////////////////////////"

        print(edge)
        print(gaps)
        print("  //",first_line.center(82),"//")
        print("  //",second_line.center(82),"//")
        print("  //",third_line.center(82),"//")
        print("  //",fourth_line.center(82),"//")
        print("  //",fifth_line.center(82),"//")
        print("  //",sixth_line.center(82),"//")
        print("  //",seventh_line.center(82),"//") ## ppp
        print("  //",eighth_line.center(82),"//")
        print("  //",nineth_line.center(82),"//")
        print(gaps)
        print(edge)
        
    def ohNosoDead(self):
        if self.ohNo == 10:
            return "Thankfully the plague passed us by."
        if self.ohNo == 20:
            return f"Death visited us and took {self.plagueDead} to the grave."

    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    def starved():
        Display.clear_terminal()
        messedUp = "Because of your greed, your whole kingdom lies dormant and baren."
        messedUp2 = "Starvation has claimed them all, there is no one left to remember you."
        gg="GAME    OVER"
        print("  ////////////////////////////////////////////////////////////////////////////////////////")
        print("  //                                                                                    //")
        print("  //",messedUp.center(82),"//")
        print("  //",messedUp2.center(82),"//")
        print("  //                                                                                    //")
        print("  ////////////////////////////////////////////////////////////////////////////////////////")
        print("")
        print(gg.center(88))
        print("")

    def eatCake():
        Display.clear_terminal()
        messedUp = "Your choices have lead to the death of far too many citizens."
        messedUp2 = "Their surviving friends and family have come to the palace to exact their revenge."
        gg= "GAME    OVER"
        print("  ////////////////////////////////////////////////////////////////////////////////////////")
        print("  //                                                                                    //")
        print("  //",messedUp.center(82),"//")
        print("  //",messedUp2.center(82),"//")
        print("  //                                                                                    //")
        print("  ////////////////////////////////////////////////////////////////////////////////////////")
        print("")
        print(gg.center(88))
        print("")

    def youWin():
        Display.clear_terminal()
        bigWin = "Your choices have lead the kingdom to great prosperity!"
        bigWin2 = "The people of the land will revere your name forever!!"
        gg= "YOU    WIN"
        print("  ////////////////////////////////////////////////////////////////////////////////////////")
        print("  //                                                                                    //")
        print("  //",bigWin.center(82),"//")
        print("  //",bigWin2.center(82),"//")
        print("  //                                                                                    //")
        print("  ////////////////////////////////////////////////////////////////////////////////////////")
        print("")
        print(gg.center(88))
        print("")