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

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age
    
# Create a Pet object and prompt the user for pet information
pet = Pet("", "", "")

pet.set_name(input("\nEnter the pet's name: "))
pet.set_animal_type(input("\nEnter the type of animal: "))
pet.set_age(input("\nEnter the pet's age: "))

# Display the retrieved pet data
print("\nPet Information:")
print("Name:", pet.get_name())
print("Animal Type:", pet.get_animal_type())
print("Age:", pet.get_age())