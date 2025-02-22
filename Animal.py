class Animal:
    def __init__(self, name, drink, capability, lift, inhabit, sleep): #These are attributes inside parenthesis.
        self.__name = name
        self.__drink = drink
        self.__capability = capability
        self.__lift = lift
        self.__inhabit = inhabit
        self.__sleep = sleep

    def Animal_name(self):
        print("This is an", self.__name)

    def Animal_drink(self):
        print("An", self.__name, "usually drinks", self.__drink)

    def Animal_capability(self):
        print("An", self.__name, "can eat leaves by reaching out through its", self.__capability)

    def Animal_lift(self):
        print("An", self.__name, "can lift weights of up to", self.__lift)

    def Animal_inhabit(self):
        print("An", self.__name, "primarily inhabits", self.__inhabit)

    def Animal_sleep(self):
        print("An adult", self.__name, "sleeps up to", self.__sleep, "per day")

    

  

