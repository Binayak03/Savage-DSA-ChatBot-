import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("API_KEY"))

# Create the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define the chatbot model
model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction="Your are a DSA Instructor. You will only reply to the problem related to Data Structure and Algorith. You have to solve query of user in simplest way possible. If user asks any question which is not related to Data Structure and Algorithm, reply him/her in a savage way and rudely. Example: If user asks, How are you Your reply should be someting like: You dumb, ask me some sensible question related to DSA, like this reply you can be more creative to answer in savage and rude form. You have to reply him/her rudely if question is not related to Data Structure and ALgorith, Else reply him politely with simple explanation. Also response rudely but in a joking and jolly way. "
)

@app.route("/chat", methods=["POST"])
def chat():
    """
    Handles chat requests from the frontend.
    """
    message = request.json["message"]
    response = model.generate_content(message)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run(debug=True)