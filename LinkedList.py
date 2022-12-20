from Food import Food


class Node:
    #key = foodcode
    #value = foodobject

    def __init__(self, key, val=None):    #node class constructor storing key and value  
        self.key = key
        self.val = val
        self.next = None

   # def __repr__(self):
   #     return self.val


class LinkedList:
######################################
#constructor sets head as none(starts empty) - Ben

    
    def __init__(self):
        self.head = None

######################################
#function to print list - ben 
    def printlist(self):     
        current = self.head   #head is set as printed value 

        while current != None:
            print(current.val)
            current = current.next #value is printed then next value is stored, then printed in loop until end of nodes
          

  ########################################
  #adding new node to end of linked list - Amrit
  
    def append(self, key, value):
        newNode = Node(key, value) #create a new node
        if (self.head == None): #check if head is empty, if yes (empty list), make this new node your head.
            self.head = newNode
            return
        else: # else declare a temp node that takes value of head and iterates through list until end of list is found where temp.next=None and adds newNode to that position.
            current = self.head 
            while (current.next != None):
                current = current.next
            current.next = newNode

          
#########################################
#printing every element of linkedlist includes key and can include any attributes of the food object in every node -Amrit
    def print_Llist(self):
      count = 0
      temp=self.head # declare temp node as head
      if(temp != None): #check to see if end of list
        print("Here is the list: ")
        while (temp != None): #while not last node
          print(temp.key, temp.val.get_fooditem()) # print the key of node
          temp= temp.next
          count +=1 
       # print()
        #print("count = ", count)
      else:
        print( "Empty list") 
        
###############################################################################
  
    def __contains__(self, key):#iterate thru linked list and find if key is contained within, if yes do something.(returns true or false)
      
      current = self.head #sets current to head
      while current != None: 
       
        if current == key: #if current is not none go through list, if it matches key return, if no move to next 
          print("Found") 
          return True
        current = current.next
      print("Key: " , key) # if not in list print not found --ben ( later rmake it print actual key that is being searched )
      return False

#########################################

    def pop(self, key):  #pops key and value pair based on key, iterate through list to find key, pop whole node -ben

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
        
      prev.next = temp.next
      temp = None
      

      

        
       