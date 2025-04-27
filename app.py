import streamlit as st
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ------------------------- Helper Functions -------------------------

def generate_tech_questions(tech_stack):
    """
    Generate 3-5 technical questions based on candidate's tech stack using Hugging Face Inference API.
    """
    api_token = os.getenv("HUGGINGFACE_API_TOKEN")
    if not api_token:
        return "Error: Hugging Face API token not found."

    model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"  # You can change model
    api_url = f"https://api-inference.huggingface.co/models/{model_id}"

    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }

    prompt = f"Generate 5 technical interview questions for a candidate skilled in {tech_stack}."

    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": 0.7,
            "max_new_tokens": 500
        }
    }

    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        try:
            # Some models return list, some dict
            return result[0]["generated_text"].strip()
        except (KeyError, IndexError):
            return "Error: Unexpected response format."
    else:
        return f"Error generating questions: {response.status_code} - {response.text}"

def save_candidate_data(candidate_data):
    """
    Save candidate data locally into a simple dictionary (simulate database).
    """
    if not os.path.exists('candidate_data.txt'):
        with open('candidate_data.txt', 'w') as f:
            pass
    with open('candidate_data.txt', 'a') as f:
        f.write(str(candidate_data) + "\n")

def initialize_session_state():
    """
    Initialize session state variables if not already done.
    """
    if 'step' not in st.session_state:
        st.session_state.step = 0
    if 'candidate_data' not in st.session_state:
        st.session_state.candidate_data = {}
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

# ------------------------- Main Streamlit App -------------------------

def main():
    st.set_page_config(page_title="TalentScout - Hiring Assistant", page_icon="🧑‍💻", layout="centered")
    st.title("🧑‍💻 TalentScout - Hiring Assistant")
    st.write("Welcome! I'm here to collect your basic details and generate some technical questions based on your skills.")

    initialize_session_state()

    # Display chat history
    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.markdown(chat["content"])

    # Define the conversation flow
    questions = [
        "Please enter your Full Name:",
        "Please enter your Email Address:",
        "Please enter your Phone Number:",
        "How many Years of Experience do you have?",
        "What is your Desired Position?",
        "Where are you currently located?",
        "Please list your Tech Stack (languages, frameworks, databases, tools):"
    ]

    if st.session_state.step < len(questions):
        # Ask next question
        with st.chat_message("assistant"):
            st.markdown(questions[st.session_state.step])

        user_input = st.chat_input("Your response")

        if user_input:
            if user_input.lower() in ["exit", "stop", "end"]:
                st.session_state.step = len(questions) + 1
                st.session_state.chat_history.append({"role": "user", "content": user_input})
                st.rerun()

            # Save user input
            field_names = ["Full Name", "Email", "Phone", "Experience", "Position", "Location", "Tech Stack"]
            st.session_state.candidate_data[field_names[st.session_state.step]] = user_input
            st.session_state.chat_history.append({"role": "user", "content": user_input})

            # Move to next step
            st.session_state.step += 1
            st.rerun()

    elif st.session_state.step == len(questions):
        # Generate technical questions
        tech_stack = st.session_state.candidate_data.get("Tech Stack", "")
        with st.chat_message("assistant"):
            st.markdown("Generating technical questions based on your tech stack... Please wait. ⏳")

        questions_generated = generate_tech_questions(tech_stack)

        with st.chat_message("assistant"):
            st.markdown(f"Here are your technical questions:\n\n{questions_generated}")

        st.session_state.chat_history.append({"role": "assistant", "content": f"Here are your technical questions:\n\n{questions_generated}"})

        # Save data
        save_candidate_data(st.session_state.candidate_data)

        with st.chat_message("assistant"):
            st.markdown("✅ Thank you! Your information has been recorded. You can now close this window.")

        st.session_state.step += 1  # move to finished
    else:
        st.success("Conversation Ended. Thank you!")

    # Restart button
    if st.button("🔄 Restart Conversation"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
# ------------------------- Entry Point -------------------------
if __name__ == "__main__":
    main()
