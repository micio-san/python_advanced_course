#A decorator is a function that extends the behavior of another function without explicitly modifying it.
#Pass thebase func as argument to the decorator function.
#@add_spinkles
#get_icecream("vanilla")
#They’re often used for:
  #Logging
  #Access control / authentication
  #Measuring execution time
  #Input validation
  # Caching results
  #Frameworks (Flask, FastAPI, Django)

def add_spinkles(func):
    def wrapper(*args, **kwargs): #to accept any number of arguments and keyword arguments 
                                  #bcuz we don't know how many n of args or the types of args(both positional and keywords) we would accept 
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

#all this is the same as writing add_chocolate = add_chocolate(get_icecream)
#print(add_chocolate("chocolate"))
get_icecream(flavor="vanilla")
#**5 MOST important decorators**
#------@property------
#treat a method as attribute, we DON'T HAVE ACCESS MODIFIERS IN PY, we use one _ before
#any attributes that we don't want to access outside of a class, starts with underscore and should be treated as private, U CAN, but shouldn't
class Circle:
    def __init__(self, radius):
        self._radius=radius # private radius= this.radius
    @property
    def radius(self):
        """Get radius from circle"""
        return self._radius
    @radius.setter
    def radius(self,new):
        if new >0:
            self.radius= new
        else:
            raise ValueError("radius must be a positive!")
    @radius.deleter
    def radius(self):
        del self.radius
#everytime we try to access the radius it will pass
#------ @staticmethod------
#use to denote a method inside of a class a static, something to belongs to the class and not to the instance of the class,
class Math:
    @staticmethod
    def add(x,y): #no self! not belonging to any instance
         return x+y
#organize functions into logical area
#______@classmethod_____
class Person:
    species="Home sapiens"
    @classmethod
    def get_species(cls):
        return cls.species
print(Person.get_species()) #Home sapiens
#it transofrms the first implicit arg to be the name or instance of the class, not an individual obj
#___functool.cache_____
#cache result of func calls in a recursive case
import functools

@functools.cache #writes a cache 
def fib(n):
    if n<2:
        return n
    return fib(n-1) + fib(n-2)
#1,1,2,3,5,8......
print(fib(10))
#_____dataclass_____
#automatically fills in boiler plate code
from dataclass import dataclass
@dataclass
class point:
    x:int
    y:int
#read content of class, focus on fields, picks the datatype and defines 3 methods we tipically we would have to write
# __init__, ___repr__, __eq__
print(p) calls repr method
