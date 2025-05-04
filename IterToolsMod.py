#is a module in python that provides variuos functions that work on 
#iterables to produce a complex iterator
from itertools import product,permutations,combinations,accumulate
import operator
#product => Cartesian product of input iterables. Equivalent to nested for-loops.
a =[2,4,1]
b=[1,3]
prod=product(a,b) #<itertools.product object at 0x0000020637950300> 
prod_show=list(prod) #[(2, 1), (2, 3), (4, 1), (4, 3)]
#permutations
#return all possible ordering
perm=permutations(a)
perm_list = list(perm)#[(2, 4), (4, 2)] all possible orders
#combinations
#the combination func will make all possible combination with specified length
comb=combinations(a,2)
print(list(comb))#[(2, 4), (2, 1), (4, 1)]
#accumulate
#makes an iterator that return accumulated sums by default, but can also add other funcions
acc=accumulate(a) #[2, 6, 7]
acc_op=accumulate(a,operator.mul) #[2, 8, 8]
acc_op=accumulate(a,func=max) #[2, 8, 8]
#groupby
#return keys in groups from and iterable
