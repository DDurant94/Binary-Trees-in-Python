class TreeNode:
  def __init__(self,key):
    self.key = key
    self.left = None
    self.right = None
    
class BinaryTree:
  def __init__(self):
    self.root = None
    
  def insert(self,key):
    if self.root is None:
      self.root = TreeNode(key)
    else:
      self._insert_recursive(self.root, key)
      
  def _insert_recursive(self, node,key):
    if key < node.key:
      #look down the left side of the node because its value is less
      if node.left is None:
        node.left = TreeNode(key)
      else:
        self._insert_recursive(node.left, key)
    elif key > node.key:
      #look down the right side of the node because its value is greater
      if node.right is None:
        node.right = TreeNode(key)
      else:
        self._insert_recursive(node.right, key)
        
  def delete(self,key):
    self.root = self._delete_recursive(self.root,key)
  
  def _delete_recursive(self,root,key):
    if root is None:
      return root
    if key < root.key:
      #look down the left side of the node because its value is less
      root.left = self._delete_recursive(root.left, key)
    elif key > root.key:
      #look down the right side of the node because its value is greater
      root.right = self._delete_recursive(root.right, key)
    else:
      if root.left is None:
        return root.right
      elif root.right is None:
        return root.left
      temp = self._find_min_key(root.right)
      root.key = temp.key
      root.right = self._delete_recursive(root.right, temp.key)
    return root
  
  def _find_min_key(self,node):
    while node.left:
      node = node.left
    return node
  
  def search(self,key):
    return self._search_recursive(self.root,key)
  
  def _search_recursive(self,node,key):
    if node is None:
      return False
    if key == node.key:
      return True
    elif key < node.key:
      #look down the left side of the node because its value is less
      return self._search_recursive(node.left,key)
    else:
      #look down the right side of the node because its value is greater
      return self._search_recursive(node.right,key)
    
  def in_order_traversal(self):
    self._in_order_traversal_recursive(self.root)
    
  def _in_order_traversal_recursive(self,node):
    if node:
      #gets the smallest numbers first and works its way back up
      self._in_order_traversal_recursive(node.left)
      print(node.key, end=" ")
      self._in_order_traversal_recursive(node.right)
  
  def pre_order_traversal(self):
    self._pre_order_traversal(self.root)
    
  def _pre_order_traversal(self,node):
    if node:
      print(node.key, end=" ")
      #printing what the tree looks like from top to bottom in a list
      self._pre_order_traversal(node.left)
      self._pre_order_traversal(node.right)
      
  def post_order_traversal(self):
    self._post_order_traversal(self.root)
    
  def _post_order_traversal(self,node):
    if node:
      #printing from left side down to its bottom left child and prints that node up to its parent and down to the right side bottom and 
      # up to its next parent and repeats that through the whole tree
      self._post_order_traversal(node.left)
      self._post_order_traversal(node.right)
      print(node.key, end=" ")
      
  def print_tree(self):
    self._print_tree_recursive(self.root,0)
    
  def _print_tree_recursive(self,node,depth):
    if node is None:
      return
    #printing right side first then the left side 
    self._print_tree_recursive(node.right, depth +1)
    print("   " * depth + str(node.key))
    self._print_tree_recursive(node.left,depth +1)
     
if __name__ == "__main__":
  tree = BinaryTree()
  
  keys =[50,30,70,20,40,60,80]
  for key in keys:
    tree.insert(key)
    
    
  print("In-order traversal:")
  tree.in_order_traversal()
  
  print("\nPre-Order-Traversal:")
  tree.pre_order_traversal()
  
  print("\nPost-order Traversal:")
  tree.post_order_traversal()
  
  print("\nBinary tree structure::")
  tree.print_tree()
  
  
  search_key = 12
  if tree.search(search_key):
    print(f"Key {search_key} has been found")
  else:
    print(f"Key {search_key} can not been found")