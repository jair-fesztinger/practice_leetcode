import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    distinct_salaries = sorted(employee['salary'].unique(), reverse=True)

    if len(distinct_salaries) >= 2:
        result = distinct_salaries[1]
    else:
        result = None 

    return pd.DataFrame({f'SecondHighestSalary': [result]})