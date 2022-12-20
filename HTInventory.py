from csv import writer
import csv
from Abstract import *
from Food import Food
from HTDictionary import HTDictionary


class HTInventory(FoodInvAbstract):
######################################################### 
    def __init__(self):

        self.dictionary = HTDictionary()  #instance of the class HTDictionary

######################################################### 
    def length(self):
      self.dictionary.length()
      pass
      
######################################################### 
    #-amrit
    def search_foodcode(self, foodcode):
        f = self.dictionary[foodcode]  #Grab object in relation to foodcode user searched for
        print(f.get_all_info())
        return f


      
######################################################### 
    def search_fooditem(self, fooditem): #- Carlos 
       f = self.dictionary._find_name(fooditem) # Grab the object in relation to the food name uswer searched for 
       print(f.get_all_info())
       return f


######################################################### 
      
    def create_inventory(self, datafile):
        #-Amrit
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
                self.dictionary._add(
                    f.get_foodcode(),
                    f)  #call to _add to add food and key into hashtable
        self.dictionary._printlists(
        )  #uncomment this code to print lists to see
        #if inventory is correctly populated
        self.dictionary.length() 

######################################################### 
      #-amrit
    def add_to_inventory(self, key, value):
        self.dictionary[key] = value
        return

######################################################### 
  #-amrit
    def del_from_inventory(self,key):
      f = self.dictionary.pop(key) #calls pop in dictionary
      print("the following food was deleted from inventory: ")
      print(f.get_all_info())
      return
      
#########################################################  
      #-amrit
    def add_to_datafile(self):
        objlist = self.dictionary.ADD_list
        for f in objlist:  # calling someting different
            # This is the new row that will be added to the csvfile
            fields = [
                f.get_foodcode(),
                f.get_fooditem(),
                f.get_calories(),
                f.get_protein(),
                f.get_carbs(),
                f.get_fats()
            ]
            #if len(objlist) > 0:
            with open("Short_Food_Database.csv", "a+") as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(fields)
        return

#################################################################################