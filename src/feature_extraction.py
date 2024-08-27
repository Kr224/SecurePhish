import pandas as pd
from scipy.io import arff

def extract_features(df):
    # In this case, features are already present in the DataFrame
    X_df = df.drop(columns=['Result'])
    return X_df


if __name__ == "__main__":
    # Load the dataset
    data, meta = arff.loadarff('../Data/Training Dataset.arff')
    df = pd.DataFrame(data)

    # Extract features
    X_df = extract_features(df)

    # Display the extracted features
    print(X_df.head())
