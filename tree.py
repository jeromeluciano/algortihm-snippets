class Tree:
    def __init__(self, value):
        self.root = self.Node(value)
        print('{} in argument'.format(self.root))
    
    def add(self, value):
        self.root = self.add_node(self.root, value)

    def add_node(self, current, value):
        #   o
        #  / \
        # o   o
        if current == None:
            return self.Node(value)
            
        if value > current.value:
            current.rightChild = self.add_node(current.rightChild, value)
        elif value < current.value:
            current.leftChild = self.add_node(current.leftChild, value)
        else:
            return current
        return current

   
    class Node:
        def __init__(self, value):
            self.value = value
            self.leftChild = None
            self.rightChild = None
            print('Node instance created')

        
        # add node to the tree
        
            

                
            
                

tree = Tree(5)
tree.add(2)

print(tree.root.value)
print(tree.root.leftChild.value)

