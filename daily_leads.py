import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    filtered_df = daily_sales.groupby(['date_id','make_name'], as_index=False).agg(
        unique_leads = ('lead_id', 'nunique'),
        unique_partners = ('partner_id', 'nunique')
    )
    return filtered_df