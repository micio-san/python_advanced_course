#----------------LIST----------------#
#Lists ordered, mutable and allows duplicate and different types of elements
myList=["banana","cherry",22,"apple"]
#empty list initiator
myListTwo=list()
#print a range from 1 to end of list
myItem = myList[1:-1] #['cherry', 22]   
myItem2 = myList[::-1] #every second item, also -1 index, reversing the list!!
print(myItem, myItem2)
#check if exists():
if "banana" not in myList:
    print("yes")
#at end
myList.append("lemon")
#insertion at idx and removal
myList.insert(2,33)
myList.remove(33)
#remove all
myList.clear()
#copying the list
myListOG=["banana"]
myListCopy=myListOG
myListCopy.append("grapes")
print(myListCopy, myListOG) #Both get modified, pointers to same memory slot
myListActualCopy=myListOG.copy() #also list list(myListOG) or also slice myListOG[:]
myListActualCopy.append("blueberry")
print(myListActualCopy, myListOG) #['banana', 'grapes', 'blueberry'] ['banana', 'grapes']
#copying with list comprehesion
a = ["cow","cat"]
myListAgain = [i for i in a]
a.append("dog")
print( myListAgain,a) #['cow', 'cat'] ['cow', 'cat', 'dog']

#----------------TUPLE----------------#
#A tuple is a collection datatype that is similar to a list, but it's immutable, ordered. 
myTuple = ("T","o","r","a","d","o","r","a") #The parenthesis are optional! also initialized as myTuple = tuple("Tora", 14) 
myTupleSingle = ("tora",) #a tuple with a signle item, no comma and it's a string
#indexing as always
#changing
#myTuple[0]="Trixy" TypeError: 'tuple' object does not support item assignment
#counting elements
myTuple.count("a")
myTuple.index("r")
#tuple=>list 
myListT=list(myTuple)
myTupleAgain =tuple(myListT)
#slice
slicedTuple=myTuple[1:3] #('o', 'r')
#separation
capitalsEu = ("Berlin","Paris","Rome","Madrid")
germany,france,italy, spain=capitalsEu
#----------------DICTIONARIES----------------#
#Key-value pairs, unordered, mutable, the keys can only be immutable datatypes
myDict={"name":"Mark","age":29,"city":"Heingetorp"} #also dict(name:"Mark",age:29,city:"Heingetorp")
myDict["lastName"]="Svenson"
#deletion
del myDict["age"]
#eller myDict.pop("age")
for key in myDict.keys():
    #print(key)
    pass
for value in myDict.values():
    #print(value)
    pass
for key, value in myDict.items():
        #print(key, value, "\n")
    pass

#copying
myDictCopy = dict(myDict)
myDict["email"]="mark.svenson@gmail.com"
#merge with update
myFirstDict={"fruit":"Baboon", "animal":"Baboon","City":"Bergen"}
mySecondDict={"thing":"Bungalow"}
myFirstDict.update(mySecondDict)
print(myFirstDict)
#----------------SETS----------------#
#Sets are unordered, mutable and forbids duplicates
mySet ={1,4,3,2,5} #set([iterable || string that gets split])
myEmpytSet=set()
myEmpytSet.add(1)
myEmpytSet.discard(1)

for i in mySet:
    pass
    #print(i)

odds = {1,3,5,7,9}
even={2,4,6,8}
primes={2,3,5,7}
odds.union(even)#joined
#compare intersection 
i=odds.intersection(primes) #{3, 5, 7}
#compare extract differences
l=odds.difference(primes)#{1, 9}
