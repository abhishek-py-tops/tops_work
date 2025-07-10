# What is used to check whether an object o is an instance of class A?
# You can use the built-in isinstance() function.

# isinstance(object, class)

# class A:
#     pass

# o = A()

# print(isinstance(o, A))   # ✅ Output: True

# class A:
#     pass

# class B(A):
#     pass

# obj = B()

# print(isinstance(obj, A))  # ✅ True, because B inherits from A
