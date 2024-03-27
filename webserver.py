from flask import Flask

# Create an instance of Flask
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'Welcome to the Mesosphere Explorer!'

# Define a route for the about page
@app.route('/about')
def about():
    return 'This is a web server built with Python and Flask to explore the mesosphere.'

# Define a route for the mesosphere page
@app.route('/mesosphere')
def mesosphere():
    return 'The mesosphere is the third layer of Earth\'s atmosphere.'

# Define a route for the near space page
@app.route('/near_space')
def near_space():
    return 'Near space refers to altitudes within the mesosphere.'

# Run the app if executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
