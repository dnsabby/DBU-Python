# app.py

# Import necessary modules from the Flask package
from flask import Flask, request, redirect, url_for, abort

# Create an instance of the Flask class
app = Flask(__name__)

# --------------------
# Basic Routing Examples
# --------------------

# Basic route that maps the URL '/' to the hello_world function
@app.route('/')
def hello_world():
    # Returns a simple greeting
    return 'Hello, World! Welcome to Flask Routing Demo.'

# Route with a dynamic segment that accepts a string variable 'username'
@app.route('/user/<username>')
def show_user_profile(username):
    # Displays the user's profile page
    return f'User {username}\'s Profile Page'

# Route with a dynamic segment that accepts an integer variable 'post_id'
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Displays the post with the given ID
    return f'Post Number {post_id}'

# Route that accepts only a float variable 'pi_value'
@app.route('/pi/<float:pi_value>')
def show_pi(pi_value):
    # Displays the float value passed in the URL
    return f'The value of Pi is approximately {pi_value}'

# --------------------
# Routing with Methods
# --------------------

# Route that handles both GET and POST requests for '/login'
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process login credentials and authenticate the user
        return 'Processing login...'
    else:
        # Display the login form to the user
        return 'Please enter your login credentials.'

# --------------------
# URL Building
# --------------------

# Route that demonstrates URL building with 'url_for'
@app.route('/dashboard')
def dashboard():
    # Redirects to the admin dashboard
    return 'Welcome to your dashboard!'

@app.route('/redirect-to-dashboard')
def redirect_to_dashboard():
    # Uses 'url_for' to build the URL for 'dashboard' function
    return redirect(url_for('dashboard'))

# --------------------
# Handling Errors
# --------------------

# Custom error handler for 404 Not Found
@app.errorhandler(404)
def page_not_found(error):
    # Returns a custom 404 error message
    return 'This page does not exist. Please check the URL.', 404

# --------------------
# Variable Rules with Options
# --------------------

# Route with a dynamic segment and a default value
@app.route('/greet/', defaults={'name': 'Guest'})
@app.route('/greet/<name>')
def greet(name):
    # Greets the user with the provided name or 'Guest' if no name is provided
    return f'Hello, {name}!'

# --------------------
# Starting the Application
# --------------------

# Checks if the script is run directly (and not imported)
if __name__ == '__main__':
    # Runs the Flask application in debug mode on localhost port 5000
    app.run(debug=True)