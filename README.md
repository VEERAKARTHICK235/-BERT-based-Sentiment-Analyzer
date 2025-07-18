# BERT-based Sentiment Analyzer (with BERTweet)

This app uses Hugging Face's `bertweet-base-sentiment-analysis` model to predict sentiment on any sentence or word.

## 💻 How to Run

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
streamlit run app.py
```

3. Try sentences like:
- I am very happy today → 🙂 Positive
- This is so sad → 😠 Negative
- Just an average day → 😐 Neutral