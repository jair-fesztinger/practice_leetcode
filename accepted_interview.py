import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    edited = rounds.groupby(['interview_id'], as_index = False)['score'].sum()
    print(edited)
    yep = pd.merge(candidates, edited, on = "interview_id", how = "inner")

    select = yep[(yep['years_of_exp']>=2) & (yep['score']>15)]
    return select[['candidate_id']]