import nltk

# Ensure required NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_data(df):
    # Check and decode bytes only where necessary
    df = df.apply(lambda col: col.map(lambda x: x.decode('utf-8') if isinstance(x, bytes) else x))

    # Convert columns to appropriate data types
    df = df.astype(int)  # Assuming all your data is integer-based

    return df
