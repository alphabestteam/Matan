

import random


NAMES = ["jcob", "matan", "simon"]
ID = ["210892070", "271852985", "016725485"]


class Person: 
    def __init__(self) -> object:
       self.name = random.choice(NAMES)
       self.id = random.choice(ID)
       self.age = random.randint(0, 19)


    def get_name(self):
        return self.name
    

    def get_id(self):
        return self.name
    

    def get_age(self):
        return self.age
    

    def set_name(self, name: str):
        self.name = name


    def set_id(self, id: str):
        self.id = id

         
    def set_age(self, age: int):
        self.age = age
    

    def p_print(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.age}")
         