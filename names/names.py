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


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
