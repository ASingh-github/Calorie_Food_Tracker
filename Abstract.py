from abc import abstractmethod
from abc import ABC

class FoodInvAbstract(ABC):

  @abstractmethod

  def search_foodcode(self, foodcode):
    pass
 
  
  @abstractmethod 
  def create_inventory(self, datafile):
    pass

  
  @abstractmethod
  def search_fooditem(self, fooditem):
    pass

  
  @abstractmethod
  def add_to_inventory(self,f):
    pass

    
  #@abstractmethod
  #def get_all_info(self, f):
    #pass


  @abstractmethod 
  def add_to_datafile(self):

    pass

########################################################################
########################################################################
#This class will be the blueprint for the Dictionary class
    
class DictAbstract(ABC):

    #Return the number of items stored in the dictionary
    @abstractmethod
    def __len__(self):
        pass

    #Implementing the python magic method __contains__
    #This will help to use in true or false sentences
    #e.g., if key is in dict
    @abstractmethod
    def __contains__(self, key):
        pass

    #Implementing the python magic method __getitem__
    #This function will help in using this sytax dict[key]
    @abstractmethod
    def __getitem__(self, key):
        pass

    #Implements self[key] = value.  If key is already stored in
    #the dictionary then its value is modified.  If key is not in the map,
    #it is added.
    @abstractmethod
    def __setitem__(self, key, value):
        pass

    #Remove a node from the linked list with the indicated key
    #Return the value after removing the node
    #Raise a KeyError if the key is not in the map."
    @abstractmethod
    def pop(self, key):
        pass
