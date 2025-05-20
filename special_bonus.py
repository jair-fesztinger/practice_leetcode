import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    def compute_bonus(row):
        if (row['employee_id']%2 == 1) & (not row['name'].startswith('M')):
            return row['salary']
        else:
            return 0
    
    employees['bonus'] = employees.apply(compute_bonus, axis = 1)
    
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')