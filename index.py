import pandas as pd

df = pd.read_csv('jobs_posts.csv')

df.to_excel('jobs.xlsx')