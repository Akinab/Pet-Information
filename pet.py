def details ():
    Description = "Pet Information"
    Date = "06-07-23"
    print ("\nDescription: {}\nDate: {}".format (Description , Date))
    
details ()

class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type