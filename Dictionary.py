from Food import Food
#from csv import writer
import csv
from Abstract import *

#This class will utilize the linked list class and the node class to behave as a dictionary.
#This class inherits from the DisctAbstract class so all the function declarations done in the DisctAbstract class need to be defined in this class. (we can also add more functions if needed but we need to add them to both classes for inheretance to work)


class DictNode:

    def __init__(self, key, val=None):  #node class constructor storing key and value - ben 
        self.key = key
        self.val = val
        self.next = None
      
##############################################################
    #-Carlos Start
    def __get_all_info__(self): 
     return str(self.val.get_foodcode()) + ":" + str(self.val.get_fooditem())
      #return fooditem and foodcode when getallinfo is called on a foodobject 
      #-Carlos End 

##############################################################

class Dictionary(DictAbstract):

    def __init__(self):
        self.head = None
        
##############################################################

    def __len__(self):
        #iterate thru linked list and a counter will go up for each node. -ben
        current = self.head
        length = 0
        while current.next != None:
            length += 1
            current = current.next
        return (length)

##############################################################
#adds a new dictNode to the end of list 
# -Carlos Start
    def _add(self, key, value):
        newNode = DictNode(key, value)  # Creating a new node
        # checks if head is empty if yes(empty list), makes this new node your head
        if (self.head == None):
            self.head = newNode
            return
        else:  # checks the list finding the end of the list where it add the newNode to that postion
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = newNode
        #self._size +=1
          #- Carlos End 

###############################################################

    def __setitem__(self, key, value):  #takes key value pair, if there is no head node(empty list) new node with key value is                                               created -ben
        self.head == self._find(key)   #head is passed through find 
        if self.head == None:
            print("node with that key does not exist,creating new node")
            self.head == DictNode(key, value)
        else:  #if head is not none, node is inserted
            self._add(key, value) #calls add to insert new node with given value and key

#############################################################
                                      #this function searches for item by foodcode
    def __getitem__(self, key):          #iterate thru linked list and find node with matching key by passing into _find. 
                                          #return the food object for that key. -ben
        f = self._find(key)
        if f == None:  #if find does not find matching key
            raise KeyError("There is no item with that key")
        else:
            return f

################################################################

    def _find(self, key):        #iterates through list and compares keys -ben
      current = self.head
      while current != None:
          if current.key == key:
              return current.val    # if found return the node of the key 
          elif current.key != key:
              current = current.next
      return None # if key is never found return none 
      #(later we could combine this to call _add if there is no node but we want to add one)

###############################################################
      
    def pop(self, key):  #pops key and value pair based on key, iterate through list to find key, pop whole node -Ben

      #to check if self.head matches the key of the node to be deleted
      temp = self.head #store head of list as a dict node object in temp 
      
      if temp != None: #if temp has value(node exists)
        if temp.key == key:  #compare key, if node to remove is self.head:
          self.head = temp.next 
          temp = None
          return 

      while temp != None: #search through list to find node with matching key
        if temp.key == key: 
          break
        prev = temp
        temp = temp.next #searches through until key is found, pointers are changed when found 
        
      if temp == None: #if temp now equals none due to the list ending and no key found: 
        print("Key not found in list !")
        return 
        
      prev.next = temp.next #takes pointer of previous list and points it to next list
      temp = None #node to be removed is set to none, and pointers have been reloacted

################################################################
      
      # This is a find function , where it it searches for the fooditem and called in the search fooditem in dictInventory 
      #- Carlos Start 
    def _findname(self,food_item):
        current = self.head 
        while current != None: 
          if current.val.get_fooditem() == food_item:
              return current.val 
          elif current.val.get_fooditem() != food_item: 
            current = current.next
        return None
      #- Carlos End 
    
#(food object found after comparing name ie.)
      
##########################################################

    def __contains__(
        self, key
    ):  #iterate thru linked list and find if key is contained within, if yes do something.(returns true or false)
        return not self._find(key) is None


###############################################################
#function to iterate through list and print every value's name (fooditem)

    def print_Llist(self):          #-ben
        current = self.head  # declare temp node as head
        if (current.next != None):  #check to see if end of list
            print("Here is the list: ")
            while (current != None):  #while not last node
                print(current.val.get_fooditem())  # print the key of node
                current = current.next
            print(" end of list")
        else:  #if self.head is none, list must be empty
            print("Empty list")
