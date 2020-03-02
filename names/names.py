import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:                        n * (what's inside of the loop)         O(n)
#     for name_2 in names_2:                        n * (what's inside of the loop)         O(n)
#         if name_1 == name_2:                          constant                                O(1)
#             duplicates.append(name_1)                 constant                                O(1)
# This runs in 7.124 seconds on my computer. It's runtime complexity is therefore O(n^2) --> its polynomial, so when the input size increases, the runtime or space used will grow at a faster rate. Not a great solution as it's not scalable.

# NEW SOLUTION 

# initialize a bst using the Binary Search Tree created earlier this week, passing in the value as the first item in names_1
# bst = BinarySearchTree(names_1[0])
# # for each name in namaes_1 
# for name in names_1:
#     # insert it into the bst
#     bst.insert(name)

# # for each name in nmaes_2
# for name in names_2:
#     # if the bts contains the name
#     if bst.contains(name):
#         # use duplicates.append(name)
#         duplicates.append(name)

# using this solution runs in 0.10642290115356445 seconds
# uses O(n) --> its linear

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# use set and intersection on list
# set() the larger list and then use the built-in function called interscetion() to compute the intersected list. intersection() is a first-class part of set.

list(set(names_1).intersection(names_2))

 # 0.0030982494354248047 seconds frist time it ran!