from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # start with the first one, adding the item to the tail, and setting the current to the head 
        if self.storage.length == 0:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        # if its not at capacity yet, keep filling in adding the next one, setting the current to the tail
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        # if it is at capacity then swap the oldest one (head) with the new that we want to add. 
        else:
            if self.current == self.storage.tail:
                # set the current to be the head we want to swap with the new vlaue
                self.current = self.storage.head
            # otherwise
            else:
                # set current to be the next one
                self.current = self.current.next
                # set the item to be the new value of the current
            self.current.value = item

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # start at the beginning by setting the node to be the head
        node = self.storage.head
        # loop over as long as there is a node passing in and adding that noe's value to the list_buffer_contents
        while node:
            list_buffer_contents.append(node.value)
            # then set the node to be the next one
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
