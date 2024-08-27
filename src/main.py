import pandas as pd
from scipy.io import arff
from data_preprocessing import preprocess_data

# Path to ARFF file
datasetPath = '/Users/karishnigupta/PycharmProjects/SecurePhish/Data/Training Dataset.arff'

# Load ARFF file
data, meta = arff.loadarff(datasetPath)

# Convert to pandas DataFrame
df = pd.DataFrame(data)

# Call data processing function
df_processed = preprocess_data(df)

print(df_processed.head())
