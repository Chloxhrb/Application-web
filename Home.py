from openai import OpenAI
import streamlit as st 

key_input = st.sidebar.text_input("Veuillez entré la clé Open IA")

client = OpenAI(
    api_key= key_input,
)

user_input = st.text_input("veuillez entré une description de l'image que vous souhaitez generer")

if user_input != "" :
    prompt = user_input
    image = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = image.data[0].url

    st.image( image_url )
