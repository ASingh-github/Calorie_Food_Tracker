class Food:  #Ben Start
    #class for storing info about the food's information

    def __init__(self):  #constructor
        #every food will have the item name, item description, food code, amount of: protein, calories, carbs, fats, and then the #of items the user has input
        self.__fooditem = ""
        self.__foodcode = 0
        self.__protein = 0
        self.__calories = 0
        self.__carbs = 0
        self.__fats = 0

        # all variables are private --               Ben End
        #Carlos Start
    def get_fooditem(self):
        return self.__fooditem

    def get_foodcode(self):
        return self.__foodcode

    def get_protein(self):
        return self.__protein

    def get_calories(self):
        return self.__calories

    def get_carbs(self):
        return self.__carbs

    def get_fats(self):
        return self.__fats

    #Carlos End
    #Amrit Start
    # setter methods to set attributes of "Food" objects

    def set_fooditem(self, fooditem):
        fooditem = str(fooditem)
        if not fooditem:  #checks if empty string
            raise Exception("Empty String entered! fooditem not set")
        else:
            self.__fooditem = fooditem

    def set_foodcode(self, foodcode):
        foodcode = int(foodcode)
        #checks if less than zero
        assert foodcode >= 5, f"foodcode greater than 0 expected, got: {foodcode}"
        self.__foodcode = foodcode

    def set_protein(self, protein):
        protein = float(protein)
        assert protein >= 0, f"protein greater than 0 expected, got: {protein}"
        self.__protein = protein

    def set_calories(self, calories):
        calories = float(calories)
        assert calories >= 0, f"calories greater than 0 expected, got: {calories}"
        self.__calories = calories

    def set_carbs(self, carbs):
        carbs = float(carbs)
        assert carbs >= 0, f"carbs greater than 0 expected, got: {carbs}"
        self.__carbs = carbs

    def set_fats(self, fats):
        fats = float(fats)
        assert fats >= 0, f"fats greater than 0 expected, got: {fats}"
        self.__fats = fats

# Carlos Start 
    def get_all_info(self):
      line = "-----Food Info----- \n" + "Food code: " + str(self.__foodcode) + "\nFood name: " + str(self.__fooditem) + "\nCalories: " + str(self.__calories) + "\nProtein: " + str(self.__protein) + "\nCarbs: " + str(self.__carbs) + "\nFats: " + str(self.__fats)
      return line 
# Carlos End 