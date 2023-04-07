class Tree:
    def __init__(self, root):
        self.root = root
        self.tree = {}
    
    def get_root(self):
        return self.root
    
    def add_branch(self, start, end, path):
        if start in self.tree:
            self.tree[start][path] = end
        else:
            self.tree[start] = {path: end}
    
    def tree_to_image(self):
        #TODO
        #-Get library to show tree
        #-Transform tree format into image with library
        
        pass
