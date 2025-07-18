from transformers import pipeline

# Load Hugging Face pipeline with BERTweet model
sentiment_pipe = pipeline(
    "sentiment-analysis",
    model="finiteautomata/bertweet-base-sentiment-analysis"
)

def predict_sentiment(text: str) -> dict:
    result = sentiment_pipe(text[:512])[0]
    return result