import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

merged_data = pd.read_csv('datasets/MergedData.csv')

# Display basic information about the dataset
print("Dataset basic info:")
print(merged_data.info())
print("\nSummary Statistics:")
print(merged_data.describe())

# Data distribution plots
plt.figure(figsize=(12, 8))

# Distribution of Encounter Counts
plt.subplot(2, 2, 1)
sns.histplot(data=merged_data, x='encounters', bins=20, kde=True)
plt.title("Distribution of Encounter Counts")

# Distribution of Lab Result Counts
plt.subplot(2, 2, 2)
sns.histplot(data=merged_data, x='lab_results', bins=20, kde=True)
plt.title("Distribution of Lab Result Counts")

# Distribution of Procedure Counts
plt.subplot(2, 2, 3)
sns.histplot(data=merged_data, x='procedures', bins=20, kde=True)
plt.title("Distribution of Procedure Counts")

# Distribution of Vital Sign Counts
plt.subplot(2, 2, 4)
sns.histplot(data=merged_data, x='vital_signs', bins=20, kde=True)
plt.title("Distribution of Vital Sign Counts")

plt.tight_layout()
plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 6))
correlation_matrix = merged_data[['encounters', 'lab_results', 'procedures', 'vital_signs']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title("Correlation Heatmap")
plt.show()

# Compare 'encounters' and 'lab_results' using histograms
plt.figure(figsize=(12, 6))

# Histogram for 'encounters'
plt.subplot(1, 2, 1)
sns.histplot(data=merged_data, x='encounters', bins=20, kde=True, color='blue')
plt.title("Distribution of Encounter Counts")
plt.xlabel("Encounter Counts")

# Histogram for 'lab_results'
plt.subplot(1, 2, 2)
sns.histplot(data=merged_data, x='lab_results', bins=20, kde=True, color='green')
plt.title("Distribution of Lab Result Counts")
plt.xlabel("Lab Result Counts")

plt.tight_layout()
plt.show()

# Compare 'encounters' and 'lab_results' using box plots
plt.figure(figsize=(8, 6))

sns.boxplot(data=merged_data[['encounters', 'lab_results']], palette='Set3')
plt.title("Comparison of Encounter and Lab Result Counts")
plt.xlabel("Variable")
plt.ylabel("Counts")
plt.xticks(ticks=[0, 1], labels=['Encounters', 'Lab Results'])

plt.tight_layout()
plt.show()

# Histogram for 'procedures'
plt.subplot(2, 2, 2)
sns.histplot(data=merged_data, x='procedures', bins=20, kde=True, color='green')
plt.title("Distribution of Procedure Counts")
plt.xlabel("Procedure Counts")

plt.tight_layout()
plt.show()

# Compare 'encounters' and 'vital_signs' using histograms and box plots
plt.figure(figsize=(12, 12))

# Histogram for 'encounters'
plt.subplot(2, 2, 1)
sns.histplot(data=merged_data, x='encounters', bins=20, kde=True, color='blue')
plt.title("Distribution of Encounter Counts")
plt.xlabel("Encounter Counts")

# Histogram for 'vital_signs'
plt.subplot(2, 2, 2)
sns.histplot(data=merged_data, x='vital_signs', bins=20, kde=True, color='orange')
plt.title("Distribution of Vital Sign Counts")
plt.xlabel("Vital Sign Counts")

plt.tight_layout()
plt.show()

# Scatter plot comparing 'encounters' and 'procedures'
plt.figure(figsize=(12, 6))

# Scatter plot for 'encounters' vs 'procedures'
sns.scatterplot(data=merged_data, x='encounters', y='procedures', color='green')
plt.title("Scatter Plot: Encounters vs Procedures")
plt.xlabel("Encounter Counts")
plt.ylabel("Procedure Counts")

plt.tight_layout()
plt.show()

# Scatter plot comparing 'encounters' and 'vital_signs'
plt.figure(figsize=(12, 6))

# Scatter plot for 'encounters' vs 'vital_signs'
sns.scatterplot(data=merged_data, x='encounters', y='vital_signs', color='orange')
plt.title("Scatter Plot: Encounters vs Vital Signs")
plt.xlabel("Encounter Counts")
plt.ylabel("Vital Sign Counts")

plt.tight_layout()
plt.show()

# Scatter plot for 'encounters' vs 'lab_results'
sns.scatterplot(data=merged_data, x='encounters', y='lab_results', color='blue')
plt.title("Scatter Plot: Encounters vs Lab Results")
plt.xlabel("Encounter Counts")
plt.ylabel("Lab Result Counts")

plt.tight_layout()
plt.show()
