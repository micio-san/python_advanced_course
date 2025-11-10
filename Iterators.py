#An iterator in any OBJECT IN PY THAT CAN BE LOOPED OVER (for,next) and it remembers 
# #where it left off each time you ask for the nxt value
#Iterable	An object you can get an iterator from (like list, tuple, str, dict, etc.)
#Iterator	The actual object that produces one value at a time when you call next()

nums =[10,3, 22] #this is the iterable
it = iter(nums) # turn it into an iterator
#after the last value is iterated over, next will raise *StopIteration*
#To BE AN ITERATOR AN OBJECT MUST HAVE TWO METHODS
it.__iter__() #return the iterator obj itself
it.__next__()  # returns the next value (or raises StopIteration)
#An iterator can be built from scratch

class CountUpTo:
    def __init__(self, max):
        self.max = max
        self.current = 1

    def __iter__(self):
        return self  # iterator must return itself
    
    def __next__(self):
        if self.current <=self.max:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration
        
#A generator is a shortcut for making an iterator, 
#instead of writing a full class with __iter__() and __next__(),
#you can just write a function with yield, and Python builds the iterator for you.
#**Iterator** class	Has __next__ and __iter__
#**Generator**	Uses yield and does the same thing automatically
