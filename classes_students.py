import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    final_df = courses.groupby(['class'], as_index= False)['student'].count()
    mask = final_df['student']>=5
    
    return final_df.loc[mask, ['class']]