import pandas as pd
import os

df = pd.read_csv('../data/ai_job_market_dataset.csv')

df_2026 = df[df['Year'] == 2026]
df_2026 = df_2026.dropna(subset=['Year', 'Job_Title', 'Country', 'Company_Type', 'Experience_Level', 'Salary_USD', 'Remote', 'Top_Skill'])

df_2026.to_csv('../data/selection_2026.csv', index=False)
print(df_2026.describe())
