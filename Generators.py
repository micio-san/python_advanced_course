#They are a special type of iterator, they let you generate values on the fly, INSTEAD OF STORING IN MEMORY all at once like a list,
#making them more MEMORY EFFICIENT.  They are created like a normal functions, except you have to use YIELD instead of return
def count_up(n):
    count=1
    while count <= n:
        yield count
        count+=1

def count_2(n):
    count=1
    while count <= n:
        return count
        count += 1

#This doesn’t run the code immediately, it returns a generator object, which you can iterate over:
num1= count_up(4)
num2=count_2(5)

print(num1)#<generator object count_up at 0x000001ADDFD94DC0>
print(num2)#1

for x in num1:
    print(x)

#Each time through the loop, the function pauses at yield, remembers its state, and resumes next time.
#LIST COMPREHENSION
squares = (x * x for x in range(5))
print(squares)        # <generator object ...>
for s in squares:
    print(s)

#Memory Efficient – They don’t store everything in memory.
#Lazy Evaluation – Values are produced only when needed.
#Infinite Sequences – You can generate endless streams of data safely.
#GENERATORS ARE USED TO WORK WITH LARGE SEQUENCES OF DATA,

def fibonacci(limit):
    a,b=0,1
    while a < limit:
        yield a
        #until a is the same size as limit a =b and b = a+b a=0, b=1+0/ a=1, b=1(prev)+a
        a,b = b,a+b

for num in fibonacci(10):
    print(num)

#generator to read a file line by line:
def get_from_file(addy):
    with open(addy,"r") as file:
        for f in file:
            yield f.strip()

lines = get_from_file()
for x in lines:
    print(x)
    print("-----------------------------")
