import streamlit as st
from transformers import pipeline

# Load the image captioning model
get_completion = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

# Streamlit app
st.title("Image Captioning App")

# Upload image
image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if image:
    # Display the uploaded image
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Generate caption button
    if st.button("Generate Caption"):
        # Generate caption using the image-to-text pipeline
        caption = get_completion(image.read())
        
        # Display the generated caption
        st.success("Generated Caption: " + caption[0]['generated_text'])
