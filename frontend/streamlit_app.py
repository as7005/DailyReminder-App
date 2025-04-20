import streamlit as st
import requests
import json
import tempfile
import speech_recognition as sr
from streamlit_mic_recorder import mic_recorder
from pydub import AudioSegment

BASE_URL = "http://127.0.0.1:5000/api"

# Backend functions (unchanged)
def register_user(username, password):
    data = {"username": username, "password": password}
    response = requests.post(f"{BASE_URL}/register", json=data)
    return response.json()

def login_user(username, password):
    data = {"username": username, "password": password}
    response = requests.post(f"{BASE_URL}/login", json=data)
    return response.json()

def get_reminders():
    response = requests.get(f"{BASE_URL}/reminders")
    return response.json()

def add_reminder(reminder, priority, notification_time):
    data = {
        "reminder": reminder,
        "priority": priority,
        "notification_time": notification_time
    }
    response = requests.post(f"{BASE_URL}/reminders", json=data)
    return response.json()

def update_reminder(reminder_id, reminder, priority, notification_time):
    data = {
        "id": reminder_id,
        "reminder": reminder,
        "priority": priority,
        "notification_time": notification_time
    }
    response = requests.put(f"{BASE_URL}/reminders", json=data)
    return response.json()

def delete_reminder(reminder_id):
    data = {"id": reminder_id}
    response = requests.delete(f"{BASE_URL}/reminders", json=data)
    return response.json()

# UI starts
st.title('Reminder App')

auth_option = st.sidebar.radio("Authentication", ["Login", "Register"])

if auth_option == "Register":
    username = st.text_input("Enter username")
    password = st.text_input("Enter password", type="password")
    if st.button("Register"):
        result = register_user(username, password)
        st.write(result)

elif auth_option == "Login":
    username = st.text_input("Enter username", key="login_username")
    password = st.text_input("Enter password", type="password", key="login_password")
    if st.button("Login"):
        result = login_user(username, password)
        if result['success']:
            st.session_state['user'] = username
            st.write(result)
        else:
            st.write(result)

if 'user' in st.session_state:
    st.subheader("Welcome, " + st.session_state['user'])
    reminder_action = st.sidebar.radio("Reminders", ["View", "Add", "Edit", "Delete"])

    if reminder_action == "View":
        reminders = get_reminders()
        for reminder in reminders['reminders']:
            st.write(f"ID: {reminder['id']} - {reminder['reminder']} - Priority: {reminder['priority']}")

    elif reminder_action == "Add":
        st.markdown("### 🎤 Voice Reminder Input (Optional)")
        audio = mic_recorder(start_prompt="🎙️ Start recording", stop_prompt="🛑 Stop", key="voice")

        voice_input = ""
        if audio:
            recognizer = sr.Recognizer()

            # Save raw audio to temporary OGG file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".ogg") as raw_file:
                raw_file.write(audio["bytes"])
                raw_path = raw_file.name

            # Convert to WAV using pydub
            wav_path = raw_path.replace(".ogg", ".wav")
            try:
                sound = AudioSegment.from_file(raw_path)
                sound.export(wav_path, format="wav")

                with sr.AudioFile(wav_path) as source:
                    audio_data = recognizer.record(source)
                    try:
                        voice_input = recognizer.recognize_google(audio_data)
                        st.success(f"Recognized: {voice_input}")
                    except sr.UnknownValueError:
                        st.error("Sorry, could not understand the audio.")
                    except sr.RequestError:
                        st.error("API unavailable or network error.")
            except Exception as e:
                st.error(f"Audio conversion failed: {e}")

        reminder = st.text_input("Enter reminder", value=voice_input)
        priority = st.selectbox("Priority", ["High", "Medium", "Low"])
        notification_time = st.text_input("Notification Time (YYYY-MM-DD HH:MM:SS)")

        if st.button("Add Reminder"):
            result = add_reminder(reminder, priority, notification_time)
            st.write(result)

    elif reminder_action == "Edit":
        reminder_id = st.number_input("Enter reminder ID to edit", min_value=1)
        reminder = st.text_input("Updated reminder")
        priority = st.selectbox("Priority", ["High", "Medium", "Low"])
        notification_time = st.text_input("Updated Notification Time (YYYY-MM-DD HH:MM:SS)")

        if st.button("Edit Reminder"):
            result = update_reminder(reminder_id, reminder, priority, notification_time)
            st.write(result)

    elif reminder_action == "Delete":
        reminder_id = st.number_input("Enter reminder ID to delete", min_value=1)
        if st.button("Delete Reminder"):
            result = delete_reminder(reminder_id)
            st.write(result)
