from SLDictionary import SLDictionary
from SLInventory import SLInventory
from DictInventory import DictInventory
import csv
from Food import Food


#Using merge sort, good for list with large amount of entries.
#for faster search, we will implement binary search, since the list will be sorted
def main():
    sli = SLInventory()
  #this is one copy of the dictionary class. generally we would not call this class directly to make sure we keep up encapsulation.But this is good for testing.
    sld = SLDictionary()  
  #this is an instance of an inventory class. (this inventory class can also create dictionary objects)



    #sld.mergesort(test_array)
    sli.create_inventory("Food_Database.csv")  #mergesorts list of foodcodes
    #for now, also prints list of sorted foodcodes through the call "self.dictionary.sort_foodOBJlist"
    print("\nTesting adding food to inventory")
    print("---------------------------------------------")
    
    candy= Food() # creating a candy food object
    candy.set_foodcode(24311013)  #setting foodcode for the candy food object
    candy.set_fooditem("candy") #setting fooditem(name) of food object
    sli.add_to_inventory(candy.get_foodcode(),candy) # adding candy to inventory
    apple = Food() # another test for adding food object.
    apple.set_foodcode(13230499)
    apple.set_fooditem("apple")
    sli.add_to_inventory(apple.get_foodcode(),apple)
    pizza = Food()
    pizza.set_foodcode(99998211)
    pizza.set_fooditem("pizza")
    sli.add_to_inventory(pizza.get_foodcode(),pizza)
    ##sli.add_to_datafile("pizza") # This will put all the new food interies in the database
    #add to database works as far as I know, I have commented it out so we don't mess up our initial database until testing is needed.
    print("\nEnd testing add to inventory and adding to datafile")
    print("---------------------------------------------\n")
    
  
  # Testing for search by foodname
    print("Testing search fooditem")
    print("---------------------------------------------")
    print("searching for, candy, apple, goose wild roasted, and yeast")
    sli.search_fooditem("candy")     #works for sure 
    sli.search_fooditem("apple")
    sli.search_fooditem("Goose  wild  roasted")
    sli.search_fooditem("Yeast")
    print(" End testing search fooditem")
    print("---------------------------------------------")

    print("\nTesting search foodcode")
    print("---------------------------------------------\n")
    print("searching for, goose wild roasted, chroizo, Plum, yeast, pizza, apple, candy")
    
    sli.search_foodcode(24311010) 
    sli.search_foodcode(25220710)
    sli.search_foodcode(63143010)
    sli.search_foodcode(75236000)
    sli.search_foodcode(99998211)
    sli.search_foodcode(13230499)
    sli.search_foodcode(24311013)
    print("\nend testing searchfoodcode")
    print("---------------------------------------------")    
    #NOTE DONT ADD FOODCODES STARTING WITH 9!! breaks code for some reason 
    
    ###########################################################
    #testing the internal add function of dictionary only
    beef = Food()
    beef.set_fooditem("beef")    
    chicken = Food()
    chicken.set_fooditem("chicken")
    burger = Food()
    burger.set_fooditem("burger")
    
    waffle = Food()
    waffle.set_fooditem("waffle")
    sld._add(1234,beef)
    sld._add(4321,chicken)
    sld._add(5678,burger)
    sld._add(1345,waffle)
    
    #foundFood=sld._find(4321)
    #print(foundFood)
    print("")
    print("Testing the pop in Dictionary, popping beef foodcode:1234")
    print("Lists before pop: \n")
    print(sld.KEY_list)
    print(sld.OBJ_list)
    print("\n")
    sld.pop(1234)
    print("Lists after pop\n")
    print(sld.KEY_list)
    print(sld.OBJ_list)
    #print(foundFood.get_all_info())#making sure the object returned from _find is correct one
    #Testing the add to datafile function from inventory
    
    

##############################################################


  
if __name__ == "__main__":
  main()
