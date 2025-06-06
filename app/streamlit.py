import streamlit as st
import joblib
from scipy.sparse import hstack


model = joblib.load('../data/logisticmodel.pkl')
tfidf = joblib.load('../data/tfidf_vectorizer.pkl')  
encoder = joblib.load('../data/airline_encoder.pkl')  
y_encoder = joblib.load('../data/label_encoder.pkl')  

st.title("Twitter US Airline Sentiment Predictor")
st.markdown("""Enter a tweet and choose airline to predict the tweet's sentiment.""")

tweet = st.text_area("Your Tweet")
airline = st.selectbox("Select Airline", ['United', 'American', 'Delta', 'Southwest', 'US Airways', 'Virgin America'])

if st.button("Predict Sentiment"):
    if tweet.strip() == "":
        st.warning("Please enter a tweet")
    else:
        tweet_vector = tfidf.transform([tweet])
        airline_vector = encoder.transform([[airline]])
        final_input = hstack((tweet_vector, airline_vector))

        prediction = model.predict(final_input)
        predicted_sentiment = y_encoder.inverse_transform(prediction)[0]

        st.success(f"Predicted Sentiment: **{predicted_sentiment.upper()}**")
