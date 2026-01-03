class Animal:
    def __new__(cls, name, tp):
        if tp == "Herbivore" or tp == "Carnivore" or tp == "Omnivore":
            return  super().__new__(cls)
        else:
            return None

    def __init__(self, name, tp):
        self.__name = name
        self.tp = tp

    def get_item(self):
        return f"The name is {self.__name}"

    def type(self):
        return f"The {self.__name} is a {self.tp}"

rabbit = Animal("Handler of Cosmos", "Herbivore")
cat = Animal("Dragon Ball", "Derbivores")
print(rabbit.get_item())
# print(cat.get_item()) # the object isn't created
print(cat) # no object created that's why returning None

# in the upper code we could have written:
# def __new__(cls, name, tp):
#         if tp in ("Herbivore", "Carnivore", "Omnivore"):

# ----------------------------------------------------------------------------------------------------------------

