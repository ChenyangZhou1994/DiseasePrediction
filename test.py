import pandas as pd

df = pd.read_csv('./data/competition_A/submission_sample.csv')

df['hepatitis'] = 0.0

df.to_csv('./data/competition_A/submission_sample.csv', index=False)