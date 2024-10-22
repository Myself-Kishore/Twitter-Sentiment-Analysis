import streamlit as st
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the pre-trained model
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

def preprocess_text(text):
    return vectorizer.transform([text])

def predict_sentiment(text):
    preprocessed_text = preprocess_text(text)
    prediction = model.predict(preprocessed_text)
    return prediction[0]

def main():
    st.title("Sentiment Analysis")
    st.markdown('<style>h2{color: #008000;}</style>', unsafe_allow_html=True)
    st.markdown('<style>p{color: #0000FF;}</style>', unsafe_allow_html=True)
    st.markdown('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.write("Enter a text of your post to determine if it's positive or negative..!!")

    # Get user input
    user_input = st.text_area("Enter text here:")

    if st.button("Analyze"):
        if user_input:
            prediction = predict_sentiment(user_input)
            st.write("### Sentiment:", prediction)
        else:
            st.write("Please enter some text to analyze.")

if __name__ == "__main__":
    main()
