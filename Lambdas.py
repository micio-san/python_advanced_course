#Lambdas 
#a lambda function is a small anonymous function that takes as many arguments as required
x = lambda a:a+10 #x(3)13

#The power of lambda is better shown when you use them as an 
#anonymous function inside another function.
#Say you have a function definition that takes one argument, 
# and that argument will be multiplied with an unknown number:
def myfunc(n):
  return lambda a : a * n
#Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))