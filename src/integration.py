import os

import pandas as pd
from scipy.io import arff
from fpdf import FPDF
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

from src.code_analysis import analyze_code
from src.data_preprocessing import preprocess_data
from src.feature_extraction import extract_features
from src.model_building import build_and_train_model

def save_report(accuracy, report, issues):
    # Create PDF Report
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Phishing Detection and Code Analysis Report', ln=True, align='C')

    # Accuracy and Classification Report
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Model Accuracy and Classification Report', ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, f'Accuracy: {accuracy}\n\nClassification Report:\n{report}')

    # Security Issues
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Security Issues Detected', ln=True)
    pdf.set_font('Arial', '', 12)
    issues_text = '\n'.join(issues)
    pdf.multi_cell(0, 10, issues_text)

    # Save PDF
    pdf_file = 'report.pdf'
    pdf.output(pdf_file)
    print(f'Report saved as {pdf_file}')

def plot_model_performance(y_test, y_pred):
    # Plot confusion matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
                xticklabels=['Legitimate', 'Phishing'],
                yticklabels=['Legitimate', 'Phishing'])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.savefig('confusion_matrix.png')
    plt.close()
    print('Confusion matrix saved as confusion_matrix.png')

def main():
    # Load and preprocess data
    data, meta = arff.loadarff('../Data/Training Dataset.arff')
    df = pd.DataFrame(data)
    df_processed = preprocess_data(df)

    # Extract features and build model
    X_df = extract_features(df_processed)
    y = df_processed['Result']
    model = build_and_train_model(X_df, y)

    # Make predictions for performance visualization
    X_train, X_test, y_train, y_test = train_test_split(X_df, y, test_size=0.3, random_state=42)
    y_pred = model.predict(X_test)

    # Plot and save model performance
    plot_model_performance(y_test, y_pred)

    # Example code analysis
    file_path = 'example.html'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
            issues = analyze_code(content)
    else:
        issues = ['File not found. Skipping code analysis.']

    # Save report
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    save_report(accuracy, report, issues)

if __name__ == '__main__':
    main()