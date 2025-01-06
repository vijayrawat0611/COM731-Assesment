#!/usr/bin/env python
# coding: utf-8

# In[3]:


#to perform csv related operation details 
import csv




# main function of csv module
def demographic_info(user):
     
    #"lung_cancer_data (2).csv"
    file_name = input("Enter the file name ")

    # main interface of csv module
    print("press 1 for  demographic information:")
    print("press 2 for  medical history details ")
    print("press 3 for  treatment details ")
    print("press 4 for  Retrieve information from your chosen columns")
    # user response
    user =int(input("select from any of three "))
    #Demographic information
    if user == 1:
        try:
            with open(file_name,'r', newline='', encoding='utf-8')as file:
                reader = csv.DictReader(file)
                Patient_id = input("WHICH PATIENT DETAILS YOU WANT TO SEE")
                # Iterate through the rows in the file and match Patient_ID
                for row in reader:
                    if row['Patient_ID'] == Patient_id:
                        print(f"Demographics for patient {Patient_id}:")
                        print(f"  Age: {row['Age']}")
                        print(f"  Gender: {row['Gender']}")
                        print(f"  Smoking History: {row['Smoking_History']}")
        except Exception as e:
             # Handle any errors 
            print(f"An error occurred: {e}")   
            
    elif user == 2:
        try:
            # Prompt user for Ethnicity
            Ethnicity = input("WHICH Ethnicity DETAILS YOU WANT TO SEE")
            with open(file_name,'r',encoding='utf-8') as file_name:
                reader = csv.reader(file_name)
                headings = next(file_name)
                header = headings.split(',')
                # Print relevant column headers
                print(header[12], header[16],header[23])
                # Iterate through the rows and filter by Ethnicity
                for row in reader:
                    if row[9] == Ethnicity:
                        print(row[12],row[16],row[23])
        except Exception as e:
            # Handle any errors
            print(f"An error occurred: {e}")
    elif user == 3:
        survival_months = '100'
        try:
            file_name = "lung_cancer_data (2).csv"
            with open(file_name, 'r',encoding='utf-8') as file_name:
                reader = csv.reader(file_name) 
                headings = next(file_name)
                header = headings.split(',')
                print(header[2], header[5],header[6])
                # Iterate through the rows and filter by survival months
                for row in reader:
                    if row[2] > survival_months:
                        print(row[4],row[5],row[6])
        except Exception as e:
            print(f"An error occurred: {e}")
    elif user == 4:
        try:
            Smoking_History = "Never Smoked"
            file_name = "lung_cancer_data (2).csv"
            with open(file_name, 'r',encoding='utf-8') as file_name:
                reader = csv.reader(file_name) 
                headings = next(file_name)
                header = headings.split(',')
                print(header[4], header[22],header[24])
                # Iterate through the rows and filter by Smoking History
                for row in reader:
                    if row[3] ==  Smoking_History:
                        print(row[4],row[22],row[24])
        except Exception as e:
            print(f"An error occurred: {e}")













# In[ ]:




