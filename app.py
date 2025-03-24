from flask import Flask, jsonify
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create the Flask app
app = Flask(__name__)

# Connect to your MySQL RDS database
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# Home route
@app.route('/')
def home():
    return "✅ SolveOnyx API is running!"

# Customers route
@app.route('/customers')
def get_customers():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customer")
    result = cursor.fetchall()
    cursor.close()
    return jsonify(result)

# Run the app
if __name__ == '__main__':
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
