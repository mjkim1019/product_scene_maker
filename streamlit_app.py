from io import BytesIO

import streamlit as st
from PIL import Image
#from rembg import remove
from openai import OpenAI

def setup_page():
    # Show title and description.
    st.set_page_config(layout="wide", page_title="Product Scene Maker")

    st.write("## 🎨 Product Scene Maker: AI로 만드는 맞춤형 상품 배경")
    st.write(
        "AI로 만드는 맞춤형 상품 배경: 이미지를 업로드하고 원하는 프롬프트를 작성해보세요"
    )
    st.sidebar.write("## Upload and download :gear:")

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

# Package the transform into a function
def fix_image(upload):
    # Create the columns
    col1, col2 = st.columns(2)

    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)


    col2.write("Fixed Image :wrench:")
    #fixed = remove(image)
    fixed = image
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button(
        "Download fixed image", convert_image(fixed), "fixed.png", "image/png"
    )

def process_and_display_images(uploaded_files):
    """Processes the uploaded files and displays the original and result images."""
    if not uploaded_files:
        st.warning("Please upload an image.")
        return

    if not st.sidebar.button("Remove Background"):
        return


def main():
    setup_page()

    # Create the file uploader
    my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    
    # Fix the image!
    if my_upload is not None:
        image_upload = my_upload
    else:
        image_upload = "./quokka.jpeg"

    fix_image(upload=image_upload)



if __name__ == "__main__":
    main()