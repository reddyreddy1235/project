from employee_operations import Employee, AVLTree

def display_menu():
    print("\nEmployee Management System")
    print("1. Add an Employee")
    print("2. Search for an Employee")
    print("3. Delete an Employee")
    print("4. Display All Employees")
    print("5. Exit")

def main():
    avl_tree = AVLTree()
    root = None

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add an employee
            emp_id = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            department = input("Enter Department: ")
            employee = Employee(emp_id, name, age, department)
            root = avl_tree.insert(root, employee)
            print(f"Employee {name} added successfully!")

        elif choice == '2':
            # Search for an employee
            emp_id = int(input("Enter Employee ID to search: "))
            employee = avl_tree.search(root, emp_id)
            if employee:
                print(f"Employee found: {employee.emp_id}: {employee.name}, Age: {employee.age}, Department: {employee.department}")
            else:
                print(f"Employee with ID {emp_id} not found.")

        elif choice == '3':
            # Delete an employee
            emp_id = int(input("Enter Employee ID to delete: "))
            root = avl_tree.delete(root, emp_id)
            print(f"Employee with ID {emp_id} deleted successfully!")

        elif choice == '4':
            # Display all employees
            employees = avl_tree.inorder(root)
            if employees:
                print("\nAll Employees:")
                for employee in employees:
                    print(employee)
            else:
                print("No employees in the system.")

        elif choice == '5':
            # Exit
            print("Exiting the system.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
