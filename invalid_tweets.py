import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    
    #counts characters filter
    mask = tweets['content'].str.len() > 15

    return tweets.loc[mask,['tweet_id']]