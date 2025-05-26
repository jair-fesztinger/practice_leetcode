import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    final_df = activity.sort_values(by = 'event_date').drop_duplicates(subset = 'player_id', keep='first', ignore_index=True)

    return final_df[['player_id', 'event_date']].rename(columns={'event_date':'first_login'})