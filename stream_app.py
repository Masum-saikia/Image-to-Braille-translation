import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import numpy as np

# Initialize the BLIP model and processor with caching
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large", cache_dir="./model_cache")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large", cache_dir="./model_cache")

# Braille Unicode Code Points for the letters a-z and space
braille_dict = {
    'a': '\u2801', 'b': '\u2803', 'c': '\u2809', 'd': '\u2819',
    'e': '\u2805', 'f': '\u280b', 'g': '\u281b', 'h': '\u2813',
    'i': '\u280a', 'j': '\u281a', 'k': '\u280c', 'l': '\u281c',
    'm': '\u280e', 'n': '\u281e', 'o': '\u280f', 'p': '\u281d',
    'q': '\u281f', 'r': '\u2817', 's': '\u280d', 't': '\u281d',
    'u': '\u2820', 'v': '\u2823', 'w': '\u283a', 'x': '\u2829',
    'y': '\u282b', 'z': '\u282a', ' ': ' '
}

def text_to_braille(text):
    braille_text = ''
    for char in text.lower():
        if char in braille_dict:
            braille_text += braille_dict[char]
        else:
            braille_text += ' '  # For characters not in the dictionary
    return braille_text

st.title("Image Captioning with Braille Output")

# Capture image from camera
uploaded_image = st.camera_input("Camera: ")

if uploaded_image:
    # Convert the uploaded image to PIL format
    image = Image.open(uploaded_image)

    # Preprocess the image and generate caption
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    st.write(f"Caption: {caption}")

    # Convert caption to Braille
    braille_output = text_to_braille(caption)
    st.write(f"Braille: {braille_output}")
else:
    st.write("No image captured.")

