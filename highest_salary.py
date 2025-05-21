import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    
    #sort to find highest and ensure the column has distinct values
    distinct_salaries = sorted(employee['salary'].unique(), reverse=True)

    if 1<=N <= len(distinct_salaries):
        result = distinct_salaries[N-1]
    else:
        result = None
    
    return pd.DataFrame({f'getNthHighestSalary({N})': [result]})