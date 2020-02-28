from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if its not at capacity yet, keep filling in adding the next one
        # if it is at capacity then swap the oldest one (head) with the new that we want to add. 
        pass

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # start at the beginning by setting the node to be the head
        # loop over as long as there is a node passing in and adding that noe's value to the list_buffer_contents
        # then set the neode to be the next one

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
