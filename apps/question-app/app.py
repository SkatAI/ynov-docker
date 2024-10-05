import streamlit as st
from openai import OpenAI
import json

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Load character prompts from a JSON file
with open('character_prompts.json', 'r') as file:
    character_prompts = json.load(file)

# Streamlit UI
st.title("Ask a Question to a Character")
st.header("Le personnage vous répondra ")

# Select a character
character = st.selectbox("Choose a character:", list(character_prompts.keys()))

# Text area for user's question
user_question = st.text_area("What's your question?")

# Button to submit question
if st.button("Ask"):
    if user_question.strip() != "":
        prompt = character_prompts[character] + "\n" + user_question
        print(prompt)

        # Query OpenAI API

        try:

            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="gpt-3.5-turbo",
            )
            answer = chat_completion.choices[0].message.content
            st.write(f"**{character} says:** {answer}")
        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter a question.")

