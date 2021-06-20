'''Get a list sorted in a increasing order by the last element in each tuple
from a given list of  non-empty tuple'''

def last_element(n):
    return n[-1]

def sort_item_last(tuples):
    return sorted(tuples, key=last_element)

print(sort_item_last([(2,5),(1,2),(4,4),(2,3),(2,1)]))