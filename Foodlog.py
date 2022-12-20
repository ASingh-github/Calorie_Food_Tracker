from Food import Food
import csv

class Foodlog:
#___________________________________________
    ## two lists are created, one grabs data from foodlog.csv file, the other is a temporary list that keeps track of entries during program runtime and is later appended back to Food_Log.csv file
    def __init__(self):
        self.__foodlog_list = [
        ]  #list food objects are appended to during runtime
        self.__logfile_list = [
        ]  # list that is populated from Food_Log.csv to show user what they have logged in prior sessions
#______________________________________________
#this function appends a user entry to the list "foodlog_list"

    def add_to_loglist(self, f):

        self.__foodlog_list.append(f)

#_____________________________________________
#this function adds the content of self.__foodlog_list into Food_Log.csv

    def add_to_foodlog(self):

        for f in self.__foodlog_list:
            fields = [
                f.get_foodcode(),
                f.get_fooditem(),
                f.get_calories(),
                f.get_protein(),
                f.get_carbs(),
                f.get_fats()
            ]
            if len(self.__foodlog_list) > 0:
                with open("Food_Log.csv", "a+") as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(fields)
#___________________________________________________________

    def create_log(self, logfile):
        # Open the file for reading
        # loop through each line of the file
        # For each line, create a food object and add it to the list of food.
        #Amrit Start
        with open(logfile) as csvfile:
            # Carlos Start
            # Reading every single line separately

            for line in csvfile:
                #words = line.split()
                words = line.strip().split(',')

                f = Food()
                #format for our lines:
                #Code, item, calories, protein, carb, fat
                #Carlos start
                f.set_foodcode(words[0])
                f.set_fooditem(words[1])
                f.set_calories(float(words[2]))
                f.set_protein(float(words[3]))
                f.set_carbs(float(words[4]))
                f.set_fats(float(words[5]))

                #print(f.get_foodcode())
                #print(f.get_fooditem())

                self.__logfile_list.append(f)


#this function will be used to populate the self.__logfile_list=[] from the Foo_Log.csv file. Once this list is filled with the prior logs, all of its content can be printed depending on how we want them presented.
#________________________________________________________

    def display_foodlog(self):#amrit skeleton
        counter = 0
      
        for f in self.__logfile_list:
            counter = counter + 1
            print(str(counter) + ". Food: " + 
            str(f.get_fooditem()) + ", Calories: " +
            str(f.get_calories()))
            
        for f in self.__foodlog_list:
          counter += 1 
          print(str(counter) + ". Food: " + 
          str(f.get_fooditem()) + ", Calories: " +
          str(f.get_calories()))
#Displays foodlog if user wants to look at it.
#__________________________________________        
    def print_target_calories(self): #ben calorie setter function 
      num = input("Enter Target Calories: ")
      calories_eaten = 0
      for f in self.__logfile_list: 
        calories_eaten += int(f.get_calories())
      for f in self.__foodlog_list: 
        calories_eaten += int(f.get_calories())

      print("Calorie count: ")        #displays calories eaten out of target calories
      print(calories_eaten,"/", num )

#calories eaten are calculated.
#___________________________________________