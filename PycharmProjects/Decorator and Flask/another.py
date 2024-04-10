# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        if args[0].is_login == True:
            function(args[0])

    return wrapper


# Use the decorator 👇

class User:
    def __init__(self, name):
        self.name = name
        self.is_login = False


@logging_decorator
def print_hello(user):
    print(f"How are you {user.name}")


new_user = User("Saifi")
new_user.is_login = True
print_hello(new_user)
