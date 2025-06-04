import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    today = delivery[delivery['order_date']==delivery['customer_pref_delivery_date']] #df

    perc = ((today['customer_id'].count())/ (delivery['customer_id'].count()))*100

    answer = pd.DataFrame({'immediate_percentage': [perc.round(2)]})
    return answer