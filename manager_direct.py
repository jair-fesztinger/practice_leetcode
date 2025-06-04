import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    yer = employee['managerId'].value_counts() 

    filtered_yer = yer[yer >= 5].index

    answer = employee[employee['id'].isin(filtered_yer)]

    return answer[['name']]