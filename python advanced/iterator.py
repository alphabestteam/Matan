

class Person:
    def __init__(self, person: list) -> object:
        self.person = person


    def add_person(self, name: str) -> None:
        self.person.append(name)

    
    def __iter__(self):
        self.curr_index = -1
        return self
    
     
    def __next__(self):
        if self.curr_index + 1 >= len(self.person):
            del self.curr_index
            raise StopIteration
        
        self.curr_index += 1
        return self.person[self.curr_index]
    

def main():
    new = Person(["matan", "ff", "sddddfff"])

    for name in new:
        print(name)


if __name__ == "__main__":
    main()