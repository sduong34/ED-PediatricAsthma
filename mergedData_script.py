import pandas as pd 
import random

patient = pd.read_csv('patient.csv')
encounter = pd.read_csv('encounter.csv')
lab_result = pd.read_csv('lab_result.csv')
procedure = pd.read_csv('procedure.csv')
vital_signs = pd.read_csv('vitals_signs.csv')

#returns counts of each (encounters, lab results, procedures, vital signs) for each patient in patient.csv
def get_data_counts(data_frame, patient_id):
    encounter_count = len(encounter[encounter['patient_id'] == patient_id])
    lab_result_count = len(lab_result[lab_result['patient_id'] == patient_id])
    procedure_count = len(procedure[procedure['patient_id'] == patient_id])  
    vital_signs_count = len(vital_signs[vital_signs['patient_id'] == patient_id])  
    return encounter_count, lab_result_count, procedure_count, vital_signs_count

merged_data = []

#iterate through each patient and calculate counts
for patient_id in patient['patient_id']:
    encounter_count, lab_result_count, lab_procedure_count, vital_signs_count = get_data_counts(encounter, patient_id)
    merged_data.append([patient_id, encounter_count, lab_result_count, lab_procedure_count, vital_signs_count])

#create new dataframe with columns for each number
merged_df = pd.DataFrame(merged_data, columns=['patient_id', 'encounters', 'lab_results', 'procedures', 'vital_signs'])

#print the df to check its contents
print(merged_df)

#save the merged df to a new CSV file
merged_df.to_csv('datasets/MergedData.csv', index=False)

#since it takes a while, print message when completed
print("MergedData.csv created successfully")