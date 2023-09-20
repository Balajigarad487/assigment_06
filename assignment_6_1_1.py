import json

# Define an Employee class
class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Read employee data from JSON file
def read_employee_data(filename):
    employee_list = []
    with open(filename, 'r') as file:
        data = json.load(file)
        for emp_data in data['employees']:
            employee = Employee(emp_data['Name'], emp_data['DOB'], emp_data['Height'], emp_data['City'], emp_data['State'])
            employee_list.append(employee)
    return employee_list

# Print employee objects
def print_employee_objects(employee_list):
    for employee in employee_list:
        print(f"Name: {employee.name}, DOB: {employee.dob}, Height: {employee.height}, City: {employee.city}, State: {employee.state}")

# Main function
if __name__ == "__main__":
    employee_file = "employee.json"
    employees = read_employee_data(employee_file)
    print("List of Employee Objects:")
    print_employee_objects(employees)
