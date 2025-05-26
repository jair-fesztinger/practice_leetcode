import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    final_df = (teacher.groupby(['teacher_id'], as_index = False)['subject_id'].nunique()
    .rename(columns = {'subject_id' : 'cnt'}))

    return final_df[['teacher_id', 'cnt']]