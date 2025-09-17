class Human:
    def __init__(self, name , age, gender):
        self.name = name
        self.gender = gender    
        self.age = age
    
    def walk(self):
        print("I am walking")
    def talk(self):
        print("I am talking")
    def tell_me_your_name(self):
          print(f"My name is {self.name}")
    def say_hello(self):
        print("Hello")
    def are_you_abover_18(self):
          if self.age >= 18:
                print("Yes, I am above 18")
          else:
                print("No, I am not above 18")      
    def introduce_yourself (self):
            if (self.gender==""):
                  print("You did not adentify your gender")
            else:     
                  print(f"My name is {self.name}, I am {self.age} years old and my sex is {self.gender}")

class Man(Human):
    def __init__(self, height, nationality, beard_length):
         self.height = height
         self.nationality = nationality
         self.hair_length = beard_length

    def can_give_birth(self):
         print("I can not give a birth")
    def can_fly(self):
            print("I can not fly")
    def work(self):
            print("I can work")
    def shave_beard(self):
            print("My beard is shaved")         
        
class Women(Human):
    def __init__(self, height, nationality, hair_length):
         self.height = height
         self.nationality = nationality
         self.hair_length = hair_length

    def can_give_birth(self):
         print("I can give a birth")
    def can_fly(self):
            print("I can not fly")
    def work(self):
            print("I can not work")
    def style_hair(self):
            print("My hair is styled")

Human.name = input("Enter your name: ")
Human.age = int(input("Enter your age: "))
Human.gender = input("Enter your sex (MALE / WOMEN): ").lower()

if Human.gender == "male":
      
      Human1 = Man(height = int(input("Enter your height: ")),nationality = input("Enter your nationality: "),beard_length=int(input("Enter your beard_length: ")))
      
      Human1.walk()
      Human1.talk()
      Human1.say_hello()
      Human1.tell_me_your_name()
      Human1.introduce_yourself()
      Human1.are_you_abover_18()
      Human1.shave_beard()
      Human1.can_give_birth()
      Human1.can_fly()
      Human1.work()


elif Human.gender == "women":
      
      Human1 = Women(height=int(input("Enter your height: ")),nationality=input("Enter your nationality: "),hair_length=int(input("Enter your hair_length: ")))

      Human1.walk()
      Human1.talk()
      Human1.say_hello()
      Human1.tell_me_your_name()
      Human1.introduce_yourself()
      Human1.are_you_abover_18()
      Human1.style_hair()
      Human1.can_give_birth()
      Human1.can_fly()
      Human1.work()

      
else:
    print("INVALID INPUT")
    