class Animal: ## base class
    def __init__(self,name,type,age):
        self.name = name    ## attribute
        self.type = type    ## attribute
        self.age = age      ## attribute

    def what_is_your_name(self): ## method
        print(f"Welcome I am {self.name} and I am a {self.type}")

    def run(self): ## method
        print(f"{self.name} is running")

    def get_age(self): ## method
        print(f"My Age is {self.age}")


class Dog(Animal):  ## child class (inheriting from Animal)
    def __init__(self,name,type,age, breed):
        self.name = name    ## attribute
        self.type = type    ## attribute
        self.age = age      ## attribute
        self.breed = breed  ## attribute

    def what_is_your_name(self):    ## method (overriding the main base class method)
        print(f"I am a {self.breed} and my name is {self.name}")

####################################################################################


dog1 = Dog(name='Buddy',type='Dog', age=5, breed='German Shepherd') ## instance of Dog

dog1.what_is_your_name() ## method (overriding the main base class method) from Dog Class
dog1.run()  ## method (inherited from Animal class)