from FoodInventory import FoodInventory
from Interface import Interface
from LinkedList import LinkedList
from Food import Food
from Dictionary import Dictionary
from DictInventory import DictInventory
#To do list:
#Add a key-value pair to the dictionary --- done
#Get the length of the dictionary ---done
#Search through the dictionary using the key and retrieve back the value --- done

#Remove a key-value pair from the dictionary using the key as input --- done kind of, not sure if pop works 100%
#Edit the value at a specific key --- not done ?
#

def step_6_main():
    ##################################
    #testing linked list
    Slist = LinkedList()

    f = Food()
    f.set_foodcode(12345)
    f.set_fooditem("chicken")
    newf = Food()
    newf.set_foodcode(54321)
    newf.set_fooditem("beef")
    newnewf = Food()
    newnewf.set_foodcode(98765)
    newnewf.set_fooditem("pie")
    new123 = Food()
    new123.set_foodcode(787878)
    new123.set_fooditem("porkchops")
    print("Testing the linked list:\n")
    print("Printing the empty list the empty list : \n")
    Slist.printlist()
    Slist.append(f.get_foodcode(), f)
    Slist.append(newf.get_foodcode(), newf)
    Slist.append(newnewf.get_foodcode(), newnewf)
    print("Printing the linked list after adding 3 items: \n")
    Slist.print_Llist()
    print("End testing linked list\n")
    print("------------------------------------------------------")
  
    ################################################################
  
    print("testing get all info")
    print(f.get_all_info())
    #testing the dictionary
  

    dict = Dictionary()
    # adding 5 food object to dictionary list
    dict._add(f.get_foodcode(), f)
    dict._add(newf.get_foodcode(), newf)
    dict._add(newnewf.get_foodcode(), newnewf)
    dict._add(new123.get_foodcode(), new123)

    #testing set_item 
    dict[5] = newf
    dict[new123.get_foodcode()] = new123
    print("Testing the dictionary linked list:\ntesting length of dict")
    print("\ntotal length: ")
    print(len(dict))  # testing length function

    print('\ntesting contains, using _find')
    if 98765 in dict:
        print("This key is in dict")
    if 0000 in dict:  #test to make sure magic method works when key not in dictionary (__contains__)
        print("")
    else:
        print("The key is not in dict")

    print('\ntesting getitem')
    dict[
        98765]  # testing __getitem__, returns food object, getitem does not print but returns .object
    print("ending test for dictionary\n-----------------------------------------------")

   

    #################################################################
    print("begin testing of DictInventory\n-----------------------------------------------")
    #Testing the dictinventory
    #function calls to dictinventory will go here

    #testing create inventory function
    
    dInventory = DictInventory()
    dInventory.create_inventory("Food_Database.csv")
    print("Testing search by food name uncomment next line to test search by foodname/food_item")
    dInventory.search_fooditem("Yeast") 
    print("\nList before any operations are performed on it \n \n")
    #dInventory.printinventory()  #prints list before searching with foodcode

    print("Testing search by food code:\n")
    dInventory.search_foodcode(11411200)
    print("Testing search by food code with incorrect foodcode:\nto test, uncomment next line")
    #dInventory.search_foodcode(11111)
    print("List after searching by food code \n uncomment next line to print list after searching by food code \n")
    #dInventory.printinventory()  # print list after searching with foodcode
  
    dfood = Food()
    dfood.set_foodcode(19910)
    dfood.set_fooditem("dictionary chicken")
    print("Testing adding new item to inventory and searching for the new added item with foodcode")
    dInventory.add_to_inventory(dfood)
    dInventory.search_foodcode(19910)
    print("printing list after adding a new food to the end of list\n to test uncomment next line")
    #dInventory.printinventory()
  
    print("new item added should be at end of list above")
    print("testing to add a food to the datafile \nuncomment next line to test if food is being added to food database")
    #dInventory.add_to_datafile()
    #print("please check Food_Database.csv for new food added at end of list")

    print("Testing pop: \n")
    
    #testing pop in linked list 
    Slist.print_Llist()
    Slist.pop(12345) #popping chicken (any of the 3 work)
    print("\nlist after popping\n")
    Slist.print_Llist()
    print("\ndone testing")
  
###############################################

if __name__ == "__main__":
  step_6_main()
