import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:

    ads['click'] = ads['action'] == 'Clicked'
    ads['view'] = ads['action'] == 'Viewed'
    
    grouped_df = ads.groupby(['ad_id']).agg(
        total_clicks = ('click', 'sum'),
        total_views = ('view', 'sum')
    ).reset_index()

    grouped_df['ctr'] = grouped_df.apply(
        lambda row: 0 if (row['total_clicks'] + row['total_views'])==0
        else round(row['total_clicks'] / (row['total_clicks'] + row['total_views'])*100, 2), axis = 1
    )

    answer = grouped_df[['ad_id', 'ctr']].sort_values(by = ['ctr', 'ad_id'], ascending = [False, True])
    return answer