import cohere
import streamlit as st

# Initialize Cohere API client
cohere_api_key = 'Mrh9BFF0YcKhl4jp5JC7ijKj0JwpQXdKFiz2aWm4'  # Replace this with your Cohere API key
co = cohere.Client(cohere_api_key)

# Function to generate story using Cohere's 'generate' module
def generate_story(prompt):
    try:
        # Generate the story based on the prompt using Cohere's generation capabilities
        response = co.generate(
            model='command-xlarge-nightly',  # Using a different model (command-xlarge-nightly)
            prompt=prompt,
            max_tokens=500,  # Control the length of the generated story
            temperature=0.8,  # Controls creativity; higher value means more creative output
            stop_sequences=["\n"]  # Stop generation at newlines if needed
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"Error generating story: {e}"

# Streamlit interface
st.title("Text to Story Generator")

st.markdown("### Enter a prompt to generate a story:")

# Input box for the prompt
user_prompt = st.text_area("Prompt:", "A young girl discovers a magical forest.")

# Button to generate the story
if st.button('Generate Story'):
    if user_prompt:
        with st.spinner('Generating story...'):
            story = generate_story(user_prompt)
            st.markdown("### Generated Story:")
            st.write(story)
    else:
        st.warning("Please enter a prompt to generate the story.")
