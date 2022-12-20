from csv import writer
import csv
from Dictionary import Dictionary
from Abstract import *
from Food import Food


class HTDictionary(DictAbstract):
    #########################################################
    def __init__(self):  #- Carlos
        self.size = 10  # Initial length of hashtable
        self.KEY_list = [[] for x in range(self.size)]  # hashList for all keys
        self.OBJ_list = [[] for x in range(self.size)
                         ]  # hashList for all objects(food)
        self.ADD_list = [
        ]  #does not need to be a hash table, only has to store object to write back to file

#########################################################
# - Carlos

    def _hash(
        self, key
    ):  # Mods the key which determine the index is going to be inserted at
        position = key % self.size  # Mods the key based on hashtable size
        return position  # return the position of where the key is going to be inserted

#########################################################
#-amrit
#adds keys food objects to a hash table

    def _add(
        self, key, value
    ):  # uses hash to place keys and values in proper locations(index)

        index = self._hash(
            key)  #gets position of where key should go using hash function
        self.KEY_list[index].append(
            key
        )  #appends to the index returned by hash appending to list within that index
        self.OBJ_list[index].append(
            value)  #appends object to the same indexlist in OBJ list

        return

#########################################################

    def _find(self, key):  # create a for loop
        hashed_key = self._hash(
            key)  #index in self.KEY_list based on key passed into find (0-10)
        keylistslot = self.KEY_list[hashed_key]
        objlistslot = self.OBJ_list[hashed_key]

        for i in range(
                len((keylistslot))
        ):  #iterates through key list and finds index, then takes index to obj list and returns object, which calls f.get_all_info
            if key == keylistslot[i]:
                return objlistslot[i]
#########################################################
#- Carlos
# Finds the object by user input of the foodname

    def _find_name(self, fooditem):
        j = 0
        objlist = self.OBJ_list
        for i in range(
                len(objlist)):  # iliterates throught the first initial list
            if len(objlist[i]) > 0:  # Skips the list if it empty
                objlistslot = objlist[i]

                for j in range(len(
                        objlistslot)):  # iliterates the list within the list
                    if objlistslot[j].get_fooditem(
                    ) == fooditem:  # If food name imputed by user match the object
                        return objlistslot[j]  # return the object
            if objlistslot[
                    j] != fooditem:  # raises key error if food name does not match
                raise KeyError("There is not fooditem with that food name")

#########################################################
#Return the number of items stored in the dictionary

    def __len__(self):  #-ben
        totallength = 0
        for i in range(0, len(self.KEY_list)):  #takes length of
            totallength += len(self.KEY_list[i])
            #print(len(self.KEY_list[i])) #to print length of sublists in hash table
        totallength *= 2
        print("Total Length of the inventory", totallength)
        return totallength

#########################################################

    def length(self):
        self.__len__()

#########################################################
#Implementing the python magic method __contains__
#This will help to use in true or false sentences
#e.g., if key is in dict

    def __contains__(self, key):
        pass

    #Implementing the python magic method __getitem__
    #This function will help in using this sytax dict[key]

#########################################################

    def __setitem__(self, key, value):  #-ben
        hashed_key = self._hash(
            key)  #calls hash function to hash key input to set item

        ifkeyinlist = False  #presets Key is not in list, will later check and can change value to true.

        keylistslot = self.KEY_list[
            hashed_key]  #accesses index in self.key/obj list to choose
        objlistslot = self.OBJ_list[
            hashed_key]  #where to iterate through for inserting item
        for i, existingkey in enumerate(
                keylistslot
        ):  #iterates through list within list to determine position
            if key == existingkey:
                ifkeyinlist = True  #key user input matches a key in list already, this is where we could override the object in the corresponding list.

        if ifkeyinlist:
            keylistslot[i] == (
                (key)
            )  #if there is a matching key, replace key and object with the new info the user is trying to add, (key will be the same object will change)
            objlistslot[i] == ((value))
        else:
            keylistslot.append(key)
            objlistslot.append(value)
            self.KEY_list[
                hashed_key] = keylistslot  #make the sublist in the hashtable == to new sublist with added food
            self.OBJ_list[
                hashed_key] = objlistslot  #make the sublist in the hashtable == to new sublist with added food
            self.ADD_list.append(
                value
            )  #adds value to add list so we can add value to dictionary

    #put print statement here to view lists after set item has been used

    #Implements self[key] = value.  If key is already stored in
    #the dictionary then its value is modified.  If key is not in the map,
    #it is added.

#########################################################

    def __getitem__(self, key):  #-ben
        return self._find(key)

#########################################################

    def _printlists(self):
        #print(self.KEY_list)
        #print(self.OBJ_list)
        return

#########################################################

    def pop(self, key):
        #-amrit

        hashed_key = self._hash(
            key)  #index in self.KEY_list based on key passed into find (0-10)
        keylistslot = self.KEY_list[
            hashed_key]  #make temporary list == to the list at hashed key location
        objlistslot = self.OBJ_list[
            hashed_key]  #make temporary list == to the list at hashed obj location

        for i in range(len(
            (keylistslot))):  #iterate through list within hash table

            if key == keylistslot[i]:  #if key == key in list
                poppedfood = objlistslot[i]  #make a copy of that food
                keylistslot.pop(i)  #pop the key from temp key slot
                objlistslot.pop(i)  #pop the food from the temp obj slot
                self.KEY_list[
                    hashed_key] = keylistslot  #replace list in keyhash table with list that has deleted key
                self.OBJ_list[
                    hashed_key] = objlistslot  # replace list in objhash table with list that has deleted food object
                for i in range(len(self.ADD_list)
                               ):  #look trhough addlist[] (data writeback)
                    if key == self.ADD_list[i].get_foodcode(
                    ):  #find the food to be deleted
                        self.ADD_list.pop(
                            i
                        )  #delete food so we don't write a food back to datafile that is deleted from inventory
                        break
                return poppedfood  #return the object that was deleted


#########################################################
