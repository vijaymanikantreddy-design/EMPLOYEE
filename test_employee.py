from employee import Employee_details

def test_employee_details():
    expexted_output = (
        "employee Name: Alice\n"
        "employee ID: E0110\n"
        "department: IT\n"
        "salary: 50000"
    )

    assert Employee_details("Alice", "E0110", "IT", 50000) == expexted_output
