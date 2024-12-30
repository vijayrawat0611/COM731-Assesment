#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

file_name = 'lung_cancer_data (2).csv'
grade_df = pd.read_csv(file_name)
def dataframe():
    
    print("press 1 for  top 3 treatments for a certain ethnicity")
    print("press 2 for   average white blood cell counts for certain treatments")
    print("press 3 for   smoking packs for patients in each treatment group")
    print("press 4 for   smoking packs for patients in each treatment group")
    response = int(input("select from any of three "))
    if response == 1:
       
        row = grade_df.loc[(grade_df.Survival_Months > 100) | (grade_df.Ethnicity == 'Asian'),['Treatment',]]
        transaction_weekday = row['Treatment'].value_counts(ascending= False)
        print(transaction_weekday[:3])

    elif response == 2:
        averageg_price = grade_df.groupby(['Ethnicity','Treatment']).White_Blood_Cell_Count.mean()
        print(f" the mean price {averageg_price}")
        
    elif response == 3:
        data=grade_df.loc[(grade_df.Blood_Pressure_Pulse > 90 ) & (grade_df.Tumor_Size_mm < 15),:]
        row = grade_df.groupby(['Treatment','Tumor_Location']).Smoking_Pack_Years.mean()
        print(row)

    elif response == 4:
         data=grade_df.loc[(grade_df.White_Blood_Cell_Count  > 9 ),:]
         row=grade_df.groupby(['Smoking_History','Stage']).Survival_Months.mean()
         print(row)
        




# In[ ]:




