# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

class ClassName:
    def __init__(self):
        # constructor
        pass

    def method_name(self):
        # method
        pass


# self refers to the current instance of the class.

# It is used to access variables and methods inside the class.

# It must be the first parameter of every instance method.




class Student:
    def __init__(self, name, roll):
        self.name = name    # instance variable
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

# Create object (instantiation)
s1 = Student("Harsh", 101)
s2 = Student("Riya", 102)

# Call method
s1.display()   # Output: Name: Harsh, Roll: 101
s2.display()   # Output: Name: Riya, Roll: 102

# | Concept    | Description                                       |
# | ---------- | ------------------------------------------------- |
# | `class`    | Keyword to define a class                         |
# | `self`     | Refers to the current object of the class         |
# | `__init__` | Constructor method, called when object is created |
# | `object`   | Instance of a class (e.g., `s1 = Student(...)`)   |
