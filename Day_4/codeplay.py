import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('csv_result-WISDM_ar_v1.csv', header=None, delimiter=',')

# Assign column names
num_features = df.shape[1] - 1
df.columns = [f'feature_{i}' for i in range(num_features)] + ['target']

# Check the DataFrame after column assignment
print("DataFrame columns:")
print(df.columns)
print("First few rows after column assignment:")
print(df.head())

# Separate features and target variable
X = df.drop('target', axis=1).values
y = df['target'].values

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")

# Perform train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")

# Initialize and fit classifiers
dt_classifier = DecisionTreeClassifier()
knn_classifier = KNeighborsClassifier()

# Fit the classifiers
dt_classifier.fit(X_train, y_train)
knn_classifier.fit(X_train, y_train)

# Predict
y_pred_dt = dt_classifier.predict(X_test)
y_pred_knn = knn_classifier.predict(X_test)

# Evaluate accuracy
print(f"Decision Tree Accuracy: {accuracy_score(y_test, y_pred_dt)}")
print(f"KNN Accuracy: {accuracy_score(y_test, y_pred_knn)}")
