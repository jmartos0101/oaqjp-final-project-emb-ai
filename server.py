''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# pylint: disable=import-error
from flask import Flask, render_template, request
from emotion_detection import emotion_detector
#Initiate the flask app : TODO
app = Flask("emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze emotion from input text."""
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    code = response["code"]

    # Return a formatted string with the sentiment label and score
    if code != 200:
        return "¡Entrada no válida! Intenta de nuevo."
    return response


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
