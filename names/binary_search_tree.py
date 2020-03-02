# import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # LEFT CASE
        # check if our new nodes value is less than the current nodes value
        if value < self.value:
            # does it have a child to the left?
            if not self.left:
                # place our new node here
                self.left = BinarySearchTree(value)
            # otherise 
            else:
                # repeat process for the left --> turn around and 
                return self.left.insert(value)
                
        # RIGHT CASE
        # check if the new nodes value is greater than or equal to the current nodes value
        if value >= self.value:
            # does it have a child to the right?
            if not self.right:
                # place one here
                self.right = BinarySearchTree(value)
            # otherwise
            else:
                # repeat the process for the right
                return self.right.insert(value)
        
        # Compare root node
            # If lesser go to left child
        # If greater or equal to go to right child
        # Else try again starting from the child on appropriate

    # if exsists then add to right: greater than or equal to --> add to right 
    # AND less than -->  add to left

    # minimum value, store values unitl we get to the None, return that value


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # BASE CASE 
        # if target eqauls the self.value 
        if target == self.value:
            # return true
            return True


        # LEFT CASE
        # if the target is less than value
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)

         # RIGHT CASE
        if target > self.value:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # BASE CASE 
        # if empty tree
            # return none
        if not self.right:
            return self.value
        # return none
        else:
            return self.right.get_max()
        # RECURSIVE CASE
        # if there is no right value
            # return the root node value
        # otherwise 
            # return get max of the 

    # ITERATIVE GET_MAX

    # def get_max(self):
    # maxVal = self.value
    # rightTree = self.right
    # while rightTree != None:
    #   if rightTree.value > maxVal:
    #     maxVal = rightTree.value
    #   rightTree = rightTree.right
    # return maxVal


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
    # each node has a value - each node we want every value -> callback(node.value)
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

        # if not self.left and not self.right:
        #     return cb(self.value)       
        # if self.left and not self.right:
        #     return self.left.for_each(cb)
        # if self.right and not self.left:
        #     return self.right.for_each(cb)
        # else:
        #     return (self.left.for_each(cb), self.right.for_each(cb))


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal DFT
    def in_order_print(self, node): 
        # find minimun value --> go far left
        # print the nodes value
        # move right once and continue left until a new leaf is found. 
        # print this value
        # Then repeat until all on left side are printed
        # base case: if no childern to left print the root

        # current_node = node
        # if not self.left and not self.right:
        #     print(node.value) 
        # if node == None: 
        #     return
        if node:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)
        #     return print(node.value)
        # print(node.value)
        # if node.right:
        #     self.in_order_print(node.right)
            # return print(node.value)


            # at node, move to child - can't move return value
        # for each node we want to left,
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create an empty queue
        queue = Queue()
        # add the starting node to the queue
        queue.enqueue(node)
        # iterate over the queue
        while queue.len() > 0:
            # set the current_node to the first item in the q
            current_node = queue.dequeue()
            # then print the current value
            print(current_node.value)
            # if the current node has a left child
            if current_node.left:
                # call enqueue on the current left
                queue.enqueue(current_node.left)
            # if the current node has a right child
            if current_node.right:
                # call enqueue on the current right
                queue.enqueue(current_node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # create an empty stack
        stack = Stack()
        # add the starting node to the stack
        stack.push(node)
        # iterate over the stack
        while stack.len() > 0:
             # pop the stack off in to current node
            current_node = stack.pop()
            # then print the current value
            print(current_node.value)
            # if the current node has a left child
            if current_node.left:
                # call push on the current left
                stack.push(current_node.left)
            # if the current node has a right child
            if current_node.right:
                # call enstack on the current right
                stack.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
