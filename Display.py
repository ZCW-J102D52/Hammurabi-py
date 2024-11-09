import os
import time

class Display:
    def title_card():
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

    def royal_report(year_object):
        Display.format_royal_report(year_object)
    
    def format_royal_report(year_object):
        first_line = "O great Hammurabi! You are in year "+str(year_object.num_of_yrs)+" of your ten year rule."
        second_line = "In the previous year "+str(year_object.peopleStarved)+" people starved to death."
        third_line = "In the previous year, "+str(year_object.immigrants)+" people entered the kingdom."
        fourth_line = "The population is now "+str(year_object.population)+"."
        fifth_line = "We harvested "+str(year_object.harvest)+" bushels at "+str(year_object.fertility)+" bushels per acre."
        sixth_line = "Rats destroyed "+str(year_object.bushelRats)+" leaving "+str(year_object.wallet)+" bushels in storage."
        seventh_line = "The city owns "+str(year_object.acresOwned)+" acres of land."
        eighth_line = "Land is currently worth "+str(year_object.landValue)+" bushels per acre."
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