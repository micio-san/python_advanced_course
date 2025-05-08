#A decorator is a funcion that extends the behavior of another function without explicitly modifying it.
#Pass thebase func as argument to the decotator funcion.
#@add_spinkles
#get_icecream("vanilla")

def add_spinkles(func):
    def wrapper(*args, **kwargs): #to accept any number of arguments and keyword arguments
        print("adding sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_chocolate(func):
    def wrapper(*args, **kwargs): #to not call the function directly
        print("adding chocolate")
        func(*args, **kwargs)
    return wrapper

#to apply a decorator to a function, use the @ symbol followed by the decorator name before the function definition.
@add_spinkles
@add_chocolate
def get_icecream(flavor):
    print(f"here is your {flavor} ice cream")

get_icecream(flavor="vanilla")