import requests
import json

BASE_URL = "http://localhost:8080/employees"

# Function to get all employees
def get_all_employees():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("All Employees:")
        print(response.json())
    else:
        print("Failed to fetch employees. Status Code:", response.status_code)

# Function to get an employee by ID
def get_employee_by_id(employee_id):
    response = requests.get(f"{BASE_URL}/{employee_id}")
    if response.status_code == 200:
        print(f"Employee {employee_id}:")
        print(response.json())
    else:
        print(f"Failed to fetch employee {employee_id}. Status Code:", response.status_code)

# Function to create a new employee
def create_employee(name, position, salary):
    payload = {
        "name": name,
        "role": position,
        "salary": salary
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(BASE_URL, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        print("Employee created successfully:")
        print(response.json())
    else:
        print("Failed to create employee. Status Code:", response.status_code)

# Function to update an existing employee
def update_employee(employee_id, name, position, salary):
    payload = {
        "name": name,
        "role": position,
        "salary": salary
    }
    headers = {"Content-Type": "application/json"}
    response = requests.put(f"{BASE_URL}/{employee_id}", data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        print(f"Employee {employee_id} updated successfully:")
        print(response.json())
    else:
        print(f"Failed to update employee {employee_id}. Status Code:", response.status_code)

# Function to delete an employee
def delete_employee(employee_id):
    response = requests.delete(f"{BASE_URL}/{employee_id}")
    if response.status_code == 204:
        print(f"Employee {employee_id} deleted successfully.")
    else:
        print(f"Failed to delete employee {employee_id}. Status Code:", response.status_code)

# Test the functions
if __name__ == "__main__":
    # Get all employees
    #get_all_employees()

    # Create a new employee
    create_employee("John Doe", "Software Engineer", 70000)

    # Get all employees again to verify the new addition
    #get_all_employees()

    # Update the employee with ID 1 (update this ID as needed)
    update_employee(1, "Jane Doe", "Senior Software Engineer", 90000)

    # Get the updated employee details
    #get_employee_by_id(1)

    # Delete the employee with ID 1
    #delete_employee(1)

    # Verify deletion by fetching all employees again
    get_all_employees()
