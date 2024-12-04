import matplotlib.pyplot as plt

def plot_pie_chart(results):
    """
    Plots a pie chart of sentiment distribution.
    """
    labels = ['Positive', 'Negative', 'Neutral']
    counts = [results.count('POSITIVE'), results.count('NEGATIVE'), results.count('NEUTRAL')]
    
    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=labels, autopct='%1.1f%%', colors=['green', 'red', 'blue'])
    plt.title('Sentiment Distribution')
    plt.show()

def plot_bar_chart(results):
    """
    Plots a bar chart of sentiment distribution.
    """
    labels = ['Positive', 'Negative', 'Neutral']
    counts = [results.count('POSITIVE'), results.count('NEGATIVE'), results.count('NEUTRAL')]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, counts, color=['green', 'red', 'blue'])
    plt.title('Sentiment Distribution')
    plt.ylabel('Count')
    plt.xlabel('Sentiment')
    plt.show()
