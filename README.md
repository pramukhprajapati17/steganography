# steganography
This project securely hides secret messages inside images using ASCII-XOR based encryption and pixel value substitution.
# 🔐 Image Steganography Using ASCII-XOR Based Encryption

This project demonstrates a simple image steganography technique that securely hides secret messages inside images using **ASCII-XOR encryption** and **pixel value substitution**. Built with Python and Streamlit, it allows users to encrypt and decrypt messages visually embedded in images.

---

## 📌 Features

- 🔏 **Encrypt Message**: Hide a secret message in an image using a pass key.
- 🔓 **Decrypt Message**: Retrieve the hidden message using the correct key and message length.
- 🖼️ **Image Support**: Works with PNG, JPG, JPEG images.
- ⚙️ **XOR Encryption**: Applies character-wise XOR between message and key for secure encoding.
- 🧪 **Simple UI**: Interactive Streamlit web interface for ease of use.

---

## 🛠️ Technologies Used

- Python 3
- [Streamlit](https://streamlit.io/) – For the UI
- OpenCV (`cv2`) – For image manipulation
- Pillow (`PIL`) – For image loading and saving
- NumPy – For pixel operations

---

## 🚀 How to Run Locally

### 📥 Clone the Repository

```bash
git clone https://github.com/pramukhprajapati17/steganography.git
cd steganography

## for Run
streamlit run app.py


