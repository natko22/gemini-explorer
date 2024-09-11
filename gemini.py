import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, GenerationConfig

# Set your Google Cloud project ID as a string
project = "gemini-explorer-434508"

# Initialize Vertex AI with the project
vertexai.init(project=project)

# Configuration for the generative model
config = GenerationConfig(temperature=0.4)

# Load and initialize the generative model
model = generative_models.GenerativeModel("gemini-pro", generation_config=config)

# Start a chat session
chat = model.start_chat()

# Function to send message to the model
def llm_function(chat, user_input, user_name="User"):
    response = chat.send_message(user_input)
    
    # Initialize an empty string for the response text
    response_text = ""

    try:
        # Log the raw response to see the structure
        st.write(f"Full response: {response}")

        # Accessing the response safely
        if hasattr(response, 'candidates') and len(response.candidates) > 0:
            candidate = response.candidates[0]
            # Access the content parts safely
            if hasattr(candidate, 'content') and hasattr(candidate.content, 'parts'):
                part = candidate.content.parts  # Directly access the parts object
                if hasattr(part, 'text'):
                    # Extract the text without additional encoding or decoding
                    response_text = part.text.strip()
                else:
                    response_text = "No valid text found in the response."
            else:
                response_text = "No valid content found in the response."
        else:
            response_text = "No valid candidates found in the response."
    except Exception as e:
        st.error(f"Error parsing response: {e}")
        response_text = "Oops! Something went wrong with the response."

    # Store user message and assistant's response in session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    
    # Personalize the response with the user's name
    personalized_response = f"{response_text} 😊 (By the way, {user_name}, let me know if you need anything else!)"
    
    return personalized_response

# Initialize the Streamlit session state for messages if not already done
if "messages" not in st.session_state:
    st.session_state.messages = []

# Capture user's name
user_name = st.text_input("Please enter your name", key="name_input")

# If user's name is provided, send a personalized greeting
if user_name and len(st.session_state.messages) == 0:
    initial_prompt = f"Hey {user_name}! I'm ReX, powered by Google Gemini, and I'm SO excited to chat with you! 🎉 Let's get this convo started with some cool ideas!"
    llm_function(chat, initial_prompt, user_name)

# Streamlit interface for user input
st.title("Chat with ReX, powered by Google Gemini")

# Capture user input for the chat
user_input = st.text_input("You:", "")

# Send message on user input
if user_input:
    response = llm_function(chat, user_input, user_name)
    st.write(f"ReX: {response}")

# Display previous chat history
if st.session_state.messages:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.write(f"You: {message['content']}")
        else:
            st.write(f"ReX: {message['content']}")
