import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    grouped = activities.groupby(['sell_date'], as_index=False).agg(
        num_sold = ('product', 'nunique'),
        products = ('product', lambda x: ','.join(sorted(set(x))))
    )
    return grouped[['sell_date', 'num_sold', 'products']]