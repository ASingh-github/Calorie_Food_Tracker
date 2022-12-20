from csv import writer
import csv
from Abstract import *
from Food import Food 
from SLDictionary import SLDictionary

class SLInventory(FoodInvAbstract):
  def __init__(self):  
   # self.fooditemList = []
    
    self.dictionary = SLDictionary()
   
####################################################################  
    #-Amrit
  def search_foodcode(self, foodcode):
      f = self.dictionary[foodcode] #uses _getitem to find foodcode and grabs foodobject in relation to that foodcode
      print(f.get_all_info())
    
###################################################################
    #-Carlos
  def search_fooditem(self, fooditem): 
      f = self.dictionary._find_name(fooditem)
      print(f.get_all_info())
###################################################################   
  
    #-Ben, Carlos , Amrit 
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

              
              self.dictionary._add(f.get_foodcode(),f)
          print("printing unsorted lists  \n")
          self.dictionary.printlist()
          print("\n")
          print("printing sorted lists \n")
          self.dictionary.sort_lists()
          
          
          
          self.dictionary.length()
          
  
            #self.KEY_unsortedListself.KEY_unsortedList.append(f.get_foodcode()) 
              #self.OBJ_unsortedList.append(f)
         # return(self.unsorted_Klist.self.KEY_unsortedlist)#testing prints, both work. obj prints food objects
          #
          #return(self.KEY_unsortedList)
           

  def printLists(self):
    self.dictionary.printlist()
   
    #-Carlos        
  def add_to_inventory(self,key, value):
    self.dictionary[key] = value
    return 
     
    #-Carlos
  def add_to_datafile(self, value):
    objlist = self.dictionary.ADD_list
    for f in objlist: # calling someting different 
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
            with open("Food_Database.csv", "a+") as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(fields)