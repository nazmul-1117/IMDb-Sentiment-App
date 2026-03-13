# app.py
import streamlit as st
import joblib
import numpy as np
import pandas as pd
import re

# ------------------------------
# Streamlit UI
# ------------------------------
st.set_page_config(
    page_title="IMDb Sentiment App",
    page_icon="🎬",
    layout="centered"
)


# ------------------------------
# Preprocessing functions (must be defined BEFORE loading the pipeline)
# ------------------------------
def preprocess_text(text):
    """Clean a single text review."""
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Convert to lowercase
    text = text.lower()
    # Handle negations
    text = re.sub(r"\bcan't\b", "cannot", text)
    text = re.sub(r"\bn't\b", " not", text)
    # Remove punctuation and numbers
    text = re.sub(r'[^a-z\s]', '', text)
    # Reduce repeated letters (loooove -> love)
    text = re.sub(r'(.)\1{2,}', r'\1', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_text_series(x: pd.Series):
    """Apply preprocessing to a pandas Series."""
    return x.apply(preprocess_text)

# ------------------------------
# Load the pipeline
# ------------------------------
@st.cache_data
def load_pipeline():
    """Load the saved Naive Bayes pipeline."""
    pipeline = joblib.load("model/naive_bayes_model_pipeline.joblib")
    return pipeline

pipeline = load_pipeline()


# Header
st.markdown(
    """
    <h1 style='text-align: center; color: #4B0082;'>IMDb Sentiment Analysis 🎬</h1>
    <p style='text-align: center; color: #555;'>Predict Positive or Negative Movie Reviews Instantly</p>
    """, unsafe_allow_html=True
)

st.write("---")

# Sidebar instructions
st.sidebar.header("How to Use This App")
st.sidebar.info(
    """
1. Enter or paste a movie review in the box below.  
2. Click **Predict Sentiment** to see if it's positive or negative.  
3. Optionally, try a sample review by checking the box.  
"""
)

# Text input
user_input = st.text_area("Enter your movie review here:", height=150)

# Sample review option
if st.checkbox("Use a Sample Review"):
    sample_reviews = [
        "I absolutely loved this movie! The acting and story were phenomenal.",
        "This film was a complete disaster. Waste of time.",
        "An enjoyable experience with heartwarming moments and great visuals.",
        "Boring plot and bad acting. I want my time back."
    ]
    user_input = np.random.choice(sample_reviews)
    st.info(f"Sample review selected: {user_input}")

# Predict button
if st.button("Predict Sentiment"):
    if not user_input.strip():
        st.warning("Please enter a review to predict sentiment.")
    else:
        input_series = pd.Series([user_input])
        prediction = pipeline.predict(input_series)[0]
        prediction_proba = pipeline.predict_proba(input_series)[0].max()
        
        st.subheader("Prediction Result:")
        if prediction.lower() == "positive":
            st.success(f"✅ Sentiment: **{prediction}**")
        else:
            st.error(f"❌ Sentiment: **{prediction}**")
        
        st.info(f"Confidence Score: {prediction_proba:.2f}")

# Footer / Author dedication
st.markdown("---")
st.markdown(
    """
    <p style='text-align: center; font-size: 0.9em; color: #888;'>
    Developed with ❤️ by Your Name | Dedicated to all movie lovers 🎥  
    <a href='https://github.com/nazmul-1117/IMDb-Sentiment-App' target='_blank'>GitHub Repo</a>
    </p>
    """, unsafe_allow_html=True
)