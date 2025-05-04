#----------------COLLECTIONS----------------#
#It's a module used to store different objects and iterate over them
#Counter/namedtuple/orderedDict/dequefaultDict/deque
from collections import Counter,namedtuple, OrderedDict, defaultdict
#-----------COUNTER------------------
#counts occurrences of values in a string?
a='aaabbbbcccac'
my_counter=Counter(a) #Counter({'b': 4, 'c': 4, 'a': 4})
my_counter.items() #dict_items([('a', 4), ('b', 4), ('c', 4)])
my_counter.keys()#dict_keys(['a', 'b', 'c'])
my_counter.values()#dict_values([4, 4, 4])
my_counter.most_common(1)#print most commons element
my_counter.elements()#<itertools.chain object at 0x0000016461A7AEC0>
list(my_counter.elements())#['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
#-----------NAMEDTUPLE------------------
#lightweitgh obj similar to a stuct, first argument is the 
#typename, usually the same name of the obj. the othrs, separatedby comma the values
Point = namedtuple('Point',"x,y")
pt=Point(1,-4) #Point(x=1, y=-4)
#-----------ORDERED_DICT------------------
#Like a regular dictionary but remembers the order of insertion even in older python versions
ordered_dict=OrderedDict()
ordered_dict["name"]="Julia"
ordered_dict["age"]=44
ordered_dict["city"]="Bucharest"
ordered_dict["profession"]="Comedian"
#-----------DEFAULT_DICT------------------
#also like a regualar dictionary with the peculiarity of having a default value
def_dict=defaultdict(int)
def_dict["a"]=1
def_dict["v"]=3
def_dict["x"]#0