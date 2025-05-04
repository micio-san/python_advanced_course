#raising exceptions
x=-1
#if x < 0 :
#  raise Exception("x shpuld be positive")#Exception: x shpuld be positive
#also with assert statement
#assert(x>=0), "X SHOOULD BE POSITIVE" #AssertionError: X SHOOULD BE POSITIVE
#handling exception
try:
  a=4/0 #zero division error because zero division is not allowed
  b=a+"10"
except TypeError as typeErr:
   print(typeErr) #unsupported operand type(s) for +: 'float' and 'str'
except Exception as e: #also except ZeroDivisionError
   #catch exception type
   print(e)#division by error
else:
   print("all good")
finally:
   print("running always")

#define own exception by subclassin from the base exception
class ValueToHighError(Exception):
   pass

class ValueTooSmallError(Exception):
   def __init__(self, message, value):
      self.message=message
      self.value=value

def test_value(x):
   if x >100:
      raise ValueToHighError
   elif x< 2:
      raise ValueTooSmallError("Value is too small",x)
   
try:  
  test_value(200)
except ValueToHighError as e:
   print(e) #line 9, in test_value raise ValueToHighError ValueToHighError
except ValueTooSmallError as er:
   print(e.message, e.value)