"""
Emotion Detection Server

This script, server.py, is the main entry point for our application. 
It sets up a server using the Flask framework, a lightweight and flexible 
micro web framework for Python.

The server is designed to perform emotion detection on user-provided text. 
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotionDetector")

@app.route("/")
def index():
    """
    This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_emotion():
    """
    Analyze the user-provided text for emotions and return the result.
    """
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)
    # if response['dominant_emotion'] is not None:
    #     string_response = f"""
    #     for the given statement, the system response is anger: {response['anger']}, 
    #     \n disgust: {response['disgust']} 
    #     \n fear: {response['fear']}
    #     \n joy: {response['joy']}
    #     \n sadness: {response['sadness']} .
    #     The dominant emotion is {response['dominant_emotion']}"""
    # else:
    #     string_response = 'Invalid text! Please try again!.'
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug = True)
