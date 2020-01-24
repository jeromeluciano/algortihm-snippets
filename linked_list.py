class LinkedList:
    # LinkedList constructor
    def __init__(self, value=None):
        if value is not None:
            self.head = self.Node(value)
        else:
            self.head = value
                
    def add(self, value):
        '''
            @classmethod LinkedList#add
            Inorder to add new element to the linked list we need to store the root node
            in a placeholder called current_node check if the current_node is None
            if its None it means the root node dont have a current value or node
            if its not None we can check if the next node have already Node inside it
            if the next node is None then we can create a new Node and assign it to the next node
        '''
        current_node = self.head
        if current_node is None:
            self.head = self.Node(value)
            return
        while current_node is not None:
            if current_node.next is None:
                current_node.next = self.Node(value)
                return
            current_node = current_node.next
    
    def print_elements(self):
        '''
            Inorder to print the elements inside the @LinkedList we need to grab a copy of 
            root node or the head node then we use While Loop to traverse each node
        '''
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def find(self, target):
        '''
        @classmethod LinkedList
        @find method will return the value of the target element
        '''
        current_node = self.head
        if current_node is not None:
            if current_node.value == target:
                return current_node.value
        while current_node is not None:
            if current_node.value == target:
                return target
            current_node = current_node.next
        return None

    def add_element_before(self, target, value):
        '''
        @classmethod LinkedList
            @add_element_before method will add new element before 
            the target element user specified.
        '''
        #[N(1),N(2),N(3),N(4)]
        current_node = self.head
        # if the target is the head or the root element
        if current_node.value == target:
            temp_next = current_node.next
            self.head = self.Node(value)
            self.head.next = current_node
            self.head.next.next = temp_next

        while current_node is not None:
            if current_node.next.value == target:
                temp_next = current_node.next
                new_node = self.Node(value)
                new_node.next = temp_next
                current_node.next = new_node
                return
            current_node = current_node.next
        

        # while the next node value is not equal to target it will run 
        # until the end of the loop    
        # while current_node.next.value != target:
        #     current_node = current_node.next
        # if current_node.next.value == target:
        #     # placeholders
        #     temp_current = current_node
        #     temp_next = current_node.next
        #     # swapping the nodes
        #     new_node = self.Node(value)
        #     current_node.next = new_node
        #     new_node.next = temp_next


    def get_last(self):
        '''
            @return Node value, None if node is None
            The @get_last method will get the last element in the @LinkedList
        '''
        current_node = self.head
        if current_node is None:
            return None
        while current_node is not None:
            current_node = current_node.next
            if current_node is not None:
                if current_node.next is None:
                    return current_node.value
        return None
    # Node class which contain the value of the node and the pointer to next Node
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None


test = LinkedList()
test.add(100)
test.add(200)
test.add(300)
test.add(400)
test.add_element_before(300, 800)

#test.print_elements()

print(test.find(800))
#print(test.get_last())
