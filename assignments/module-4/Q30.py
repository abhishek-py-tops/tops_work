# What relationship is appropriate for Student and Person?
# A Student is a Person (i.e., Student has all attributes of Person + extra student-specific fields).

# This fits the Object-Oriented Inheritance model.


# # models.py

# from django.db import models

# class Person(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()

# class Student(Person):  # Inheriting from Person
#     roll_no = models.CharField(max_length=20)
#     course = models.CharField(max_length=100)

# | Relationship    | Use Case                                             | Example                             |
# | --------------- | ---------------------------------------------------- | ----------------------------------- |
# | **Inheritance** | A Student **is a** Person                            | `Student(Person)` ✅ Best Fit        |
# | OneToOneField   | If Student has extra info but is not always a Person | Rare                                |
# | ForeignKey      | If Person has many Students (like Guardian)          | `Student -> Person` as `ForeignKey` |
# | ManyToMany      | If many Persons can be Students in different roles   | Used in complex systems             |
