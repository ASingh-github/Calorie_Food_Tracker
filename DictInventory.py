from csv import writer
import csv
from Dictionary import Dictionary
from Abstract import *
from Food import Food


class DictInventory(FoodInvAbstract):
#####################################################
  #creates 2 linked lists, one for runtime operations(searching), one for writing back to database file after program is done running.
    def __init__(self):
        self.__food_dict = Dictionary()
        self.__data_dict = Dictionary() #amrit
#####################################################      #amrit
     #searches for food object using foodcode(key) 
    def search_foodcode(self, foodcode):
      
        f = self.__food_dict[foodcode] #searching foodcode using magic method get_item.
        #print("foodcode exists")
        print(f.get_all_info()) #prints all attributes of food object if it is found.

##########################################################searches for fooditem by name (not needed but kept the implementation since it does work)
   # - Carlos Start
    def search_fooditem(self, foodname):
          f = self.__food_dict._findname(foodname)
          #print("fooditem exists")
          print(f.get_all_info())
            # Carlos End 

###########################################################
# -  Carlos Start 
    def create_inventory(self, datafile):
        # Reading the file , looping through each line of the file
        # For each line , create a food object and add it to the dictionary object

        with open(datafile) as csvfile:
            for line in csvfile:
                words = line.strip().split(',')

                f = Food()

                f.set_foodcode(words[0])
                f.set_fooditem(words[1])
                f.set_calories(float(words[2]))
                f.set_protein(float(words[3]))
                f.set_carbs(float(words[4]))
                f.set_fats(float(words[5]))

                
                self.__food_dict._add(f.get_foodcode(), f)
# - Carlos End 
###########################################################

    def add_to_inventory(self, f):
        self.__food_dict._add(f.get_foodcode(), f)
        self.__data_dict._add(f.get_foodcode(),f)

##########################################################
    #adds to datafile any foods the user has input during run time, works only for food database current.
    def add_to_datafile(self):
        current = self.__data_dict.head #amrit
        while current != None:

            fields = [
                current.val.get_foodcode(),
                current.val.get_fooditem(),
                current.val.get_calories(),
                current.val.get_protein(),
                current.val.get_carbs(),
                current.val.get_fats()
            ]
            current = current.next
            #    if len(self.__add_to_foodlist) > 0:
            with open("Food_Database.csv", 'a+') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(fields)

##############################################
    #amrit
    def printinventory(self):
        self.__food_dict.print_Llist()
        print("The size of list is:\n")
        print(self.__food_dict.__len__())


################################################
