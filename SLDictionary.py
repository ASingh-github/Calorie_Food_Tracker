from csv import writer
import csv
from Dictionary import Dictionary
from Abstract import *
from Food import Food


class SLDictionary(DictAbstract):
    #ben
    #####################################
    def __init__(self):
        # self.fooditemList = []
        self.KEY_list = []
        self.OBJ_list = []
        self.ADD_list = []
       
####################################

############################################################

    def mergesort(self, keylist, objlist): #-ben
        if len(keylist) > 1:  # if list is populated
            left_K_array = keylist[0:len(keylist) //2]  #splits array from left to middle
            right_K_array = keylist[len(keylist) // 2:len(keylist)]  #splits array from middle to right
            left_O_array = objlist[0:len(objlist) //2]  #splits array from left to middle(object array)
            right_O_array = objlist[len(objlist) // 2:len(objlist)]  #splits array from middle to right(object array)
            
            self.mergesort(left_K_array, left_O_array)
            self.mergesort(right_K_array, right_O_array)

            i = 0  #index for left array
            j = 0  #index for right array
            k = 0

            while i < len(left_K_array) and j < len(right_K_array):
                if left_K_array[i] < right_K_array[j]:
                    keylist[k] = left_K_array[i]
                    objlist[k] = left_O_array[i]
                    i += 1
                else:
                    keylist[k] = right_K_array[j]
                    objlist[k] = right_O_array[j]
                    j += 1
                k += 1

            while i < len(
                    left_K_array
            ):  #while there are elements in the left array to transfer into new array
                keylist[k] = left_K_array[i]
                objlist[k] = left_O_array[i]
                i += 1
                k += 1

            while j < len(
                    right_K_array
            ):  #while there are elements in right array to transfer
                keylist[k] = right_K_array[j]
                objlist[k] = right_O_array[j]
                j += 1
                k += 1

        self.KEY_list = keylist
        self.OBJ_list = objlist
        return 

#################################################################################
      
       
              

###############################################################


    def printlist(self): #-ben
        print("foodcodes:")
        #print(self.KEY_list)
        print("food objects:")
       # print(self.OBJ_list)

################################################################
      
    def sort_lists(self):#-ben
        self.mergesort(self.KEY_list,self.OBJ_list)


################################################################
        #-Amrit
        #when final sorting function is done between foodcode list and food object list , call it here, then when calling sort_lists, it will print both sorted lists
        #internal function to find an object by key (using binary search) and return it. 
    def _find(self, key):
        #self.mergesort(self.KEY_list)
        low = 0  #WIP
        high = len(self.KEY_list) 
        
        # calls a binary search with key requested
        #index= an integer that was returned using the binary search.
        # this integer will = the index in self.OBJ_list that holds the food object in relation to the key(foodcode)
        index = self._binary_search(low, high, key)
      
        #print("printing index: ")
        #print(index)      #also commenting out, if needed to see index of searched food its this line 
        #print(self.OBJ_list)
        
        
        return self.OBJ_list[index] 


      
      #-Carlos 
       # goes throught the Objlist where if finds the object and returns the name of the item
    def _find_name(self, food_item):
      k = 0
      objlist = self.OBJ_list 
      
      while objlist != None: # while list is populated 
        
        if objlist[k].get_fooditem() != food_item: # goes through the list 
          k += 1
          
        else: 
          
          return objlist[k] # returns the name of the object 
     

##############################################################################
#-Amrit
#binary search(recursive),can't be used until lists are sorted.
#returns index of key list that has matching key after doing binary search

    def _binary_search(self, low, high, key):
        #low is lower bound of search, starts at 0 since list begins at zero
        #high is the size of array-1 (this way the function won't go out of range.
        
        if high >= low:  #Base case

            mid = (high + low) // 2  #getting middle element

            if self.KEY_list[mid] == key:
                #if key is in middle # it returns an integer that = the index where match was found Then _find takes that index and looks at same index in OBJ_list
                return mid
                #binary search looks like its working, its finding the match, and then returns 
                #return key(middle element)
            elif self.KEY_list[mid] > key:
               # if key smaller than mid, then its in left array
                return self._binary_search(
                    low, mid - 1, key
                )  #recursive call to _binary_search(low,high,key) with high = mid-1
            else:
                return self._binary_search(
                    mid + 1, high, key
                )  #else recursive call to _binary_search with the right array
        else:
            return print("key not found!")  #if key isn't found after calls are complete 
         

#################################################################################
#Amrit
# adds food objects to object list and keys to key list, this is prior to sort.

    def _add(self, key, value):
        self.KEY_list.append(key)  #key(foodcodee) is added to Key_list
        self.OBJ_list.append(value)  #value(foodobject) is added to OBJ_list

#################################################################################
#Return the number of items stored in the dictionary 
      #-Carlos & Amrit

    def __len__(self):
        KEYsize = len(self.KEY_list)
        OBJsize= len(self.OBJ_list)
        print("The size of the KEY list is ", KEYsize)
        print("The size of the OBJ list is ", OBJsize )
        dictsize = KEYsize + OBJsize
        print("The size of the dictionary is", dictsize)
        return KEYsize, OBJsize

    def length(self):
        self.__len__()

#################################################################################
    #this function is carried over from last dictionary, can be used to see if a key exists in dictionary or not
    def __contains__(self, key):
        return not self._find(key) is None

################################################################################
#-Amrit
#Implementing the python magic method __getitem__
#This function will help in using this sytax dict[key]

    def __getitem__(self, key):
        f = self._find(key)
        
        if f == None:  #if find does not find matching key
            raise KeyError("There is no item with that key")
        else:
          
          return f

################################################################################
#Implements self[key] = value.  If key is already stored in
#the dictionary then its value is modified.If key is not in the list,it is added.
#-AMRIT

    def __setitem__(self, key, value): 
      keymatch=False #check to see if a matching key is found in key list
      index=0 #index used from KEY list to get location of object in OBJ list
      for i in range (len(self.KEY_list)):
        if key == self.KEY_list[i]: #if given key matches key at index
          keymatch==True #key match is now true
          index=i #index is = to index where key was found
          break

      if keymatch == True:
        print("this food code "+ str(key)+"already exists") # let user know key already exists
        self.OBJ_list[index]= value #replace object represented by key found to new object input by user.
        value.set_foodcode(key) #sets the foodcode of the object to be = to key of old object(this is validation could be removed if it causes bugs)
        print("existing food object was replaced with new foodobject")# let user know food regarding certain key has been changed
      elif keymatch == False: #if key not matched
        for i in range (len(self.KEY_list)):
          if key < self.KEY_list[i]:
            self.KEY_list.insert(i, key)
            self.OBJ_list.insert(i, value)
            self.ADD_list.append(value) #add to ADD_list so the new object can be added to database once program is done runnning
            print("new key list length after adding" ,len(self.KEY_list))
            print("new object list length after adding" , len(self.OBJ_list))   
            print("The following food was added: ", self.OBJ_list[i].get_fooditem(), "with key: ", self.KEY_list[i] ,"\n")
            print("This food was added at index: " + str(i))
            break
            #self.KEY_list.insert(0, key)  #add new key to list
        else:
          self.KEY_list.append(key)
          self.OBJ_list.append(value)
          self.ADD_list.append(value)
        
        #self.OBJ_list.insert(0, value)
            
        #add new food object that is represented by key
        #self.sort_foodOBJlist(self.OBJ_list) #sort both lists once new food is added

        #self.sort_lists()
        #self.sort_foodOBJlist(self.OBJ_list) #at this point, the list is already sorted, but this call is needed to sort the newly added food codes and objects 
        #checks to see if the food is actually added to the correct list(OBJ_list)
        
      return
                

################################################################################
#-Carlos 
      # Removes the foodobject from the indicated key from the KEYlist and the OBJlist 
      # Raise an error if the key does not match 
    def pop(self, key):
        for i in range(len(self.KEY_list)):
          if key == self.KEY_list[i]:
            self.KEY_list.pop(i)
            self.OBJ_list.pop(i)
            j = self.OBJ_list[i]
            print(j.get_foodcode)
          else: 
            print("No existing key to pop")
          return 
              
          
#Remove an index with the indicated key
#Return the value after removing the node
#Raise a KeyError if the key is not in the map."
