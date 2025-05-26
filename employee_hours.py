import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['hours_worked'] = employees['out_time'] - employees['in_time'] 


    hour_tracker = employees.groupby(['event_day', 'emp_id'], as_index = False)['hours_worked'].sum().rename(columns={'event_day': 'day', 'hours_worked':'total_time'})
    return hour_tracker 