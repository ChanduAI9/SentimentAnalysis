import openai
from preprocess import preprocess_text

# Set your OpenAI API key
openai.api_key = ''

def sentiment_analysis_openai(text):
    """
    Analyzes the sentiment of the input text using OpenAI GPT API (new interface).
    """
    # Preprocess the text
    text = preprocess_text(text)
    
    # Make API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant for sentiment analysis."},
            {"role": "user", "content": f"Analyze the sentiment of the following text: '{text}'"}
        ]
    )
    
    # Return response
    return response['choices'][0]['message']['content'].strip()

