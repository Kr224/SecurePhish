from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
from scipy.io import arff
from feature_extraction import extract_features

def build_and_train_model(X, y):
    # Ensure that y contains at least two unique classes
    if len(set(y)) < 2:
        raise ValueError("The target variable 'y' needs at least two classes to perform classification.")

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Initialize and train the Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f'Accuracy: {accuracy}')
    print(f'Classification Report:\n{report}')

    return model

if __name__ == "__main__":
    # Load the dataset
    data, meta = arff.loadarff('../Data/Training Dataset.arff')
    df = pd.DataFrame(data)

    # Extract features and target variable
    X_df = extract_features(df)
    y = df['Result'].astype(int)

    # Build and train the model
    model = build_and_train_model(X_df, y)
