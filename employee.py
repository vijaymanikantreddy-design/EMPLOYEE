def empoyee_details(name,emp_id, department, salary):
    result = (
        f"employee Name: {name}\n"
        f"employee ID: {emp_id}\n"
        f"department: {department}\n"
        f"salary: {salary}"
    )
    return result

if __name__ == "__main__":
   name = "Alice"
    emp_id = "E0110"
    department = "IT"
    salary = 50000
   
    print(empoyee_details(name, emp_id, department, salary))
