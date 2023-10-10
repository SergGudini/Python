class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        res = f'значение нашего узла: {self.value} '
        if self.left:
            res += f'значение левого: {self.left.value} '
        if self.right:
            res += f'значение правого: {self.right.value} '
        return res    
        
class BinaryTree:
    
    def __init__(self, root_value):
        self.root = Node(root_value)
        
    def add(self, value):
        res = self.search(self.root, value)
        
        if res[0] is None:
            new_node = Node(value)
            if value > res[1].value:
                res[1].right = new_node
            else:
                res[1].left = new_node
        else:
            print('Конец')
    
    def search(self, node, value, parent = None):
        if node == None or value == node.value:
            return node, parent
        if value > node.value:
            return self.search(node.right, value, node)
        if value > node.value:
            return self.search(node.left, value, node)

bt = BinaryTree(5)
bt.add(10)
bt.add(15)
bt.add(3)
bt.add(4)

print(bt.root)
#print(bt.search(bt.root, 8)[1])