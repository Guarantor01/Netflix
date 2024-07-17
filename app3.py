import streamlit as st
from PIL import Image

st.title("Netflix")

img = Image.open("netflix logo.png")
st.image(img)

st.text_input(" First Name")
st.text_input(" Last Name")
st.text_input(" Email address")
st.text_input(" Password")
st.radio("Gender",["Male","Female"])
st.selectbox("Country",["Uk", "Us", "Nigeria", "South Africa", "Canada"])
st.text_area("Description",max_chars=200)

if st.checkbox("Agree"):
    st.write("Permission granted")
else:
    st.warning("click agree")

if st.button("Calculate"):
    st.success("Calculation successful")
    st.balloons()

st.file_uploader("Upload Your Picture",type=["PNG","JPEG","JPG"])
st.camera_input("Say Hello")
st.date_input("D.O.B")