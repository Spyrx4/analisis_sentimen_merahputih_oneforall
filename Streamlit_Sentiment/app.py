import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# --- Load model (pastikan tuple berisi (model, vectorizer, y))
model, vectorizer, y = joblib.load("model/sentiment_model_new.pkl")

# --- Load dataset hasil preprocessing (untuk wordcloud)
data = pd.read_csv("data/Hasil_new.csv")  # ganti sesuai nama file hasil preprocessing

# --- Fungsi prediksi
def predict_sentiment(text):
    text_vec = vectorizer.transform([text])   # gunakan vectorizer hasil load
    return model.predict(text_vec)[0]

# --- Sidebar menu
st.sidebar.title("📌 Menu")
menu = st.sidebar.radio(
    "Pilih halaman:",
    ("Prediksi Sentimen", "Wordcloud")
)

# --- Halaman Prediksi
if menu == "Prediksi Sentimen":
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

# --- Halaman Wordcloud
elif menu == "Wordcloud":
    st.title("☁️ Wordcloud Visualisasi")

    option = st.radio("Pilih kategori:", ("Semua", "Positif", "Negatif"))

    if option == "Semua":
        text = " ".join(data['stemming'].astype(str))
    elif option == "Positif":
        text = " ".join(data[data['sentiment']=="Positif"]['stemming'].astype(str))
    else:
        text = " ".join(data[data['sentiment']=="Negatif"]['stemming'].astype(str))

    # Generate wordcloud dengan stopwords
    stopwords = set(STOPWORDS)
    wc = WordCloud(
        width=800,
        height=400,
        background_color="white",
        stopwords=stopwords,
        max_words=200
    ).generate(text)

    # Tampilkan
    fig, ax = plt.subplots(figsize=(10,5))
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

