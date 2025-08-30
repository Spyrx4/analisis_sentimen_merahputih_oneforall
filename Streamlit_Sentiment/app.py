import streamlit as st
import joblib
import pandas as pd

# --- Load model (pastikan tuple berisi (model, vectorizer, y))
model, vectorizer, y = joblib.load("model/sentiment_model_new.pkl")

# --- (Opsional) Load lexicon
positive_lexicon = set(pd.read_csv("data/positive.tsv", sep="\t", header=None)[0])
negative_lexicon = set(pd.read_csv("data/negative.tsv", sep="\t", header=None)[0])

# --- Fungsi prediksi
def predict_sentiment(text):
    text_vec = vectorizer.transform([text])   # gunakan vectorizer hasil load
    return model.predict(text_vec)[0]

# --- Streamlit UI
st.title("📝 Sentiment Analysis App")
st.write("Masukkan kalimat untuk diprediksi sentimennya.")

user_input = st.text_area("Tulis teks di sini...")

if st.button("Prediksi"):
    if user_input.strip() == "":
        st.warning("Tolong masukkan teks terlebih dahulu.")
    else:
        sentiment = predict_sentiment(user_input)
        if sentiment == "Positif":
            st.success(f"Hasil Prediksi: **{sentiment} 😀**")
        else:
            st.error(f"Hasil Prediksi: **{sentiment} 😡**")
