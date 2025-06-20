# common_python_errors.py
# This script is a learning tool to demonstrate common errors in Python.
# Each error is contained within a callable function.
# To see an error, uncomment the corresponding function call in the main block.

# Note: SyntaxError and IndentationError are special because they prevent
# the script from compiling/running in the first place. Therefore, the code

# that would cause them is commented out.

def cause_syntax_error():
    """
    SyntaxError: Occurs when the Python parser encounters code that does not
    conform to the Python language syntax. It's like a grammar mistake.
    
    The code below is commented out because a live SyntaxError would prevent
    the entire script from running.
    """
    print("This function demonstrates a SyntaxError.")
    # To see the error, try to run a python file with this line uncommented:
    # print "Hello, World!"  # In Python 3, print is a function, not a statement.
    # The line above uses Python 2 syntax and will raise a SyntaxError in Python 3.


def cause_indentation_error():
    """
    IndentationError: A specific kind of SyntaxError that occurs when code is
    not indented correctly. Python uses indentation to define code blocks.
    
    The code below is commented out because a live IndentationError would
    also prevent the script from running.
    """
    print("This function demonstrates an IndentationError.")
    # To see the error, try to run a python file with the 'print' line
    # below not indented correctly:
    # for i in range(5):
    # print(i)  # This line should be indented to be inside the for loop.


def cause_name_error():
    """
    NameError: Raised when you try to use a variable or function name that
    has not been defined yet.
    """
    print("This function will cause a NameError.")
    # 'my_variable' does not exist, so referencing it causes a NameError.
    print(my_variable)


def cause_type_error():
    """
    TypeError: Raised when an operation or function is applied to an object
    of an inappropriate type. For example, adding a string to an integer.
    """
    print("This function will cause a TypeError.")
    result = "hello" + 5
    print(result)


def cause_value_error():
    """
    ValueError: Raised when a function receives an argument that has the right
    type but an inappropriate value.
    """
    print("This function will cause a ValueError.")
    # The int() function can convert strings to integers, but it can't convert
    # the string 'abc' into a number.
    number = int("abc")
    print(number)


def cause_index_error():
    """
    IndexError: Raised when you try to access an index of a sequence (like a
    list or a tuple) that is out of range.
    """
    print("This function will cause an IndexError.")
    my_list = [1, 2, 3]
    # The list has indices 0, 1, and 2. Trying to access index 3 is an error.
    print(my_list[3])


def cause_key_error():
    """
    KeyError: Raised when you try to access a key in a dictionary that
    does not exist.
    """
    print("This function will cause a KeyError.")
    my_dict = {"name": "Alice", "age": 30}
    # The dictionary does not have a key named 'city'.
    print(my_dict["city"])


def cause_attribute_error():
    """
    AttributeError: Raised when you try to access an attribute or method on
    an object that doesn't have it.
    """
    print("This function will cause an AttributeError.")
    my_string = "hello"
    # Strings do not have a method called 'append'. Lists do.
    my_string.append(" world")


def cause_zero_division_error():
    """
    ZeroDivisionError: Raised when the second argument of a division or
    modulo operation is zero.
    """
    print("This function will cause a ZeroDivisionError.")
    result = 10 / 0
    print(result)


def cause_module_not_found_error():
    """
    ModuleNotFoundError: Raised when an import statement has trouble trying
    to load a module. This could be because the module does not exist or is
    not in the Python path.
    """
    print("This function will cause a ModuleNotFoundError.")
    # Assuming 'a_module_that_does_not_exist' is not a real module.
    import a_module_that_does_not_exist


# --- Main execution block ---
if __name__ == "__main__":
    # Choose which error you want to see by uncommenting the function call.
    # Remember to only run one at a time, as they will stop the script.
    
    error_functions = {
        "1": ("NameError", cause_name_error),
        "2": ("TypeError", cause_type_error),
        "3": ("ValueError", cause_value_error),
        "4": ("IndexError", cause_index_error),
        "5": ("KeyError", cause_key_error),
        "6": ("AttributeError", cause_attribute_error),
        "7": ("ZeroDivisionError", cause_zero_division_error),
        "8": ("ModuleNotFoundError", cause_module_not_found_error),
    }

    print("Welcome to the Python Error Learning Tool!")
    print("-----------------------------------------")
    print("SyntaxError and IndentationError are explained in their functions.")
    print("Select an error to trigger:")
    for key, (name, _) in error_functions.items():
        print(f"  {key}. {name}")

    choice = input("Enter the number of the error you want to see: ")

    if choice in error_functions:
        error_name, error_func = error_functions[choice]
        print(f"\n--- Triggering {error_name} ---")
        try:
            error_func()
        except Exception as e:
            print(f"\nSuccessfully caught the expected error!")
            print(f"Error Type: {type(e).__name__}")
            print(f"Error Message: {e}")
            print("--------------------------------------")
    else:
        print("Invalid choice. Please run the script again and select a valid number.")

