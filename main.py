from HTDictionary import HTDictionary
from HTInventory import HTInventory
from DictInventory import DictInventory
import csv
from Food import Food
from Abstract import *

def main():
  print("_______________________________")
  print("Start testing create inventory")

  
  H = HTDictionary()
  HI = HTInventory()
  HI.create_inventory("Food_Database.csv")

  
  print("end testing create inventory") 
  print("_______________________________")
  print("Start testing adding foods to inventory")


  candy= Food() # creating a candy food object
  candy.set_foodcode(24311013)  #setting foodcode for the candy food object
  candy.set_fooditem("candy")
  HI.add_to_inventory(candy.get_foodcode(),candy)
  juice= Food() # creating a juice food object (this was needed to test add to data file since candy gets popped)
  juice.set_foodcode(28351172)  #setting foodcode for the juice food object
  juice.set_fooditem("juice") 
  HI.add_to_inventory(juice.get_foodcode(),juice)

  print("\nsearch for these added foods is in search testing\n")
  
  print("end testing adding foods to inventory")
  print("_______________________________")
  print("start testing search foodcode")
  
 
  HI.search_foodcode(11350000)
  #HI.search_foodcode(11350000)
  print("\nsearching for foods that were just added to inventory\n")
  HI.search_foodcode(24311013) # searching for foods that were just added
  HI.search_foodcode(28351172) # searching for foods that were just added
   

  print("end testing search foodcode")
  print("_______________________________")
  print("Start testing length function")
  HI.length()

  
  print("Start testing seach by foodname")
  print("search for a fooditem here\n")
  HI.search_fooditem("Tequila")
  #HI.search_fooditem("egg") #uncomment this code to test for food that doesn't exist
  
  print("end testing search food item")
  print("_______________________________")
  
  print("start testing pop")
  
  HI.del_from_inventory(24311013) #trying to delete candy out of inventory

  print("end testing pop")
  print("_______________________________")
  print("testing add to datafile")
  print("\nplease uncomment next line to test datafile write back\n")
  #HI.add_to_datafile() #uncomment this line to test writeback to file
  
  print("end testing add to data file")
  print("_______________________________")
  
if __name__ == "__main__":
  main()
