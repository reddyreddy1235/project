class Employee:
    def __init__(self, emp_id, name, age, department):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.left = None  # Left child
        self.right = None  # Right child
        self.height = 1  # Height of the node (used in balancing)

class AVLTree:
    def __init__(self):
        self.root = None

    # Get the height of the node
    def height(self, node):
        if node is None:
            return 0
        return node.height

    # Get the balance factor of the node
    def get_balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Right rotate the subtree rooted with node
    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self.height(y.left), self.height(y.right)) + 1
        x.height = max(self.height(x.left), self.height(x.right)) + 1

        # Return the new root
        return x

    # Left rotate the subtree rooted with node
    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self.height(x.left), self.height(x.right)) + 1
        y.height = max(self.height(y.left), self.height(y.right)) + 1

        # Return the new root
        return y

    # Insert an employee in the AVL tree
    def insert(self, root, employee):
        if not root:
            return employee

        # Perform the normal BST insert
        if employee.emp_id < root.emp_id:
            root.left = self.insert(root.left, employee)
        elif employee.emp_id > root.emp_id:
            root.right = self.insert(root.right, employee)
        else:
            return root  # No duplicates

        # Update the height of this ancestor node
        root.height = 1 + max(self.height(root.left), self.height(root.right))

        # Get the balance factor to check whether this node became unbalanced
        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and employee.emp_id < root.left.emp_id:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and employee.emp_id > root.right.emp_id:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and employee.emp_id > root.left.emp_id:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and employee.emp_id < root.right.emp_id:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Search for an employee by emp_id
    def search(self, root, emp_id):
        if root is None or root.emp_id == emp_id:
            return root
        elif emp_id < root.emp_id:
            return self.search(root.left, emp_id)
        else:
            return self.search(root.right, emp_id)

    # Delete an employee by emp_id
    def delete(self, root, emp_id):
        if not root:
            return root

        # Perform the normal BST delete
        if emp_id < root.emp_id:
            root.left = self.delete(root.left, emp_id)
        elif emp_id > root.emp_id:
            root.right = self.delete(root.right, emp_id)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.get_min(root.right)
            root.emp_id = temp.emp_id
            root.name = temp.name
            root.age = temp.age
            root.department = temp.department
            root.right = self.delete(root.right, temp.emp_id)

        # Update height of the current node
        root.height = 1 + max(self.height(root.left), self.height(root.right))

        # Get the balance factor
        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Helper method to get the minimum node
    def get_min(self, root):
        while root.left:
            root = root.left
        return root

    # Inorder traversal to display employees
    def inorder(self, root):
        employees = []
        if root:
            employees += self.inorder(root.left)
            employees.append(f"{root.emp_id}: {root.name}, Age: {root.age}, Department: {root.department}")
            employees += self.inorder(root.right)
        return employees
