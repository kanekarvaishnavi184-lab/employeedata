from employee import employee_details

def test_employee_details_rahul():
    result=employee_details("rahul",101,"IT",45000)

    expected_emp=(
        "employee name:rahul\n"
        "employee id:101\n"
        "department:IT\n"
        "salary:45000"
    )

    assert result == expected_emp
