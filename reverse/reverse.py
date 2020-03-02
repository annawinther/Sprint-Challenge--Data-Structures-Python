class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED
    # 1 --> 2 --> 3 --> None
    # 3 --> 2 --> 1 --> None

    # set the current node to the head and start with setting the prev to be none as ther are no previous
    current_node = self.head
    previous = None
    # loop over while the head isn't none
    while current_node:
      # set the new node to be the next of the current node's next node in the list
      new_node = current_node.next_node
      # set the current node's next node to be the previous
      current_node.next_node = previous
      # set the previous to be the current node
      previous = current_node
      # and then set the current node to be the next
      current_node = new_node
    # once finished update the head to be the previous
    self.head = previous
    
    

   