# What relationship is appropriate for Course and Faculty?
# The most appropriate relationship between Course and Faculty is:

# 🔷 Many-to-One Relationship
# Because:

# One Faculty can teach many Courses.

# But each Course is typically taught by one Faculty member.

# from django.db import models

# class Faculty(models.Model):
#     name = models.CharField(max_length=100)
#     department = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Course(models.Model):
#     title = models.CharField(max_length=100)
#     code = models.CharField(max_length=10)
#     faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)  # Many-to-One

#     def __str__(self):
#         return self.title
