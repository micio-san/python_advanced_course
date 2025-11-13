"""Itertools is a module in python that provides tools for efficient looping and data combos, it helps to
handle infinite or large sequences efficiently, combine and filter data elegantly and avoid writing manual
loops"""
import itertools 
import operator
#INFINITE!!
#These iterators never end — perfect for generators, pipelines, or testing.
def infinite_example(start, step):
    counter = itertools.count(start, step) #passing a start, if no step, default 1, counts a seq from start, goes up everytime by step
    for c in counter:
        print(c)
        if c==50: #I would suggest stoppoing it :D
            break

infinite_example(10, 5)
#another infinite iterator is REPEAT,  repeats an element
def repeat_example(element, max_repeats):
    repeater= itertools.repeat(element, max_repeats)
    for val in repeater:
        print(val)

repeat_example("hello",10) #repeats element, the number of times passed in max_repeat, if max_repeat not passed, goes forever
"""another infinite iterator is CYCLE, cycle over an sequence for n number of times

Iterators that Terminate
These work with finite sequences and are very common."""

def accumulate_example(elements):
    running_sum=itertools.accumulate(elements)
    print(list(running_sum))

accumulate_example([1,2,3,4,5,6,7,8,9]) #[1, 3, 6, 10, 15, 21, 28, 36, 45] Running totals or cumulative ops
"""EVERYTIME YOU CALL AN ITERATOR, WE CAN CALL THE LIST FUNCTION DIRECTY!!!!
next is CHAIN, simply list two iterable objs toghether """

nums = [1, 2, 3, 4, 5]
print(list(itertools.accumulate(nums)))                # [1, 3, 6, 10, 15]
print(list(itertools.accumulate(nums, operator.mul)))  # [1, 2, 6, 24, 120]
print(list(itertools.chain("AB", "CD")))               # ['A', 'B', 'C', 'D']
print(list(itertools.takewhile(lambda x: x < 4, nums)))# [1, 2, 3]

"""Combinatoric Iterators
These are used for permutations, combinations, and product generation (like nested loops)."""


#return all possible orderings!
print(list(itertools.permutations('ABC', 2))) #[('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
