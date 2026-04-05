# 🎨 Neural Style Transfer 

A simple, beginner-friendly web application built with Python and Streamlit. This app applies the artistic style of one image to another using a pre-trained deep learning model from TensorFlow Hub.

## 🚀 Quick Start

### 1. Install dependencies
Make sure you have Python installed. In your terminal/command prompt, run:
```bash
pip install -r requirements.txt
```

### 2. Run the application
Start the Streamlit server:
```bash
streamlit run app.py
```

### 3. Usage
- Open the provided Local URL in your browser (usually `http://localhost:8501`).
- Upload a **Content Image** (e.g., a photo of a landscape or person).
- Upload a **Style Image** (e.g., a famous painting like Starry Night).
- Click **"Generate Art 🌟"** and wait a few seconds to see the result!


## 🛠 Tech Stack
- **[Streamlit](https://streamlit.io/):** For building the web UI simply and quickly.
- **[TensorFlow Hub](https://tfhub.dev/):** To load the pre-trained `magenta/arbitrary-image-stylization-v1-256` model. No need to train complex networks manually!
- **[Pillow (PIL)](https://python-pillow.org/) & Numpy:** For basic image processing.
