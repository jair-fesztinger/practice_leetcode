import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(employee, department, 
        left_on = 'departmentId', 
        right_on = 'id', 
        how = 'left', 
        suffixes = ('', '_department'))

    #Merge Tables
    merged_df = merged_df.rename(columns={'name': 'Employee', 'name_department': 'Department', 'salary': 'Salary'})
    
    #incorporate new colum with the max per group
    merged_df['max_in_group'] = merged_df.groupby('Department')['Salary'].transform('max')

    #apply boolean mask and allows for duplicates
    highest_salaries_df = merged_df[merged_df['Salary'] == merged_df['max_in_group']]

    return highest_salaries_df[['Department', 'Employee', 'Salary']]