#the random module, secrets module for cryptography, the numpy module for random array genration mdoule
import random #sudo random(number seem random bu are repruducable)
#the secrets module is used for cryptography and is not reproducible, should be used for passwords, tokens, etc. IT ONLY HAS 3 FUNCTIONS
import secrets
#it stands for numerical python and " and provides support for arrays, matrices, and many mathematical functions to operate on these data structures.
import numpy as np
a = random.random() #random number between 0 and 1
b= random.uniform(1,5) #produce random FLOAT
c= random.randint(1,5) #produce random INTEGER incles the upper and lower bound7
d=random.randrange(1,10) #produce random INTEGER but not include the upper bound
e=random.normalvariate(0,1) #produce random number with normal distribution with mean 0 and standard deviation 1
myList = [1,5,6,7,8,9,12,3,1]
f= random.choice(myList) #chooses a random value from the list
g= random.sample(myList, 3) #chooses 3 random values from the list without replacement
h= random.choices(myList, k=3) #chooses 3 random values from the list with replacement
i= random.shuffle(myList) #shuffles the list in place
#all these are sudo random and can be reproduced by using the seed function
random.seed(1) #
w= random.random() #0.13436424411240122 
x=random.randint(1,10)#2
random.seed(1) #
y= random.random()#0.13436424411240122
z=random.randint(1,10)#2

#_____________________SECRETS_______________________________

myListSM = [8,3,1,7,9,5,2,4,6]
asm = secrets.randbelow(10) #Return a random int in the range [ exclusive_upper_bound).
bsm=secrets.randbits(4) #Return a non-negative int with k random bits. (4 bits = can have 4 different random binary value, highest being 1111 =15)
csm=secrets.choice(myListSM) #Return a randomly chosen element from a non-empty sequence.

#_____________________NUMPY_______________________________

an= np.random.rand(3); #produces 3 random number between 0 and 1, one dimension array
bn=np.random.randint(0,20,size=(3,1)) #produces 3 arrays  with one random number between 0 and 20 [[0][15][10]]
cn= np.array([[1,2,3],[4,5,6],[7,8,9]]) #creates a 2D array with 3 rows and 3 columns
dn= np.random.choice(cn.flatten(), 3) #chooses 3 random values from the array without replacement
en=np.random.shuffle(cn) #only along the first axis, in the same array
print(cn, en)