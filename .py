class Pet:
    print("Hi, I am a pet profile builder!")
name = input("Enter your pet's name?")
aniaml_type = input("Enter the kind of aniaml he is?")
age = input("Enter your pet's age?")
favourite_food = input("Enter the food which your pet likes the most?")
pet_object = Pet()
class PetProfile:
    def __init__(self, name, aniaml_type, age, favourite_food):
        self.name = name
        self.aniaml_type = aniaml_type
        self.age = age
        self.favourite_food = favourite_food
print("Your pet profile has been built")
print("Fecthing yuour Pet's profile now.")
print("Wait....")
print("")
print("======================YOUR PET'S PROFILE======================")
print("{} is a {} and is {} years old.".format(name, aniaml_type, age))
print("{} likes eating {}.".format(name, favourite_food))
print("==============================================================")