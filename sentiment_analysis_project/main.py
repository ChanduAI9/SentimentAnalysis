from batch_analysis import analyze_file
import sys

def main():
    print("Welcome to the Sentiment Analysis Tool!")
    print("Options:")
    print("1. Analyze a single text input")
    print("2. Analyze a file containing tweets (CSV)")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        text = input("Enter text to analyze: ")
        from sentiment_hf import sentiment_analysis_hf
        result = sentiment_analysis_hf(text)
        print(f"Sentiment: {result['label']}, Confidence: {result['score']:.2f}")
    elif choice == '2':
        input_file = input("Enter the path to the input CSV file: ")
        output_file = input("Enter the path to save the output CSV file: ")
        try:
            analyze_file(input_file, output_file)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
