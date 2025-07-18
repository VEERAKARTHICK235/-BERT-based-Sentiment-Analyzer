import streamlit as st
from utils.transformer_sentiment import predict_sentiment

st.set_page_config(page_title="BERT Sentiment Analyzer", page_icon="💡")
st.title("🤖 BERT-based Sentiment Analyzer")
st.markdown("### Enter your text below to detect sentiment:")

user_input = st.text_area("Input Text", "")

if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Please enter some text.")
    else:
        result = predict_sentiment(user_input)
        label = result['label']
        score = result['score']

        if label == "POS":
            st.success(f"🙂 Positive Sentiment — Confidence: {score:.2f}")
        elif label == "NEG":
            st.error(f"😠 Negative Sentiment — Confidence: {score:.2f}")
        else:
            st.info(f"😐 Neutral Sentiment — Confidence: {score:.2f}")