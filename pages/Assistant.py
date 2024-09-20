import os
from openai import OpenAI

import streamlit as st

key_input = st.sidebar.text_input("Veuillez entré la clé Open IA")

client = OpenAI(
    api_key= key_input,
)
user_input = st.text_input("Tapez votre texte :")
prompt = user_input

if user_input != "" :
    chat_completion = client.chat.completions.create(
        messages=[
             {
              "role": "system",
             "content": f"Tu es un traducteur de langue qui traduit de l'anglais vers le français. Si le texte en entrée n'est pas en anglais, tu retournes la phrase : 'Je ne prends que du texte en anglais.'"
             },
    
            {
                "role": "user",
                "content": "Hello everyone !",
            },
            {
                "role": "assistant",
                "content": "La traduction est : Bonjour tout le monde !",
            },
             {
                "role": "user",
                "content": "Hola todos",
            },
            {
                "role": "assistant",
                "content": "Je ne prends que du texte en anglais.",
            },
             {
                "role": "user",
                "content": "Bonjour tout le monde !",
            },
            {
                "role": "assistant",
                "content": "Je ne prends que du texte en anglais.",
            },
             {
                "role": "user",
                "content": prompt,
            },
        ],
        model="gpt-3.5-turbo",
        temperature=0.3,
      max_tokens=100,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    
    st.write(chat_completion.choices[0].message.content)
