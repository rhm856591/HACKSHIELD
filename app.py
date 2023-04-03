from flask import Flask, request, render_template
import pickle

# Load the model and vectorizer
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Create a Flask app
app = Flask(__name__)

# Define the home page route
@app.route('/')
def home():
    return render_template('index.html', result='')

# Define the route for checking if a message is spam or not
@app.route('/check', methods=['POST'])
def check():

    # Get the message from the request form
    message = request.form['message']


    # Vectorize the message
    message_vector = vectorizer.transform([message])

    # Predict if the message is spam or not
    is_spam = model.predict(message_vector)[0]

    # Display the result
    if is_spam == 1:
            result = "This messagße is spam."
    else:
            result = "This message is not spam."

    return render_template('index.html', result=result)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

