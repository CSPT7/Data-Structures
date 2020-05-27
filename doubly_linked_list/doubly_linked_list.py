"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
# INSTANTIATE THE DOUBLY-LINKED LIST DATA STRUCTURE
class ListNode:
    # __NOTE: A LINKED LIST (OF ANY KIND) IS A SERIES OF LINKED NODES; A NODE IS DESCRIBED BELOW:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next  # CREATE A POINTER TO THE NEXT NODE CALLED "CURRENT_NEXT"
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        
        # __POSSIBLE CONDITION 1: LINKED LIST WITH LENGTH 0
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = self.head
        
        # __POSSIBLE CONDITION 2: LINKED LIST WITH LENGTH 1 OR MORE
        elif self.length == 1:
            dummy_node = ListNode(value)
            dummy_node.next = self.head
            self.head = dummy_node
            self.length += 1


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        pass

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        pass

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):

        # __NOTE: TO RETURN THE VALUE OF THE TAIL LATER, IT MUST BE SAVED NOW, BEFORE IT IS REMOVED
        value_of_removed_node = self.tail.value

        # __POSSIBLE CONDITION 1: LINKED LIST WITH LENGTH 0
        if not self.tail:
            return

        # POSSIBLE CONDITION 2: LINKED LIST WITH LENGTH 1
        elif self.head == self.tail:
            self.head = None
            self.tail = None

        # POSSIBLE CONDITION 3: LINKED LIST WITH LENGTH 2+
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        # DECREMENT THE LENGTH OF THE ENTIRE DOUBLY LINKED LIST TO SHOW THAT TAIL HAS BEEN REMOVED
        self.length -= 1

        return value_of_removed_node


    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        
        # IF LIST IS EMPTY
        if not self.head:
            print("Your list is already empty.")
            return
        
        # IF LIST CONTAINS ONLY ONE ITEM
        elif self.head == self.tail:
            self.head = None
            self.tail = None
            return
        
        # IF LIST CONTAINS AT LEAST TWO NODES AND HEAD NEEDS TO BE DELETED
        elif node == self.head:
            self.head = node.next
            self.head.prev = None

        # IF LIST CONTAINS AT LEAST TWO NODES AND TAIL NEEDS TO BE DELETED
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None

        # IF LIST CONTAINS AT LEAST TWO NODES AND NON-HEAD OR TAIL NEEDS TO BE DELETED
        else:
            node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        
        highest_value = self.head.value
        current_node = self.head
        
        while current_node is not None:
            if current_node > 0:
                pass
            
        # == CASE 1 == DOUBLY LINKED LIST WITH NO NODES
        if not self.tail:
            return


