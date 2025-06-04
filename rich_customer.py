import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    df = store[store['amount'] > 500]
    df['rich_count'] = len(df['customer_id'].unique())
    
    return df[['rich_count']].head(1)