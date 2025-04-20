
# Daily Reminder App (Streamlit + Flask)

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
