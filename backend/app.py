from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

users = {}  # Stores registered users
reminders = []  # Stores reminders

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users:
        return jsonify({"success": False, "message": "User already exists"})
    
    users[username] = password
    return jsonify({"success": True, "message": "User registered successfully"})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username not in users or users[username] != password:
        return jsonify({"success": False, "message": "Invalid username or password"})
    
    return jsonify({"success": True, "message": "Login successful"})

@app.route("/reminders", methods=["GET"])
def get_reminders():
    return jsonify({"reminders": reminders})

@app.route("/reminders", methods=["POST"])
def add_reminder():
    data = request.get_json()
    reminder = data.get("reminder")
    priority = data.get("priority")
    notification_time = data.get("notification_time")
    reminder_id = len(reminders) + 1

    reminder_data = {
        "id": reminder_id,
        "reminder": reminder,
        "priority": priority,
        "notification_time": notification_time,
        "created_at": datetime.now().isoformat()
    }

    reminders.append(reminder_data)
    return jsonify({"success": True, "message": "Reminder added successfully", "reminder": reminder_data})

@app.route("/reminders", methods=["PUT"])
def update_reminder():
    data = request.get_json()
    reminder_id = data.get("id")
    reminder = data.get("reminder")
    priority = data.get("priority")
    notification_time = data.get("notification_time")

    for r in reminders:
        if r["id"] == reminder_id:
            r["reminder"] = reminder
            r["priority"] = priority
            r["notification_time"] = notification_time
            return jsonify({"success": True, "message": "Reminder updated successfully"})
    
    return jsonify({"success": False, "message": "Reminder not found"})

@app.route("/reminders", methods=["DELETE"])
def delete_reminder():
    data = request.get_json()
    reminder_id = data.get("id")

    for r in reminders:
        if r["id"] == reminder_id:
            reminders.remove(r)
            return jsonify({"success": True, "message": "Reminder deleted successfully"})
    
    return jsonify({"success": False, "message": "Reminder not found"})

if __name__ == "__main__":
    app.run(debug=True)
