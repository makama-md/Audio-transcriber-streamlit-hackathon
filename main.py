import streamlit as st
from google.cloud import translate_v2 as translate

# Set up the Google Cloud Translation client
translate_client = translate.Client()

# Streamlit app title
st.title("Simple Translation App")

# Input text for translation
text_to_translate = st.text_area("Enter text to translate:")

# Select the target language for translation
target_language = st.selectbox("Select target language:", ["English", "Spanish", "French"])

# Translate the input text when the user clicks the "Translate" button
if st.button("Translate"):
    if text_to_translate:
        # Map the target language name to its language code
        language_codes = {"English": "en", "Spanish": "es", "French": "fr"}
        target_language_code = language_codes.get(target_language, "en")

        # Perform the translation
        translation = translate_client.translate(text_to_translate, target_language=target_language_code)

        # Display the translated text
        st.write(f"Translated text ({target_language}):")
        st.write(translation["translatedText"])
    else:
        st.warning("Please enter text to translate.")

# About section
st.sidebar.header("About")
st.sidebar.markdown(
    "This is a simple Streamlit app for text translation using the Google Cloud Translation API."
)

# Optional: Provide a link to Google Cloud Translation API documentation or credentials setup guide
st.sidebar.markdown(
    "[Google Cloud Translation API Documentation](https://cloud.google.com/translate/docs)"
)
