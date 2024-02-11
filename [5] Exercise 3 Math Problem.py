print("MathHomework.py")

problem = input("Enter a math problem, or 'q' to quit: ")

while (problem != 'q'):
    try:
        print("The answer to", problem, "is:", eval(problem))
    except Exception as e:
        print("Invalid input. Please enter a valid math problem.")
    problem = input("Enter another math problem, or 'q' to quit: ")



# an exception is a type of runtime error
"""

while (problem != "q"):
    print("The answer to ", problem, "is:", eval(problem) )
    problem = input("Enter another math problem, or 'q' to quit: ")
"""

# Why we used 'except Exception as e'?
"""
except: This keyword starts the block of code that will be
executed if an exception is raised in the try block.

Exception: This is a built-in Python class that serves as the
base class for all built-in exceptions (except for system-exiting
exceptions, like SystemExit and KeyboardInterrupt).
By catching Exception, you're essentially catching
most of the common exceptions that can be raised.

as e: This part of the syntax allows you to assign the caught exception
to a variable, in this case, e. This is useful if you want to access
or print out the specific details of the exception.

The choice of 'e' as the variable name is a convention,
but it's not mandatory. You could use any valid variable name,
like 'except Exception as error: ' or 'except Exception as ex: '
but 'e' is concise and commonly used in this context.
"""

# What is eval()?
"""
In Python, eval() is a built-in function that parses and evaluates
a string as a Python expression and returns the result.
It allows for dynamic execution of Python programs,
which can both be powerful and dangerous.

x = 1
result = eval("x + 1")
print(result)  # Outputs: 2

"""