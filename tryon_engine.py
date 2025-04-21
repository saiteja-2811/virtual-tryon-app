from PIL import Image

def overlay_accessory(user_img, accessory_img_path, position=(50, 50), scale=(150, 50)):
    accessory = Image.open(accessory_img_path).convert("RGBA")
    accessory = accessory.resize(scale)
    user_img.paste(accessory, position, accessory)
    return user_img
