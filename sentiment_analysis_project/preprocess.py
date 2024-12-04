import re

def preprocess_text(text):
    """
    Preprocesses the input text by removing URLs, special characters, and extra spaces.
    Converts text to lowercase.
    """
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^A-Za-z0-9\s]', '', text)  # Remove special characters
    text = text.lower().strip()  # Convert to lowercase and strip whitespace
    return text
