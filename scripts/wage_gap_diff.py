import pandas as pd

""" 
This script takes the cleaned table male_female and rewrite data into a new table wage_gap_worldwide.xlsx.
Also counts differences in male and female wages in local currency and calculates this difference in percentages.

Differences are counted as: male_wage - female_wage.
Differences in percentage are counted as: ((male_wage-female_wage) / female_wage)
"""

df = pd.read_excel('average_monthly_earnings_by_sex_and_occupation_male_female.xlsx')
new_df = pd.DataFrame(columns=['Country', 'Occupation', 'Year', 'Difference in local currency', 'Difference in % of local currency'])
rows_num = 17313  # number of rows in average_monthly_earnings_by_sex_and_occupation_male_female.xlsx table

for i in range(rows_num):  # iterate over all rows in df 
    row_sex_m = df['Sex'][i]
    row_occupation_m = df['Occupation'][i]
    
    if (row_sex_m == 'Female'):
        continue
    
    k = 1
    tmp_sex = df['Sex'][i+k]
    tmp_occupation = df['Occupation'][i+k]
    
    if (row_occupation_m == 0):
        continue
    
    while (tmp_sex != 'Female' or tmp_occupation != row_occupation_m):
        k += 1
        
        if (k+i >= rows_num): # we reach the end of the table
            break
        
        tmp_sex = df['Sex'][i+k]
        tmp_occupation = df['Occupation'][i+k]
        
        if (tmp_sex != 'Male' and tmp_occupation[0] != 'T' and tmp_occupation[0] != 'X' and tmp_occupation[0] > row_occupation_m[0]):
            break
    
    if (k+i >= rows_num): # we reach the end of the table
            break
    
    if (df['Local currency'][i+k] == 0):
        continue 
    
    if (tmp_sex != 'Male' and tmp_occupation[0] != 'T' and tmp_occupation[0] != 'X' and tmp_occupation[0] > row_occupation_m[0]):
            continue
    
    diff_usd = df['Local currency'][i] - df['Local currency'][i+k]
    
    diff_perc = (diff_usd / df['Local currency'][i+k])
    
    new_df.loc[len(new_df.index)] = [df['Country'][i], df['Occupation'][i], df['Time'][i], diff_usd, diff_perc]
    
new_df.to_excel('wage_gap_worldwide.xlsx')
