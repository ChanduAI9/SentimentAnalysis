# SentimentAnalysis

Here's a sample `README.md` file for your **Sentiment Analysis Project**:

---

# **Sentiment Analysis Project**

This project performs sentiment analysis on text data using the **Hugging Face Transformers** library. It supports analyzing individual text samples as well as batch processing for text data in `.csv` files. The output includes sentiment labels (e.g., Positive, Negative, Neutral) and can be visualized using charts.

---

## **Features**

1. **Preprocessing**:
   - Cleans input text by removing URLs, special characters, and converting to lowercase.

2. **Sentiment Analysis**:
   - Uses Hugging Face's `distilbert-base-uncased-finetuned-sst-2-english` model for sentiment classification.

3. **Batch Processing**:
   - Supports analyzing sentiment for a file containing multiple text samples (e.g., tweets or reviews) in a column named **"Tweet"**.

4. **Visualization**:
   - Generates visual representations of sentiment distribution using pie charts and bar charts.

---

## **Project Structure**

```
sentiment_analysis_project/
├── main.py                # Entry point for the project
├── preprocess.py          # Preprocessing utility functions
├── sentiment_hf.py        # Hugging Face sentiment analysis code
├── batch_analysis.py      # Batch processing for file input
├── visualize.py           # Visualization functions for results
├── requirements.txt       # Required libraries for the project
└── README.md              # Instructions and project overview
```

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/ChanduAI9/SentimentAnalysis.git
cd sentiment_analysis_project
```

### **2. Install Dependencies**
Make sure Python 3.8+ is installed. Install the required libraries:
```bash
pip install -r requirements.txt
```

---

## **Usage**

### **1. Analyze Single Text**
Run the `main.py` script to analyze individual text samples:
```bash
python main.py
```
The script will prompt you to input a sentence, and the sentiment will be displayed.

---

### **2. Analyze Batch Data**
You can analyze a CSV file containing a column named **"Tweet"**:
```bash
python batch_analysis.py --input_file path/to/input.csv --output_file path/to/output.csv
```
- `--input_file`: Path to the input CSV file.
- `--output_file`: Path to save the output CSV file with added sentiment labels.

---

### **3. Visualize Sentiment Distribution**
Visualize the sentiment analysis results using `visualize.py`. You can use:
- A pie chart for sentiment distribution.
- A bar chart for sentiment counts.

```python
# Example in your script
from visualize import plot_pie_chart, plot_bar_chart

# Example usage after batch processing
plot_pie_chart(sentiment_results)
plot_bar_chart(sentiment_results)
```

---

## **Example Input and Output**

### **Input Text**
```plaintext
"I love this product! It's amazing!"
```

### **Output**
```plaintext
Sentiment: Positive
```

### **Input CSV**
| Tweet                              |
|------------------------------------|
| "I love this product!"             |
| "The service was terrible."        |
| "The food was okay, not great."    |

### **Output CSV**
| Tweet                              | Sentiment |
|------------------------------------|-----------|
| "I love this product!"             | Positive  |
| "The service was terrible."        | Negative  |
| "The food was okay, not great."    | Neutral   |

---

## **Dependencies**

- Python 3.8+
- `transformers`
- `torch`
- `pandas`
- `matplotlib`

Install them using:
```bash
pip install -r requirements.txt
```

---
