import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    #filter
    mask = views[views['author_id']==views['viewer_id']]

    #rename
    foo = mask[['author_id']].drop_duplicates().rename(columns={'author_id': 'id'})

    return foo.sort_values('id', ascending = True)