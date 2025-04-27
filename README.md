## 🧑‍💻 **TalentScout - Hiring Assistant**

## 🚀 **Project Overview**

TalentScout Hiring Assistant is an intelligent chatbot built with Streamlit and powered by a Hugging Face LLM (Mixtral-8x7B-Instruct) through API integration.
It assists in:

 - Collecting basic candidate information (name, email, experience, tech stack, etc.)

 - Automatically generating 3 to 5 technical interview questions based on the candidate’s technology expertise.

 - Saving candidate details locally for later review.

This tool simulates a real-time hiring assistant that recruiters or HR teams can deploy for initial technical screening.

## ⚙️ **Installation Instructions**

Follow these steps to set up and run the application locally:

### 🔄 **Clone the Repository**

```bash
git clone https://github.com/your-username/hiring-assistant.git
cd hiring-assistant

### 🖥️ **Set up a Virtual Environment (optional but recommended)**

```bash

python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
```
### 📦 **Install Required Packages**

```bash
pip install -r requirements.txt
```

### 🔐 **Create a .env file**
Add your Hugging Face API token:

```bash
HUGGINGFACE_API_TOKEN=your_huggingface_api_token_here
```

### 🚀 **Run the Streamlit Application**
```bash
streamlit run app.py
```

## 🎯 **Usage Guide**
Start the app using streamlit run app.py.

Enter your details step-by-step as the chatbot prompts:

1. Full Name

2. Email Address

3. Phone Number

4. Years of Experience

5. Desired Position

6. Current Location

7. Tech Stack

After completing the inputs, the bot will generate 3–5 technical questions tailored to your skills.

All candidate data will be saved locally in a file named candidate_data.txt.

Click "🔄 Restart Conversation" to begin a new session if needed.

## 🛠️ **Technical Details**
Frontend Framework: Streamlit

LLM Backend: Hugging Face Inference API (mistralai/Mixtral-8x7B-Instruct-v0.1)

Environment Management: dotenv

API Communication: requests

Session Management: Streamlit session_state

Data Storage: Local file (candidate_data.txt)

## 🧠 **Prompt Design**

###  **Information Gathering**
The chatbot uses a simple, friendly series of chat-style prompts to collect necessary candidate information without overwhelming them.

###  **Technical Question Generation**
A carefully crafted dynamic prompt is sent to the Hugging Face model:
```text
Generate 5 technical interview questions for a candidate skilled in {tech_stack}.
```
This design ensures:

1. Focus on the technologies the candidate mentioned.

2. Questions are at a basic to intermediate level.

3. LLM temperature is controlled at 0.7 for balanced creativity and relevance.

## 🚧 **Challenges & Solutions**

| **Challenge** | **Solution** |
|:--------------|:-------------|
| Hugging Face models sometimes return unpredictable response formats. | Added robust error handling while parsing API responses. |
| Ensuring the conversation flow feels natural in Streamlit. | Used `session_state` and `chat_message` components to simulate a real chat experience. |
| Managing API token security. | Implemented `.env` file loading with `python-dotenv` to avoid exposing sensitive credentials. |
| Preventing session data from leaking between candidates. | Provided a clear "Restart Conversation" button to reset `session_state`. |

## 📢  **Final Note**
"TalentScout - Hiring Assistant" provides a strong foundation for building more sophisticated HR automation tools by adding resume parsing, ATS integration, or advanced analytics later.
