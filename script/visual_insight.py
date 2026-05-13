import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


df = pd.read_csv('data/ai_job_market_dataset.csv')

job_trend = df[['Year','Job_Title']].copy()

job_trend_ai = job_trend.groupby(['Year', 'Job_Title']).size().unstack(fill_value='0')

plt.figure(figsize=(10, 6))

for subject in job_trend_ai.columns :
    plt.plot(
        job_trend_ai.index, job_trend_ai[subject],
        marker='o', linewidth=3, label=subject
        )
plt.title("Advances in Artificial Intelligence")
plt.xlabel('Year')
plt.ylabel('Count')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.savefig('output/Adv_AI.png')


df2 = pd.read_csv('data/ai_job_market_dataset.csv')

experience_trend = df2[['Year','Experience_Level']].copy()
experience_trend_ai = experience_trend.groupby(['Year', 'Experience_Level']).size().unstack(fill_value='0')

plt.figure(figsize=(10, 6))

for subject in experience_trend_ai.columns :
    plt.plot(
    experience_trend_ai.index, experience_trend_ai[subject],
    marker='o', linewidth=3, label=subject
    )
            
plt.title("Trend Experience in Artificial Intelligence")
plt.xlabel('Year')
plt.ylabel('Count')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.savefig('output/Trend_Experience_AI.png')



df3 = pd.read_csv('data/ai_job_market_dataset.csv')

skill_trend = df[['Year', 'Top_Skill']].copy()
skill_trend_ai = skill_trend.groupby(['Year', 'Top_Skill']).size().unstack(fill_value='0')

plt.figure(figsize=(10, 6))

for subject in skill_trend_ai.columns :
    plt.plot(
    skill_trend_ai.index, skill_trend_ai[subject],
    marker='o', linewidth=3, label=subject
    )
plt.title('Artifical Intellegence Skill Trend')
plt.xlabel('Year')
plt.ylabel('Count')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.savefig('output/Trend_Skill_in_AI')

