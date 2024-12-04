import pandas as pd
from sentiment_hf import sentiment_analysis_hf

def analyze_file(input_file, output_file):
    """
    Reads a CSV file, performs sentiment analysis on the 'Tweet' column,
    and saves the results to a new file.
    
    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the output file with sentiments.
    """
    df = pd.read_csv(input_file)
    
    if 'Tweet' not in df.columns:
        raise ValueError("The input file must contain a 'Tweet' column.")
    
    sentiments = []
    for tweet in df['Tweet']:
        result = sentiment_analysis_hf(tweet)
        sentiments.append(result['label']) 
    
    df['Sentiment'] = sentiments
    
    df.to_csv(output_file, index=False)
    print(f"Sentiment analysis complete. Results saved to {output_file}")
