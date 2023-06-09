import streamlit as st
import numpy as np
from PIL import Image
#import cv2

#def final():

st.title("GennyAI App")
st.write("This Web App is to help convert your clothes to digital wardrobe")

file_image = st.file_uploader("Upload your Photos", type=['jpeg','jpg','png'])

if file_image is None:
    st.write("You haven't uploaded any image file")

else:
    input_img = Image.open(file_image)
    #final_sketch = final(np.array(input_img))
    st.write("**Input Photo**")
    st.image(input_img, use_column_width=True)
    st.write("**Output**")
    #st.image(final_sketch, use_column_width=True)