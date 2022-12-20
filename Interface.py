from FoodInventory import FoodInventory
from Food import Food
from Foodlog import Foodlog


class Interface:  #amrit start

    @staticmethod
    #___________________________________________________________________________
    def food_interface_cl():
        print("***********************************************************")
        print("*   Welcome to the calorie tracker system   *")
        print("***********************************************************")
        print("")
        print(
            "[0] - exit program"
        )  #exits the program, adds any new foods to database or foodlog files
        print("[1] - search food")  #searches for food by food code or name
        print("[2] - add food to database"
              )  #adds user defined food into database
        print("[3] - food log ")  #need backend for this function stil

        fInventory = FoodInventory()  #new inventory object
        fInventory.create_inventory("Food_Database.csv")
        fFoodlog = Foodlog()
        fFoodlog.create_log("Food_Log.csv")
        #inventory is created using Food_Database.csv file
        #initial menu options are presented to user for input 
      #____________________________________________________________________________
        #This while loop controls the menu.

        menuoption = input("Please choose option:\n")
        if not menuoption:  #checks if empty string
            raise Exception("Empty String entered!")
        while menuoption != '0':
            assert menuoption == '1' or menuoption == '2' or menuoption == '3' or menuoption == '0'

            #If '0'(exit option): while loop exits(menu stops displaying)      #____________________________________________________________________________
            #asks user if searchng by food name or food code

            if menuoption == '1':
                searchoption = input("Would you like to search by food code" +
                                     " or by item name?\n" + "[1]Food name\n" +
                                     "[2]Food Code\n")
                #____________________________________________________________________________
                #User is prompted to enter food by name(search option '1')
                #if matching food is not found user is prompted to pick options again
                assert searchoption == '1' or searchoption == '2'
                if searchoption == '1':
                    fooditem = (str(input("Enter the name of the food: ")))
                    food = fInventory.search_fooditem(fooditem)

                    if food == None:
                        print("food not found! \n")

                    else:
                        food = fInventory.get_all_info(food)
# if  food is found, get all the info for the food.
#____________________________________________________________________________
#searching by food code (search option '2', same logic as search by food name above
                elif searchoption == '2':

                    foodcode = (str(input("Enter the code of the food: ")))
                    food = fInventory.search_foodcode(foodcode)

                    if food == None:
                        print("food not found ")
                    else:
                        food = fInventory.get_all_info(food)
#_________________________________________________________________________
#///adding new food to list

#creates a new food object for user to give attributes
            elif menuoption == '2':
                f = Food()
                # Carlos start
                f.set_fooditem(input("Enter the name of the new food: "))
                f.set_protein(
                    input("Enter the amount of protein in the food: "))
                f.set_calories(
                    input("Enter the amount of calories in the food:"))
                f.set_carbs(input("Enter the amount of carbs in the food:"))
                f.set_fats(input("Enter the amount of fats in the food: "))
                f.set_foodcode(input("Enter a new 5 digit food code: "))

                fInventory.add_to_inventory(f)
            #add_to_inventory function is called and creating a new list with foods added by user
#______________________________________________________________________________
            elif menuoption == '3':
                #food log functions go here
                assert menuoption == '1' or menuoption == '2' or menuoption == '3' or menuoption == '0'
                logoption = input(
                    "Would you like to search for a food to log, view the current log, or set/view your calorie goal?\n"  #ben adding calorie counting option 
                    + "[1]-search for a food to log\n" + "[2]-view log\n" +
                    "[3]-Set calorie goal\n")
                assert logoption == '1' or logoption == '2' or logoption == '3'
                if logoption == '1':
                    logsearch_option = input(
                        "Search for food by name or food code?\n" +
                        "[1]-food name\n" + "[2]-food code\n")

                    #searches by food name
                    #------------------------------------------------------------------------------
                    if logsearch_option == '1':
                        fooditem = (str(input("Enter the name of the food: ")))
                        food = fInventory.search_fooditem(
                            fooditem)  #searches by foodname

                        if food == None:
                            print("food not found! \n")

                        else:
                            fInventory.get_all_info(food)

                            addchoice = input(
                                "\ndo you want to add this food to foodlog?\n"
                                + "[1]-yes/n" + "[2]-no\n")

                            if addchoice == '1':  #user wants to add food to log

                                fFoodlog.add_to_loglist(food)

                            else:
                                pass

                    elif logsearch_option == '2':
                        foodcode = (str(input("Enter the code of the food: ")))
                        food = fInventory.search_foodcode(foodcode)

                        if food == None:
                            print("food not found ")
                        else:
                            fInventory.get_all_info(food)

                            addchoice = input(
                                "\ndo you want to add this food to foodlog?\n"
                                + "[1]-yes/n" + "[2]-no\n")

                            if addchoice == '1':  #user wants to add food to log

                                fFoodlog.add_to_loglist(food)
                            else:
                                pass

                elif logoption == '2':
                    print("**********************FOOD LOG" +
                          "**********************")
                    fFoodlog.display_foodlog()

                elif logoption == '3':
                    print("calorie counter goes here")  #ben calorie counter
                    fFoodlog.print_target_calories()

#_________________________________________________________________________
#last condition in while loop, refreshes menu options (small differences vs main that is presented prior to while loop)
            menuoption = input(
                "\nYou can search for another food, add a new food to data base, or acess the food log:"
                + "\n[0]-exit\n" + "[1]-search again\n" +
                "[2]-add new food\n" + "[3]-access food log\n")
            assert menuoption == '1' or menuoption == '2' or menuoption == '3' or menuoption == '0'
        if menuoption == '0':
            print("Thanks, Goodbye!")
            #foodlist= FoodInventory.__add_to_foodlist
            fInventory.add_to_datafile(
            )  # calls function to add user input to csv file
            fFoodlog.add_to_foodlog()  #adds user food choice to food_log


#add_to_datafile function is called taking data from add_to_foodlist[] and appending it to the next empty row in database file

#______________________________________________________________________________
if __name__ == "__main__":
    Interface.food_interface_cl()
