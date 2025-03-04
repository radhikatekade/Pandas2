# Filter the DF to only include rows where the author_id == viewer_id. 
# Remove duplicate author_id entries and sort the results before returning the final DF.

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views.drop(views[views['author_id'] != views['viewer_id']].index)
    df.drop_duplicates(subset=['author_id'], inplace = True)
    df.sort_values(by=['author_id'], inplace = True)  
    return df[['author_id']].rename(columns = {'author_id': 'id'})