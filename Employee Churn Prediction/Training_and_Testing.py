'''
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("HR-Employee-Attrition-Updated_1.csv")

# Define the feature set (X) and target (y)
X = df.drop(columns=['Attrition_Binary'])  # Exclude the target column from the features
y = df['Attrition_Binary']  # Target column

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print the shapes to confirm the split
print("Training set:", X_train.shape, y_train.shape)
print("Testing set:", X_test.shape, y_test.shape)

# Step 1: Train the Logistic Regression model

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Initialize the Logistic Regression model
model = LogisticRegression(max_iter=100000, solver='saga')

# Train the model on the training data
model.fit(X_train, y_train)

# Step 2: Make predictions on the test data

# Make predictions on the test data
y_pred = model.predict(X_test)

# Step 3: Evaluate the model
# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)

# Generate the confusion matrix to see how the model performed
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
'''

'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the dataset
df = pd.read_csv("HR-Employee-Attrition-Updated_1.csv")

# Define the feature set (X) and target (y)
X = df.drop(columns=['Attrition_Binary'])  # Exclude the target column from the features
y = df['Attrition_Binary']  # Target column

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print the shapes to confirm the split
print("Training set:", X_train.shape, y_train.shape)
print("Testing set:", X_test.shape, y_test.shape)

# Step 1: Feature scaling for better convergence
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 2: Train the Logistic Regression model with class weighting for imbalance
model = LogisticRegression(max_iter=70000, solver='saga', class_weight='balanced')

# Train the model on the scaled training data
model.fit(X_train_scaled, y_train)

# Step 3: Make predictions on the test data
y_pred = model.predict(X_test_scaled)

# Step 4: Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)

# Generate the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Output the results
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv("HR-Employee-Attrition-Updated_1.csv")

# Define the feature set (X) and target (y)
X = df.drop(columns=['Attrition_Binary'])  # Exclude the target column from the features
y = df['Attrition_Binary']  # Target column

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling for better convergence
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Apply SMOTE for balancing the classes
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train_scaled, y_train)

# Train the RandomForest model
model = RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=42)
model.fit(X_train_resampled, y_train_resampled)

# Make probability predictions on the test data
y_prob = model.predict_proba(X_test_scaled)[:, 1]  # Probabilities for the positive class

# Adjust the threshold (example: lowering threshold to 0.3 for class 1)
y_pred_adjusted = (y_prob >= 0.3).astype(int)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred_adjusted)

# Generate the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred_adjusted)

# Output the results
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(classification_report(y_test, y_pred_adjusted))
import joblib

# Save the model
joblib.dump(model, 'random_forest_model.pkl')

# Save the scaler
joblib.dump(scaler, 'scaler.pkl')



'''
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load the dataset
df = pd.read_csv("HR-Employee-Attrition-Updated_1.csv")

# Define the feature set (X) and target (y)
X = df.drop(columns=['Attrition_Binary'])  # Exclude the target column from the features
y = df['Attrition_Binary']  # Target column

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling for better convergence
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Apply SMOTE for balancing the classes
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train_scaled, y_train)

# Hyperparameter Tuning using GridSearchCV
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10],
    'class_weight': ['balanced', None]
}

grid_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42),
                           param_grid=param_grid,
                           cv=5,
                           n_jobs=-1,
                           verbose=2,
                           scoring='accuracy')
grid_search.fit(X_train_resampled, y_train_resampled)

# Best parameters from GridSearchCV
best_params = grid_search.best_params_
print(f"Best Parameters from GridSearchCV: {best_params}")

# Train the RandomForest model with the best parameters
model = RandomForestClassifier(n_estimators=best_params['n_estimators'],
                               max_depth=best_params['max_depth'],
                               min_samples_split=best_params['min_samples_split'],
                               class_weight=best_params['class_weight'],
                               random_state=42)
model.fit(X_train_resampled, y_train_resampled)

# Make predictions on the test data
y_pred = model.predict(X_test_scaled)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)

# Generate the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Evaluate additional metrics
roc_auc = roc_auc_score(y_test, model.predict_proba(X_test_scaled)[:, 1])

# Output the results
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(classification_report(y_test, y_pred))
print(f"ROC-AUC Score: {roc_auc}")
'''