#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import matplotlib to show diagram
import matplotlib.pyplot as plt
import numpy as np
#Import pandas 
import pandas as pd
#use datafram to save the file
file_name ='lung_cancer_data (2).csv'
grade_df = pd.read_csv(file_name,encoding='utf-8')

#User input to Get Ethnicty
def visualization():
    print("Welcome to Assesment 2 ")
    print(" press 1  Identify the top 3 treatments for a certain ethnicity")
    print("press 2   Analyse the average white blood cell counts for certain treatments")
    print("press 3    Analyse the average number of smoking packs for patients ")
    print("press 4    Analyse the data to derive meaningful insights based on your unique selectionn")
    user = int(input("Which details you want to see"))
    if user == 1:
        #use variable to match with data of Ethnicity column
       ethincity = input("Enter the ethnicity")
 
       row = grade_df.loc[(grade_df.Ethnicity == ethincity),['Treatment',]]
       group_treatment = row.groupby('Treatment')
       treatment_type = group_treatment.get_group("Radiation Therapy")
       group_treatment.size()
       sorted_treatment_group_type = group_treatment.size().sort_values(ascending=False)
       print(type(sorted_treatment_group_type))
       top_treatment = sorted_treatment_group_type.head()
        # storing data into a list
       treatment_list = top_treatment.index.tolist()
        # storing data count of treatment
       number_treatment_list = top_treatment.tolist()
        #create a figure
       fig = plt.figure(figsize=(12,6))
        #plot a pie chart
       plt.pie(number_treatment_list,labels=treatment_list)
        #set a label and legend
       plt.title(" Cancer Treatments")
       plt.legend(loc='upper right',bbox_to_anchor=(1.9,1))
       plt.show()

    elif user == 2:
        grouped_data = grade_df.groupby(['Ethnicity', 'Stage'])['Smoking_Pack_Years'].mean().reset_index()
        plt.figure(figsize=(10, 6))
        
        
        for ethnicity in grouped_data['Ethnicity'].unique():
            subset = grouped_data[grouped_data['Ethnicity'] == ethnicity]
            plt.plot(subset['Stage'], subset['Smoking_Pack_Years'], marker='o', label=ethnicity)
            
       
        plt.xlabel('Cancer Stage')
        plt.ylabel('Average Smoking Packs Consumption')
        plt.title('Trend of Average Smoking Packs Consumption Across Cancer Stages by Ethnicity')
        plt.legend()
        plt.grid(True)
        plt.show()




   
    elif user == 3:
         movie_released_year = grade_df.groupby('Treatment')[['Blood_Pressure_Systolic','Blood_Pressure_Diastolic']].mean()
         years = movie_released_year.index.tolist()
         avg_budget = movie_released_year['Blood_Pressure_Systolic'].tolist()
         avg_gross = movie_released_year['Blood_Pressure_Diastolic'].tolist()

         #create a figure
         fig = plt.figure(figsize=(15,10))

         # create the x-axis values
         x_axis = np.arange(len(years))

         #plot bar chart of movie's budget
         plt.bar(x_axis-0.2,avg_gross, width=0.4, label = 'avg_gross')

         #plot bar chart of movie's gross
         plt.bar(x_axis+0.2,avg_budget, width=0.4, label = 'avg_budget')

         # label the x-axis with the rotation
         plt.xticks(x_axis,years,rotation=90)

         # create a label for x-axis and y-axis
         plt.xlabel("Movies")
         plt.ylabel("Amount in Millions")

         # create a title for your graph
         plt.title("The budget and gross revenue of the top 5 movies with the most Facebook likes")

         # create a legend for labeled plot elements
         plt.legend()

         plt.show() # show the
    elif user == 4:
        # Group data by 'Gender' and 'Stage' and count occurrences
        grouped_data = grade_df.groupby(['Gender', 'Stage'])['Patient_ID'].count().reset_index()
        # Correct the column renaming: 'Patient_ID' to 'Patient Count'
        grouped_data = grouped_data.rename(columns={'Patient_ID': 'Patient Count'})  
# Create the visualization
        plt.figure(figsize=(10, 6))

# Define colors for each gender
# Updated colors dictionary to use 'Male' and 'Female' as keys
        colors = {'Male': 'skyblue', 'Female': 'salmon'}
# Plot the data for each gender
        for gender, group in grouped_data.groupby('Gender'):
            plt.scatter(group['Stage'], group['Patient Count'], label=gender, color=colors[gender], s=100, marker='o', edgecolor='black') # Increased marker size
            
        plt.title('Patient Count by Cancer Stage and Gender')
        plt.xlabel('Cancer Stage')
        plt.ylabel('Patient Count')
        plt.xticks(rotation=45) # Rotate x-axis labels for better readability
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7) # Added grid with a different linestyle and alpha
        plt.tight_layout()
        plt.show()



# In[ ]:





# In[ ]:





# In[ ]:




