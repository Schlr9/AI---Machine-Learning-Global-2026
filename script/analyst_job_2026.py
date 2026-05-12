import pandas as pd
import os

df_2026 = pd.read_csv('data/selection_2026.csv')
os.makedirs('data/processed', exist_ok=True)

comparative_analysis = df_2026.groupby('Job_Title')['Salary_USD'].mean().reset_index()
comparative_analysis = comparative_analysis.sort_values(by='Salary_USD', ascending=False)
print("Comparative Analysis of Average Salaries by Job Title in 2026:")
print(comparative_analysis)


average_salary_by_experience = df_2026.groupby('Experience_Level')['Salary_USD'].mean().reset_index()
print('\nAverage Salary by Experience Level in 2026:')
print(average_salary_by_experience)

comparative_Experience_job_title = pd.pivot_table(df_2026, values='Salary_USD', index='Experience_Level', columns='Job_Title', aggfunc='mean')
comparative_Experience_job_title = comparative_Experience_job_title.reset_index()
print('\nComparative Analysis of Average Salaries by Experience Level and Job Title in 2026:')
print(comparative_Experience_job_title)

correlation = pd.crosstab(df_2026['Experience_Level'], df_2026['Job_Title'])
correlation_name = correlation.reset_index()
print('\nCorrelation between Experience Level and Job Title in 2026:')
print(correlation_name)

country_job_title = pd.crosstab(df_2026['Country'], df_2026['Job_Title'])
country_job_title_flat = country_job_title.reset_index()
print('\nCorrelation between Country and Job Title in 2026:')
print(country_job_title_flat)

skill_impact = df_2026.groupby('Top_Skill')['Salary_USD'].mean().sort_values(ascending=False).reset_index()
print('\nImpact of Top Skills on Salary in 2026:')
print(skill_impact)

remote_impact = df_2026.groupby('Remote')['Salary_USD'].mean().sort_values(ascending=False).reset_index()
print('\nImpact of Remote Work on Salary in 2026:')
print(remote_impact)

company_profile = df_2026.groupby('Company_Type')['Salary_USD'].agg(['mean', 'std', 'count'])
print('\nCompany Profile by Type in 2026:')
company_profile.columns = ['Average_Salary', 'Salary_StdDev', 'Count']
company_profile = company_profile.reset_index()
print(company_profile)

comparative_analysis.to_csv('data/processed/comparative_analysis_2026.csv', index=False)
average_salary_by_experience.to_csv('data/processed/average_salary_by_experience_2026.csv', index=False)
comparative_Experience_job_title.to_csv('data/processed/comparative_experience_job_title_2026.csv', index=False)
correlation_name.to_csv('data/processed/correlation_experience_job_title_2026.csv', index=False)
country_job_title_flat.to_csv('data/processed/correlation_country_job_title_2026.csv', index=False)
skill_impact.to_csv('data/processed/skill_impact_2026.csv', index=False)
remote_impact.to_csv('data/processed/remote_impact_2026.csv', index=False)
company_profile.to_csv('data/processed/company_profile_2026.csv', index=False)
