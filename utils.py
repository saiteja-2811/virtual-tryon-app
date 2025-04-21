from PIL import Image
import io
import os

def load_image(uploaded_file):
    """Load image from Streamlit uploader."""
    try:
        image = Image.open(uploaded_file).convert("RGBA")
        return image
    except Exception as e:
        raise ValueError(f"Unable to open image: {e}")

def resize_image(image, size=(150, 150)):
    """Resize image to desired dimensions."""
    return image.resize(size)

def save_image(image, filename="output.png", folder="outputs"):
    """Save image to a folder."""
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.join(folder, filename)
    image.save(path)
    return path

def validate_filetype(file):
    """Optional filetype validator."""
    valid_types = ["jpeg", "jpg", "png"]
    filetype = file.name.split(".")[-1].lower()
    return filetype in valid_types
