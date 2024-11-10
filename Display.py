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
        first_line = f"O great Hammurabi! You are in year {self.num_of_yrs} of your ten year rule."
        second_line = f"In the previous year {self.howManyPeopleStarved} people starved to death."
        third_line = f"In the previous year, {self.immigrants} people entered the kingdom."
        fourth_line = f"The population is now {self.population}."
        fifth_line = f"We harvested {self.harvest} bushels at {self.fertility} bushels per acre from {self.acresPlanted} acres."
        sixth_line = f"Rats destroyed {self.bushelRats} leaving {self.wallet} bushels in storage."
        seventh_line = f"The city owns {self.acresOwned} acres of land."
        eighth_line = f"Land is currently worth {self.landValue} bushels per acre."
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
        print("  //",seventh_line.center(82),"//")
        print("  //",eighth_line.center(82),"//")
        print(gaps)
        print(edge)
        

    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')