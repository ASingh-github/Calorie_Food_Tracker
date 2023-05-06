# Calorie_Food_Tracker
###############################################################
This is is a small project to test out different implementations of dictionaries in a food logger/calorie tracker.

Use any of the main.py files to test the different data structures and algorithms used.

Authors: Amritpal Singh, Ben

                            FILE DESCRIPTION
HTDictionary.py:
Dictionary implementation using hashtables

HTInventory.py
Inventory implementation using Hash table dictionary

Short_Food_Database.csv: 
Holds all the attributes of our food objects but a small length of 10 
Used to test the sorting algorithm 

SLInventory.py: 
Includes all the implementation of a inventory 
This includes , searching from a key and fooditem, adding , and deleting from a dictionary 

SLDictionary.py: 
Implements a sorted list as a dictionary
Function of the SLDictionary is to add , delete and also functions that sort the unsorted list and search from that list 

DictInventory.py:
Includes all the implementation of an inventory
This includes, searching, adding, and deleting from an inventory.

Dictionary.py:
Implements the linked list as a dictionary.
Functions to add to dictionary, delete from dictionary, search from dictionary, also includes magic methods.

DisctAbstract.py:
Blueprint for any dictionary class, inheritence requires all the functions be included. Minimal requirements for a dictionary are included in this file.

Food_Database.csv: *****************FROM USDA https://fdc.nal.usda.gov/resources.html#bkmk-1********** 
Holds all the attributes of our food objects in order by foodcode

Short_Food_Database.csv:
Used to test dictionary or other inventories. Easier to debug with smaller data before implementing to the larger database

Food_Log.csv:
Holds food object data that the user had logged

Food.py:
Holds all the functions to create and modify a "food" object.
Getters and setters for the object are included in this file.

FoodInvAbstract.py:
Blueprint for FoodInventory classes. Minimal requirements of a FoodInventory are in this blueprint.

FoodInventory.py:
Handles all the inventory functions such as adding to inventory list, adding back to data file, searching from inventory list.

Foodlog.py:
class to manage food log functionality. Searching, adding, and adding to food log data file. Probably could be added to inventory class.

Interface: 
Static class that manages user input and interface operations.

LinkedList:
Test class for linked list implementation
