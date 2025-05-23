# Daily Reminder App

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-darkgreen)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-brightgreen)
![Status](https://img.shields.io/badge/Status-Prototype-orange)

A simple reminder app built with Flask for the backend and Streamlit for the frontend. This app allows users to register, log in, and manage their reminders. Users can add, edit, view, and delete reminders, with options to set priorities and notification times.

## Features

- **User Authentication**: Register and log in to the app.
- **Reminder Management**: Add, edit, view, and delete reminders.
- **Voice Recognition**: Use voice commands to input reminders.
- **Priority & Notification Time**: Set priority and specific notification times for each reminder.
- **Audio Conversion**: Convert recorded audio to text for reminders.

## Technologies Used

### Backend:

- **Flask**: A micro web framework for Python used for the backend.

- **SQLite**: A lightweight database used for storing user data and reminders.

### Frontend:

- **Streamlit**: A framework to quickly create data applications and interactive UIs.

- **Speech Recognition**: A Python library for speech-to-text conversion.

- **Pydub**: A simple and easy-to-use Python library for manipulating audio files.

- **pyttsx3**: A library used for text-to-speech conversion.
  
## Setup and Installation

### Prerequisites

Make sure you have the following installed:
- Python 3.x
- Git (for version control)

### Clone the Repository

```bash
git clone https://github.com/as7005/DailyReminder-App.git
cd DailyReminder-App


## 🔧 Setup

1. **Install dependencies** (inside virtual env if preferred):
```bash
pip install -r requirements.txt
```

2. **Create SQLite DB** (one-time setup):
```bash
cd backend
python
>>> import sqlite3
>>> conn = sqlite3.connect('database.db')
>>> conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT);")
>>> conn.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin');")
>>> conn.execute('''CREATE TABLE reminders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        priority TEXT,
        timestamp TEXT,
        done INTEGER)''')
>>> conn.commit()
>>> conn.close()
```

3. **Run Flask API**:
```bash
cd backend
python app.py
```

4. **Run Streamlit App**:
```bash
cd frontend
streamlit run streamlit_app.py
```

Login with: `admin / admin`
