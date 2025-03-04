# Give tweets where the len(content) > 15.  
# Finally, return a DataFrame containing only the 'tweet_id'.
import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
   isValid = tweets['content'].str.len() > 15
   df = tweets[isValid]
   return df[['tweet_id']]