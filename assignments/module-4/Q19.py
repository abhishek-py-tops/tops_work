# # How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.

# try:
    
#     risky_operation()
# except SomeException:
    
#     handle_exception()
# finally:
    
#     cleanup()


try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input, please enter a number.")
finally:
    print("This block always executes.")
