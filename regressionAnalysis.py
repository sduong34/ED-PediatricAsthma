import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

merged_data = pd.read_csv('datasets/MergedData.csv')

# Define independent variables and the dependent variable 
independent_vars = ['lab_results', 'procedures', 'vital_signs']
dependent_var = 'encounters'  

# Split the data into features (X) and target (y)
X = merged_data[independent_vars]
y = merged_data[dependent_var]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

# Display regression results
print("Regression Coefficients:")
for var, coef in zip(independent_vars, model.coef_):
    print(f"{var}: {coef:.4f}")
print(f"Intercept: {model.intercept_:.4f}")

print("\nRoot Mean Squared Error (RMSE):", rmse)
print("R-squared:", r2) 