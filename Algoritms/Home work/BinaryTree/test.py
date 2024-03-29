class TreeNode:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return f"TreeNode({self.key})"

    def insert(self, key):
        if self.key is None:
            self.key = key
            return
        
        if key < self.key:
            if self.left is None:
                self.left = TreeNode(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = TreeNode(key)
            else:
                self.right.insert(key)
        else:
            raise ValueError(f"Key {key} already exists")
    
    def print_hierarchy(self, dir="root", level=0):
        print(f"[{dir}] #{level} = {self.key} | left = {self.left} | right = {self.right}")
        if self.left  is not None: self.left.print_hierarchy("left", level+1)
        if self.right is not None: self.right.print_hierarchy("right", level+1)


tree = TreeNode()
tree.insert(9)
tree.insert(17)
tree.insert(4)
tree.insert(3)
tree.insert(6)
tree.print_hierarchy()
tree.insert(3) # exception