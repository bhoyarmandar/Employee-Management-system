import csv
import os

file = "employees_project.csv"

# 1) Add Employee
def add_emp(employee):
    try:
        emp_id = input('enter emp id: ').strip().upper()
        name = input('enter emp name: ').strip().title()
        age = input('enter emp age: ').strip()
        department = input('enter emp dept: ').strip().title()
        job_role = input('enter role: ').strip().title()
        salary = input('enter emp salary: ').strip()
        joining_date = input('enter joining_date: ').strip()
    
        ae = False
        for i in employee:
            if i['employee_id'].strip().upper() == emp_id:
                print('Employee Already Exists !')
                ae = 1
                break
        else:
            emp_row = {
                'employee_id': emp_id, 
                'name': name, 
                'age': age, 
                'department': department, 
                'job_role': job_role, 
                'salary': salary, 
                'joining_date': joining_date
            }
            
            employee.append(emp_row)
            fieldnames = ['employee_id', 'name', 'age', 'department', 'job_role', 'salary', 'joining_date']
            with open(file, 'a', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writerow(emp_row)
            ae = True    
    
        if ae:
            print(f'Employee {name} added and saved sucessfully !')

    except Exception as e:
        print(f' Error Occurred: {e}')


# 2) Delete Employee
def delete_emp(employee):
    try:
        id = input('enter emp_id to delete : ').strip().upper()
        id_l = id.split(',')
        for il in id_l:
            il = il.strip().upper()
            for i in employee:
                if i['employee_id'].strip().upper() == il:
                    print('Employee Found')
                    employee.remove(i)
                    fieldnames = ['employee_id', 'name', 'age', 'department', 'job_role', 'salary', 'joining_date']
                    with open(file, 'w', newline='', encoding='utf-8') as f:
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(employee)
                            
                    print('Deleted sucessfully')
                    break      
            else:
                print("Employee doesn't exist")
    except Exception as e:
        print(f' Error Occurred: {e}')


# 3) Update Employee
def update_emp(employee):
    try:
        id = input('Enter Employee ID: ').strip().upper()
        id_l = id.split(',')
        for il in id_l:
            il = il.strip().upper()
            found = False
            for i in employee:
                if i['employee_id'].strip().upper() == il:
                    print(f"Employee found , Emp name is {i['name']} and id is {i['employee_id']}")
        
                    new_salary = input(f"Enter new salary (current salary:{i['salary']}): ").strip()
                    new_age = input(f"enter new age (current age is:{i['age']}): ").strip()
                    new_department = input(f"enter new department (current department is:{i['department']}): ").strip().capitalize()
                    new_job_role = input(f"enter new job_role (current job_role is:{i['job_role']}): ").strip().title()
        
                    if new_salary:
                        i['salary'] = new_salary
                    if new_age:
                        i['age'] = new_age
                    if new_department: 
                        i['department'] = new_department
                    if new_job_role:
                        i['job_role'] = new_job_role
        
                    found = True
                    break
            if found:
                fieldnames = ['employee_id', 'name', 'age', 'department', 'job_role', 'salary', 'joining_date']
                with open(file, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(employee)
                    
                print('Employee Updated sucessfully')
            else:
                print("Employee Doesn't exist")

    except Exception as e:
        print(f' Error Occurred: {e}')


# 4) View employee
def view_emp(employee):
    try:
        id = input('enter employee id: ').strip().upper()
        id_l = id.split(',')
        for il in id_l:
            il = il.strip().upper()
            for i in employee:
                if i['employee_id'].strip().upper() == il:
                    print(i)
                    print('viewed sucessfully')
                    break
            else:
                print("Employee Doesn't exist")
    except Exception as e:
        print(f' Error Occurred: {e}')


# 5) Search By Department
def search_by_dept(employee):
    try:
        dept = input('enter Employee dept: ').strip().capitalize()
        id_l = dept.split(',')
        
        for il in id_l:
            target_dept = il.strip().capitalize()
            found = False
            
            for i in employee:
                if i['department'].strip().capitalize() == target_dept:
                    print(f"ID: {i['employee_id']} | Name: {i['name']} | 'Department':{i['department']} | Role: {i['job_role']} | Salary: {i['salary']}")
                    found = True
                    
            if not found:
                print('No Employees with ', target_dept, 'department')
        
    except Exception as e:
        print(f' Error Occurred: {e}')


# 6) Main Menu Controller
def main():
    if not os.path.exists(file):
        print(f"Error: {file} not found in directory.")
        return

    with open(file, 'r', newline='', encoding='utf-8') as f:
        a = csv.DictReader(f)
        employee = []
        for i in a:
            employee.append(i)
            
    while True:
        print('\n **Employee Managememt System**')
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Update Employee")
        print("4. View Employee")
        print("5. Search by Department")
        print("6. Exit the Program")
        
        operation = input('enter opreation : ').strip()
        
        if operation == '1':
            add_emp(employee)
        elif operation == '2':
            delete_emp(employee)   
        elif operation == '3':
            update_emp(employee)   
        elif operation == '4':
            view_emp(employee)
        elif operation == '5':
            search_by_dept(employee)
        elif operation == '6':
            print('Exit the program , Goodbye!')
            break
        else:
            print('Invalid Operation! Please enter a number between 1 and 6.')

if __name__ == "__main__":
    main()