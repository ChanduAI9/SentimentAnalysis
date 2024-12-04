from transformers import pipeline
from preprocess import preprocess_text

def sentiment_analysis_hf(text):
    """
    Analyzes the sentiment of the input text using Hugging Face's sentiment-analysis pipeline.
    """
    text = preprocess_text(text)
    
    classifier = pipeline(
        'sentiment-analysis',
        model='distilbert-base-uncased-finetuned-sst-2-english',
        revision='714eb0f'
    )
    
    result = classifier(text)
    return result[0]
