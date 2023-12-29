Calorie_Food_Tracker

###############################################################
This is a small project to test out different implementations of dictionaries in a food logger/calorie tracker.

Use any of the main.py files to test the different data structures and algorithms used.

Authors: Amritpal Singh, Ben Ollar, Carlos Veloz-Avelar

markdown

                        FILE DESCRIPTION

HTDictionary.py:
Dictionary implementation using hash tables.

HTInventory.py:
Inventory implementation using Hash table dictionary.

Short_Food_Database.csv:
Holds all the attributes of our food objects but with a small length of 10.
Used to test the sorting algorithm.

SLInventory.py:
Includes all implementations of an inventory.
This includes searching from a key and food item, adding, and deleting from a dictionary.

SLDictionary.py:
Implements a sorted list as a dictionary.
The function of the SLDictionary is to add, delete and also functions that sort the unsorted list and search from that list.

DictInventory.py:
Includes all implementations of an inventory.
This includes searching, adding, and deleting from an inventory.

Dictionary.py:
Implements the linked list as a dictionary.
Functions to add to the dictionary, delete from the dictionary, search from the dictionary, also includes magic methods.

DictAbstract.py:
Blueprint for any dictionary class, inheritance requires all the functions to be included. Minimal requirements for a dictionary are included in this file.

Food_Database.csv: *******FROM USDA https://fdc.nal.usda.gov/resources.html#bkmk-1
Holds all the attributes of our food objects in order by food code.

Short_Food_Database.csv:
Used to test dictionaries or other inventories. Easier to debug with smaller data before implementing it in the larger database.

Food_Log.csv:
Holds food object data that the user has logged.

Food.py:
Holds all the functions to create and modify a "food" object.
Getters and setters for the object are included in this file.

FoodInvAbstract.py:
Blueprint for FoodInventory classes. Minimal requirements of a Food Inventory are in this blueprint.

FoodInventory.py:
Handles all the inventory functions such as adding to the inventory list, adding back to the data file, searching from the inventory list.

Foodlog.py:
A class to manage food log functionality. Searching, adding, and adding to the food log data file. Probably could be added to the inventory class.

Interface:
A static class that manages user input and interface operations.

LinkedList:
A test class for linked list implementation.
