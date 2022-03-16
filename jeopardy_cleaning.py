import pandas as pd

scores = pd.read_csv('jeopardy_scores.csv')
scores = scores.drop('Unnamed: 0',axis=1)
scores['key'] = scores['question2'] + scores['gameID'].astype(str) + scores['round'].astype(str)

dd = pd.read_csv('dailydoubles.csv')
dd = dd.drop('Unnamed: 0', axis=1)
dd['isDD'] = 1
dd['key'] = dd['question'] + dd['gameID'].astype(str) + dd['round'].astype(str)

    
merged_df = scores.join(dd, how='left', on='key')
print(merged_df.head(10))