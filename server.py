"""
Flask server for the Emotion Detection web application.
Provides routes and handles interaction with the emotion detector.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the main page of the web application.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Handle requests to analyze the emotion in a given text.
    Returns an error message if the text is invalid or empty.
    """
    text = request.args.get("textToAnalyze", default="", type=str)
    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)
