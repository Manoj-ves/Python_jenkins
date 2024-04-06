from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def index():
    return 'Hello, World! This is my Flask app running on localhost:8080.'

if __name__ == '__main__':
    # Run the Flask application on localhost, port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
    print("Flask app is running on port 5000")
