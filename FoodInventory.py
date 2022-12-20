from Food import Food
#from csv import writer
import csv
from Abstract import *


class FoodInventory(FoodInvAbstract):  #Ben Start
    #///constructor
    def __init__(self):
        self.__list_foods = []  #sets empty list to store foods in
        self.__add_to_foodlist = []  #sets empty list to store user input foods only
#----------------------------------------

#///search function

    def search_foodcode(
        self, foodcode
    ):  #with given food code, find matching foodcode from                                               list of foods
        foodcode = int(foodcode)
        for f in self.__list_foods:
            if f.get_foodcode() == (foodcode):
                return f
        return None
#----------------------------------------

    def search_fooditem(self, fooditem):
        for f in self.__list_foods:
            if f.get_fooditem() == str(fooditem):
                return f
        return None
#----------------------------------------

    def create_inventory(self, datafile):
        # Open the file for reading
        # loop through each line of the file
        # For each line, create a food object and add it to the list of food.
        with open(datafile) as csvfile:
            # Carlos Start
            # Reading every single line separately

            for line in csvfile:
                #words = line.split()
                words = line.strip().split(',')

                f = Food()
                #format for our lines:
                #Code, item, calories, protein, carb, fat
                #Carlos start
                f.set_foodcode(words[0])
                f.set_fooditem(words[1])
                f.set_calories(float(words[2]))
                f.set_protein(float(words[3]))
                f.set_carbs(float(words[4]))
                f.set_fats(float(words[5]))

                self.__list_foods.append(f)  #append f to list
#-----------------------------------------

    def add_to_inventory(self,
                         f):  # This function is to add user input to list

        # Made a new food list to store only the user input to append later
        # to csv file
        self.__add_to_foodlist.append(f)  # append user input to new list
        self.__list_foods.append(f)  # append user input to existing list
#-----------------------------------------

    def add_to_datafile(self):
        # This function is to get user input and adds it to the end of a csv file as a new line
        for f in self.__add_to_foodlist:
            # This is the new row that will be added to the csvfile
            fields = [
                f.get_foodcode(),
                f.get_fooditem(),
                f.get_calories(),
                f.get_protein(),
                f.get_carbs(),
                f.get_fats()
            ]
            if len(self.__add_to_foodlist) > 0:
                with open("Food_Database.csv", "a+") as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(fields)
                # Added the new row to the end of the csv file which is called when the user exits the program so it can be saved and used later if needed

#----------------------------------------------

    def get_all_info(self, f):
        print("-----Food Info----- \n" + "Food code: " +
              str(f.get_foodcode()) + "\nFood name: " + str(f.get_fooditem()) +
              "\nCalories: " + str(f.get_calories()) + "\nProtein: " +
              str(f.get_protein()) + "\nCarbs: " + str(f.get_carbs()) +
              "\nFats: " + str(f.get_fats()))


#displays all the food info of food object
#____________________________________________
