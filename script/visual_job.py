import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os

os.makedirs('output', exist_ok=True)
df_avg = pd.read_csv('data/processed/average_salary_by_experience_2026.csv')

plt.figure(figsize=(10, 6))
sns.barplot(data=df_avg.sort_values('Salary_USD', ascending=False), x='Experience_Level', y='Salary_USD', palette='magma')
ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.xlabel('Experience Level') 
plt.ylabel('Average Salary (USD)')
plt.title('Average Salary by Experience Level in 2026')
plt.savefig('output/average_salary_by_experience_2026.png', bbox_inches='tight')

df_com_analysis = pd.read_csv('data/selection_2026.csv')

plt.figure(figsize=(10, 8))
sns.scatterplot(data=df_com_analysis.sort_values('Salary_USD', ascending=False), x='Salary_USD', y='Job_Title')
plt.title('Comparative Analysis of Average Salaries by Job Title in 2026')
plt.xlabel('Average Salary (USD)')
plt.ylabel('Job Title')
plt.savefig('output/comparative_analysis_2026.png', bbox_inches='tight')


df_corr_country_job_title = pd.read_csv('data/processed/correlation_country_job_title_2026.csv')

plt.figure(figsize=(10, 6))
sns.heatmap(df_corr_country_job_title.set_index('Country').T, annot=True, cmap='coolwarm', cbar=False)
plt.title('Correlation between Country and Job Title in 2026')
plt.xlabel('Country')
plt.ylabel('Job Title')
plt.savefig('output/correlation_country_job_title_2026.png', bbox_inches='tight')


df_company_profile = pd.read_csv('data/processed/company_profile_2026.csv')

plt.figure(figsize=(10, 6))
sns.barplot(data=df_company_profile.sort_values('Average_Salary', ascending=False), x='Company_Type', y='Average_Salary')
ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.title('Average Salary by Company Type in 2026')
plt.xlabel('Company Type')
plt.ylabel('Average Salary (USD)')
plt.xticks(rotation=45)
plt.savefig('output/average_salary_by_company_type_2026.png', bbox_inches='tight')


df_exper_job_title = pd.read_csv('data/processed/comparative_experience_job_title_2026.csv')

plt.figure(figsize=(12, 8))
sns.heatmap(df_exper_job_title.set_index('Experience_Level').T, annot=True, cmap='YlGnBu', cbar=True, fmt='.0f')
plt.title('Comparative Analysis of Average Salaries by Experience Level and Job Title in 2026')
plt.xlabel('Experience Level')
plt.ylabel('Job Title')
plt.savefig('output/comparative_experience_job_title_2026.png', bbox_inches='tight')

df_skill_impact = pd.read_csv('data/processed/skill_impact_2026.csv')

plt.figure(figsize=(10, 6))
sns.barplot(data=df_skill_impact.sort_values('Salary_USD', ascending=False), x='Top_Skill', y='Salary_USD', palette='viridis')
ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.title('Impact of Top Skills on Salary in 2026')
plt.xlabel('Top Skill')
plt.ylabel('Average Salary (USD)')
plt.savefig('output/skill_impact_2026.png', bbox_inches='tight')

df_remote_impact = pd.read_csv('data/processed/remote_impact_2026.csv')

plt.figure(figsize=(8, 6))
sns.barplot(data=df_remote_impact.sort_values('Salary_USD', ascending=False), x='Remote', y='Salary_USD', palette='Set2')
ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
plt.title('Impact of Remote Work on Salary in 2026')
plt.xlabel('Remote Work')
plt.ylabel('Average Salary (USD)')
plt.savefig('output/remote_work_impact_2026.png', bbox_inches='tight')

df_corr_experience_job_title = pd.read_csv('data/processed/correlation_experience_job_title_2026.csv')

plt.figure(figsize=(10, 6))
sns.heatmap(df_corr_experience_job_title.set_index('Experience_Level').T, annot=True, cmap='coolwarm', cbar=False)
plt.title('Correlation between Experience Level and Job Title in 2026')
plt.xlabel('Experience Level')
plt.ylabel('Job Title')
plt.savefig('output/correlation_experience_job_title_2026.png', bbox_inches='tight')


sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(4, 2, figsize=(20, 30))
fig.suptitle('Dashboard Analisis Karir & Gaji AI 2026', fontsize=35, fontweight='bold', y=1.02)


formatter = ticker.StrMethodFormatter('{x:,.0f}')


sns.barplot(ax=axes[0, 0], data=df_avg.sort_values('Salary_USD', ascending=False), 
            x='Experience_Level', y='Salary_USD', palette='magma')
axes[0, 0].set_title('Average Salary by Experience', fontsize=18, fontweight='bold')
axes[0, 0].yaxis.set_major_formatter(formatter)


sns.scatterplot(ax=axes[0, 1], data=df_com_analysis, x='Salary_USD', y='Job_Title', hue='Experience_Level', palette='viridis')
axes[0, 1].set_title('Salary Distribution by Job Title', fontsize=18, fontweight='bold')
axes[0, 1].xaxis.set_major_formatter(formatter)


sns.heatmap(ax=axes[1, 0], data=df_corr_country_job_title.set_index('Country').T, annot=True, cmap='coolwarm', fmt='d')
axes[1, 0].set_title('Talent Distribution per Country', fontsize=18, fontweight='bold')


sns.barplot(ax=axes[1, 1], data=df_company_profile.sort_values('Average_Salary', ascending=False), 
            x='Company_Type', y='Average_Salary', palette='Blues_r')
axes[1, 1].set_title('Average Salary by Company Type', fontsize=18, fontweight='bold')
axes[1, 1].yaxis.set_major_formatter(formatter)


sns.heatmap(ax=axes[2, 0], data=df_exper_job_title.set_index('Experience_Level').T, annot=True, cmap='YlGnBu', fmt='.0f')
axes[2, 0].set_title('Salary Matrix: Job Title vs Experience', fontsize=18, fontweight='bold')

sns.barplot(ax=axes[2, 1], data=df_skill_impact.sort_values('Salary_USD', ascending=False), 
            x='Top_Skill', y='Salary_USD', palette='viridis')
axes[2, 1].set_title('Impact of Top Skills on Salary', fontsize=18, fontweight='bold')
axes[2, 1].yaxis.set_major_formatter(formatter)

sns.barplot(ax=axes[3, 0], data=df_remote_impact.sort_values('Salary_USD', ascending=False), 
            x='Remote', y='Salary_USD', palette='Set2')
axes[3, 0].set_title('Impact of Remote Work on Salary', fontsize=18, fontweight='bold')
axes[3, 0].yaxis.set_major_formatter(formatter)

sns.heatmap(ax=axes[3, 1], data=df_corr_experience_job_title.set_index('Experience_Level').T, annot=True, cmap='rocket_r', fmt='d')
axes[3, 1].set_title('Talent Correlation: Exp vs Job', fontsize=18, fontweight='bold')

plt.tight_layout(rect=[0, 0, 1, 0.98])
plt.savefig('output/full_dashboard_2026.png', bbox_inches='tight', dpi=300)
plt.show()