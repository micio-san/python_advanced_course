#The Built-in Debugger: pdb
#Modern Debuggers (Visual Studio Code, PyCharm, etc.)
#trace module See which lines execute

#PBD
import pdb
#Pbd is part of py_std labrary, it lets you pause your program and inspect what’s happening interactively.
def divide(a,b):
    pdb.set_trace() # pauses execution here
    return a/b

#divide(10,2) 
#When you run this, you’ll drop into a debugger prompt like:
#> <stdin>(5)divide()
#(Pdb): Options are
# n new line
# s step into function
# c continue
# p<val> print variable
#q quit
#You can also start your script under pdb, from cmd
#****python -m pdb my_script.py

#Since py3.7 you can also just call the breakpoint() shortcut, same as import pdb sdb.set_trace()

def average(numbers):
    total = 0
    for n in numbers:
        breakpoint()
        total += n
    avg = total / len(numbers)
    return round(avg, 2)

nums = [2, 4, 6, 8, 10, "12"]
print("Average:", average(nums))
