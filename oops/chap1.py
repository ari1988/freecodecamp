class Dog():
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Woof!")

class Owner:
    def __init__(self, name,address,contact_number):
        self.Owner_name = name
        self.address = address
        self.phone_number = contact_number
        # self.contact_number = contact_number

#----
owner1 = Owner("John Doe","123 Bark St","555-1234")
dog1 = Dog("Snuffles","Beagle", owner1)
print(dog1.name)
print(dog1.breed)
dog1.bark()
print(dog1.owner.Owner_name)

# owner1 = Owner("John Doe","123 Bark St","555-1234")
# print(owner1.Owner_name)
# print(owner1.address)
# print(owner1.phone_number)