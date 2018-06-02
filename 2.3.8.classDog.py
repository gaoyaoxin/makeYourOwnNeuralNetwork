# class for a dog object
class Dog:

    # initialization method with internal data
    def __init__(self, petname, temp):
        self.name = petname;
        self.temperature = temp;
    
    # get status
    def status(self):
        print("Dog name is ", self.name)
        print("Dog temprature is ", self.temperature)
        pass

    # set temperature
    def setTemperature(self, temp):
        self.temperature = temp;
        pass

    # dogs can bark()
    def bark(self):
        print("woof!")
        pass
    
    pass

# create a new dog object from the Dog class
lassie = Dog("Lassie", 37)
lassie.status()

lassie.setTemperature(40)
lassie.status()