import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:

    scores['rank'] = scores['score'].rank(method = 'dense', ascending = False)

    updated_scores = scores.sort_values(by = ['score', 'rank'], ascending = False)
    
    return updated_scores[['score', 'rank']]