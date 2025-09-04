class Human:  ## base class
    def __init__(self, name, age, gender):  ## attributes
        self.name = name
        self.age = age
        self.gender = gender

    def walk(self):  ## method
        print(f"{self.name} is walking")

    def talk(self):  ## method
        print(f"{self.name} is talking")

    def tell_me_your_name(self):  ## method
        print(f"My name is {self.name}")

    def say_hello(self):  ## method
        print(f"Hello, my name is {self.name}")

    def are_you_abover_18(self):  ## method
        if self.age >= 18:
            print(f"Yes, I am above 18. My age is {self.age}")
        else:
            print(f"No, I am not above 18. My age is {self.age}")

    def introduce_yourself(self):  ## method
        print(f"My name is {self.name}, I am {self.age} years old and I am {self.gender}")


class Man(Human):  ## child class inheriting from Human
    def __init__(self, name, age, gender, height, nationality, beard_length):  ## attributes
        super().__init__(name, age, gender)  ## inherit attributes from Human
        self.height = height
        self.nationality = nationality
        self.beard_length = beard_length

    def can_give_birth(self):  ## method
        print("Men cannot give birth")

    def can_fly(self):  ## method
        print("Humans cannot fly")

    def work(self):  ## method
        print(f"{self.name} is working hard")

    def shave_beard(self):  ## method (specific to men)
        print(f"{self.name} shaved his beard. It was {self.beard_length} cm long")


class Woman(Human):  ## child class inheriting from Human
    def __init__(self, name, age, gender, height, nationality, hair_length):  ## attributes
        super().__init__(name, age, gender)  ## inherit attributes from Human
        self.height = height
        self.nationality = nationality
        self.hair_length = hair_length

    def can_give_birth(self):  ## method
        print("Women can give birth")

    def can_fly(self):  ## method
        print("Humans cannot fly")

    def work(self):  ## method
        print(f"{self.name} is working smart")

    def style_hair(self):  ## method (specific to women)
        print(f"{self.name} is styling her hair of length {self.hair_length} cm")
