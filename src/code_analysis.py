import re

def analyze_code(file_content):
    vulnerabilities = []

    # Example checks (extend with more complex checks)
    if re.search(r'eval\(', file_content):
        vulnerabilities.append("Use of 'eval' detected, which can lead to code injection vulnerabilities.")

    if re.search(r'<script>', file_content, re.IGNORECASE):
        vulnerabilities.append("Inline JavaScript detected. Consider moving scripts to external files.")

    # Improved detection for hard-coded credentials
    if re.search(r'password\s*=\s*[\'"]\w+[\'"]', file_content, re.IGNORECASE) or re.search(
            r'api[_-]?key\s*=\s*[\'"]\w+[\'"]', file_content, re.IGNORECASE):
        vulnerabilities.append("Hard-coded credentials detected. Avoid storing sensitive data in the code.")

    print("Analyzed Code Content:")
    print(file_content)

    print("Detected Vulnerabilities:")
    for issue in vulnerabilities:
        print(f"- {issue}")

    return vulnerabilities
