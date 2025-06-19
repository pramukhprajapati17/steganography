pip install opencv-python
import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

# ASCII maps
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Encrypt function
def encrypt_image(image, message, key):
    image_np = np.array(image)
    x_enc = image_np.copy()
    h, w, _ = x_enc.shape

    if len(message) > h * w * 3:
        raise ValueError("Message too long for image size.")

    n = m = z = kl = 0
    for i in range(len(message)):
        ascii_val = d[message[i]] ^ d[key[kl]]
        orig_val = x_enc[n, m, z]
        x_enc[n, m, z] = ascii_val

        kl = (kl + 1) % len(key)
        z += 1
        if z == 3:
            z = 0
            m += 1
            if m == w:
                m = 0
                n += 1

    return Image.fromarray(x_enc)

# Decrypt function
def decrypt_image(image, key, msg_len):
    image_np = np.array(image)
    h, w, _ = image_np.shape
    n = m = z = kl = 0
    msg = ""

    for i in range(msg_len):
        enc_val = image_np[n, m, z]
        dec_val = enc_val ^ d[key[kl]]
        msg += c[dec_val]

        kl = (kl + 1) % len(key)
        z += 1
        if z == 3:
            z = 0
            m += 1
            if m == w:
                m = 0
                n += 1

    return msg

# Streamlit UI
st.title("🔐 Image Encryption & Decryption with Secret Key")

tab1, tab2 = st.tabs(["🔏 Encrypt", "🔓 Decrypt"])

with tab1:
    st.header("Encrypt a Message into Image")
    uploaded_img = st.file_uploader("Upload an Image (PNG recommended)", type=["png", "jpg", "jpeg"])
    secret = st.text_input("Enter Secret Message")
    key = st.text_input("Enter Pass Key")

    if uploaded_img and secret and key:
        image = Image.open(uploaded_img).convert("RGB")
        encrypted_img = encrypt_image(image, secret, key)
        st.image(encrypted_img, caption="Encrypted Image", use_column_width=True)

        buf = io.BytesIO()
        encrypted_img.save(buf, format="PNG")
        st.download_button("Download Encrypted Image", buf.getvalue(), file_name="encrypted_image.png")

with tab2:
    st.header("Decrypt Message from Image")
    uploaded_img2 = st.file_uploader("Upload Encrypted Image", type=["png", "jpg", "jpeg"], key="decrypt")
    key2 = st.text_input("Enter Pass Key to Decrypt")
    msg_len = st.number_input("Enter Length of Original Message", min_value=1, step=1)

    if uploaded_img2 and key2 and msg_len:
        image = Image.open(uploaded_img2).convert("RGB")
        try:
            message = decrypt_image(image, key2, msg_len)
            st.success("Decrypted Message:")
            st.code(message)
        except Exception as e:
            st.error(f"Error: {e}")
