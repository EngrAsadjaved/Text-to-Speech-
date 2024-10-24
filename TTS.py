# app.py
import streamlit as st
from TTS.api import TTS  # Make sure this import is correct

# Initialize the Tacotron2-DDC model
model_name = "tts_models/en/ljspeech/tacotron2-DDC"
tts = TTS(model_name)

# Streamlit app interface
st.title("Text-to-Speech with Tacotron2-DDC")
st.write("Convert text to speech using the Tacotron2-DDC model.")

# Input text from user
input_text = st.text_area("Enter the text you want to convert to speech:", "Hello, this is a test of the Tacotron2 DDC text-to-speech model.")

# Button to generate speech
if st.button("Generate Speech"):
    output_path = "output.wav"
    tts.tts_to_file(text=input_text, file_path=output_path)
    st.success("Speech generated successfully!")

    # Display the audio player
    audio_file = open(output_path, "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/wav")
