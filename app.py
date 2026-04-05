import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image
import os

# 1. Page Configuration
st.set_page_config(page_title="Neural Style Transfer", page_icon="🎨", layout="centered")

st.title("🎨 Neural Style Transfer")
st.write("Apply the artistic style of one image (e.g., a painting) to the content of another image (e.g., a photo) using Deep Learning!")

# 2. Load Pre-trained Model from TensorFlow Hub
# We use @st.cache_resource so the model loads only once
@st.cache_resource
def load_model():
    # This is a fast, pre-trained model for arbitrary image stylization
    model_url = 'https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2'
    return hub.load(model_url)

model = load_model()

# 3. Helper Functions mapped to tf/numpy operations
def preprocess_image(image, target_size=None):
    """Converts a PIL Image to a normalized tensor suitable for the TF model."""
    img = np.array(image.convert('RGB'))
    img = tf.convert_to_tensor(img, dtype=tf.float32)[tf.newaxis, ...] / 255.
    if target_size:
        img = tf.image.resize(img, target_size, preserve_aspect_ratio=True)
    return img

def tensor_to_image(tensor):
    """Converts a tensor back to a displayable PIL image."""
    tensor = tensor * 255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor) > 3:
        tensor = tensor[0]
    return Image.fromarray(tensor)

# 4. User Interface setup using Streamlit columns
col1, col2 = st.columns(2)

def get_image_from_source(title, dataset_folder):
    options = ["Upload your own"]
    dataset_images = []
    
    if os.path.exists(dataset_folder):
        dataset_images = [f for f in os.listdir(dataset_folder) if f.endswith(('jpg', 'jpeg', 'png'))]
        options.extend(dataset_images)
        
    choice = st.selectbox(f"Choose {title}", options)
    
    if choice == "Upload your own":
        file = st.file_uploader(f"Or upload {title}", type=['jpg', 'jpeg', 'png'])
        if file:
            return Image.open(file)
    else:
        img_path = os.path.join(dataset_folder, choice)
        return Image.open(img_path)
    return None

with col1:
    content_image = get_image_from_source("Content Image", "datasets/content_images")
    if content_image:
        st.image(content_image, caption="Content Image", use_container_width=True)

with col2:
    style_image = get_image_from_source("Style Image", "datasets/style_images")
    if style_image:
        st.image(style_image, caption="Style Image", use_container_width=True)

# 5. Perform the Style Transfer
if content_image and style_image:
    st.write("---")
    if st.button("Generate Art 🌟", use_container_width=True):
        with st.spinner("Applying style... This may take a few seconds."):
            try:
                # Preprocess both images
                content_tensor = preprocess_image(content_image)
                # The model is optimized for 256x256 style images
                style_tensor = preprocess_image(style_image, target_size=(256, 256))
                
                # Apply style transfer using the TF Hub model
                stylized_tensor = model(tf.constant(content_tensor), tf.constant(style_tensor))[0]
                
                # Convert result back to image and display
                result_image = tensor_to_image(stylized_tensor)
                
                st.success("Style transfer complete!")
                st.image(result_image, caption="Stylized Output", use_container_width=True)
                
                st.balloons()
            except Exception as e:
                st.error(f"An error occurred: {e}")
