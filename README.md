# Chat with ReX - Powered by Google Gemini

This project demonstrates how to integrate **Google Vertex AI** with **Streamlit** to create an interactive chatbot named **ReX**. The bot is powered by **Google Gemini**.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Environment Setup and Installation](#environment-setup-and-installation)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [License](#license)

## Overview

This project is built to demonstrate the following:

- Interfacing with **Google Vertex AI** to interact with a **Generative Model**.
- Utilizing **Streamlit** for creating a user-friendly web interface.
- Ensuring the chatbot ReX can process and return conversational responses in real-time.

## Features

- Connects to **Google Vertex AI** to load the **Gemini generative model**.
- Chat interface built using **Streamlit**.
- Real-time responses from ReX, powered by Google Gemini, using the **GenerativeModel** API.

## Installation

### Prerequisites

1. **Python**: Ensure Python 3.8 or higher is installed. You can check the version by running:

   ```bash
   python --version

   ```

2. **Google Cloud Account**:

- Set up a Google Cloud Project with Vertex AI API enabled.
- Note your Google Cloud Project ID, as you will use it in the code.
- Streamlit: Install Streamlit, the framework used for creating the web interface.
  -Google Vertex AI Python SDK: Used to interact with Google Vertex AI.

### Environment Setup and Installation

1. Clone the repository
   git clone https://github.com/natko22/rex-google-gemini-chat.git

   cd rex-google-gemini-chat

2. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate

# On Windows, use `venv\Scripts\activate`

3. Install the required dependencies:

pip install streamlit vertexai python-dotenv

4. Replace your Google Cloud Project ID in the code. In the app.py file, update the following line:

project = "your-gcp-project-id"

### Required Libraries

- Install the following libraries:

- vertexai: To interact with Google - Vertex AI's GenerativeModel API.
- Streamlit: For creating the
- interactive chat interface.
- python-dotenv: For managing
- environment variables (if needed later).

pip install vertexai streamlit python-dotenv

### Running the Application

1. Activate the virtual environment (if not already active):

source venv/bin/activate

# For Windows: `venv\Scripts\activate`

2. Run the Streamlit application:
   streamlit run app.py

3. Navigate to the browser: After running the above command, open your browser and visit:

http://localhost:8501

### License

This project is licensed under the MIT License.
