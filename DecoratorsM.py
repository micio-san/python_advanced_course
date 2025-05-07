#A decorator is a funcion that extends the behavior of another function without explicitly modifying it.
#Pass thebase func as argument to the decotator funcion.
#@add_spinkles
#get_icecream("vanilla")

def add_spinkles(func):
    def wrapper():
        print("adding sprinkles")
        func()
    return wrapper

#to apply a decorator to a function, use the @ symbol followed by the decorator name before the function definition.
@add_spinkles
def get_icecream():
    print("here is your ice cream")

get_icecream()