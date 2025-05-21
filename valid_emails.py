import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    
    pattern = r'^[A-Za-z][\w\.-]*@leetcode\.com$'
    new_df = users[users['mail'].str.match(pattern)]

    return new_df