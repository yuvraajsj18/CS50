def main():
    s = Student("S", 1)     # creating an object of class Student
    s.print()

    s.changeId(11)
    s.print()

class Student():    # creating a class in python 

    def __init__(self, name, id):   # constructer in python __init__ . Self refers to the object that calls the function
        self.name = name    # initialising characterstics/ data/ states of the object
        self.id = id
    
    def changeId(self, id):     # defining behaviour of the object
        self.id = id
    
    def print(self):
        print(f"name = {self.name} --> id = {self.id}")

if __name__ == "__main__":
    main()