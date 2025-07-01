#install and import the necessar libraries 
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import random

# --- Page Setup ---
st.set_page_config(page_title="Art Lab + Chat Companion", page_icon="🎨", layout="wide")
st.title("🎨 Art Lab + Chat Companion")
st.markdown("Welcome to your creative playground! Sketch your ideas and get inspired by your AI art buddy.")

# --- Section 1: Creative Quote Prompts ---
st.sidebar.header("💬 Your AI Art Companion Says:")

def get_creative_prompt():
    prompts = [
        "🎨 Draw your dream city!",
        "🌌 Try making a spiral galaxy!",
        "😊 What does 'happiness' look like to you?",
        "🔺 Make an abstract piece using only triangles and circles.",
        "🌿 Draw a nature-inspired scene!"
    ]
    return random.choice(prompts)

if st.sidebar.button("🎲 Inspire Me!"):
    st.sidebar.success(get_creative_prompt())

# --- Section 2: Drawing Canvas ---
st.subheader("🖌️ Draw Something Awesome Below")

# Define canvas parameters
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # translucent fill
    stroke_width=5,
    stroke_color="#000000",
    background_color="#ffffff",
    update_streamlit=True,
    height=400,
    width=700,
    drawing_mode="freedraw",
    key="canvas",
)

# --- Section 3: Optional Save Feedback ---
if canvas_result.image_data is not None:
    st.success("🖼️ Keep creating! You can take a screenshot to save your art.")
    # Optionally show preview
    # st.image(canvas_result.image_data)

# --- Footer ---
st.markdown("---")
st.caption("Built with Python, Streamlit & your imagination 🧠✨")
