import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    
    largest_orders_df = orders.groupby(['customer_number'], as_index=False)['order_number'].count()

    updated_df = largest_orders_df.sort_values(by = 'order_number', ascending = False).head(1)
    
    return updated_df[['customer_number']]