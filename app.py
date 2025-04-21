import streamlit as st
from PIL import Image
from tryon_engine import overlay_accessory

st.title("🧢 Virtual Try-On App")

uploaded_file = st.file_uploader("Upload your selfie", type=["jpg", "jpeg", "png"])

accessory = st.selectbox("Choose an accessory", ["sunglasses", "hat"])
accessory_map = {
    "sunglasses": "assets/sunglasses.png",
    "hat": "assets/hat.png"
}

if uploaded_file:
    user_img = Image.open(uploaded_file).convert("RGBA")
    result = overlay_accessory(user_img, accessory_map[accessory])
    st.image(result, caption="Here's your virtual look!", use_column_width=True)
