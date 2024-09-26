from openai import OpenAI
import streamlit as st 

st.set_page_config(
    page_title="Home - Générateur d'images",
    page_icon="https://quera.fr/wp-content/uploads/2022/11/cropped-Quera_Agence_Data_Webmarketing_logo.png",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.title("Dall-e 3")

key_input = st.sidebar.text_input("Veuillez entrer la clé Open IA")

client = OpenAI(
    api_key= key_input,
)

user_input = st.text_input("Veuillez entrer une description de l'image que vous souhaitez générer")

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
