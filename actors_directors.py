import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    filtered_df = actor_director.groupby(['actor_id', 'director_id'], as_index=False).agg(
        director_count = ('director_id', 'count'))
    
    grouped = filtered_df[filtered_df['director_count']>2]
     
    return grouped[['actor_id', 'director_id']]