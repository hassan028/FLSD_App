#Import Packages
import numpy as np
from PIL import Image
import streamlit as st
from io import BytesIO
import base64
import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)

icon = Image.open('icon.jpeg')
st.set_page_config(page_title='Classifier', page_icon = icon)
st.header('Face Liveness Spoofing Detection')
st.sidebar.subheader(("Input a Face Picture"))

#Get Image
file_up = st.sidebar.file_uploader('Upload an Image', type="jpeg")

def img_to_bytes(img):
    buffered = BytesIO()
    img.save(buffered, format=img.format)
    img_str = base64.b64encode(buffered.getvalue())
    strIMG = img_str.decode("utf-8")
    resp = get_response(strIMG)
    return resp

def get_response(ImgStr):
    url = 'https://27030819-823c-42a3-ab8a-3e05ca9185df.syndic.ai'
    data = {'url': ImgStr}

    x = requests.post(url, data, verify=False)
    return x.text

if file_up is not None:
    # display image that user uploaded
    image = Image.open(file_up)
    result = img_to_bytes(image)
    st.image(image, caption = 'Original Image', width=350)
    st.write("Predictions: ",result)
