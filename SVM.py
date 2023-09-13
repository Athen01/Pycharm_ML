import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_breast_cancer
from sklearn.inspection import DecisionBoundaryDisplay

# Read the data from an Excel sheet
data = pd.read_excel('/content/drive/MyDrive/svmdata.xlsx')

# Split the data into features (X) and labels (y)
X = data[['X1', 'X2']]
y = data['Label_column']  # Replace 'Label_column' with the actual name of your label column

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create an SVM classifier (you can choose the kernel and other hyperparameters)
clf = SVC(kernel='linear')

# Train the SVM classifier on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Plot Decision Boundary
DecisionBoundaryDisplay.from_estimator(
    clf,
    X.values,
    response_method="predict",
    cmap=plt.cm.Spectral,
    alpha=0.8,
    xlabel='X1',
    ylabel='X2',
)

# Scatter plot
plt.scatter(X['X1'], X['X2'], c=y, s=20, edgecolors="k")
plt.show()