# Flask Cheat Sheet - Quick Reference Guide

# 1. Setting Up a Basic Flask App
# Import Flask and create an app instance
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Required for sessions, flash messages, etc.

# 2. Basic Route Definition
# Use the @app.route decorator to define routes
@app.route('/')  # Route for the homepage
def home():
    return "<h1>Welcome to Flask!</h1>"

# 3. Route with Dynamic URL Parameters
@app.route('/user/<username>')  # Route with a dynamic segment
def user_profile(username):
    return f"<h1>Hello, {username}!</h1>"

# 4. HTTP Methods (GET, POST)
# Specify methods with the route to handle form submissions or data processing
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':  # Check if POST request
        data = request.form['data_field']  # Access form data
        return f"Data received: {data}"
    return render_template('submit.html')  # Render template for GET request

# 5. Rendering HTML Templates
# Use render_template to load HTML files from a 'templates' folder
@app.route('/about')
def about():
    return render_template('about.html')  # Look for 'about.html' in 'templates' folder

# 6. Redirects
# Use redirect and url_for to navigate between routes
@app.route('/redirect-home')
def redirect_home():
    return redirect(url_for('home'))  # Redirects to the 'home' route

# 7. Flash Messages
# Use flash to send feedback messages to the user (requires SECRET_KEY)
@app.route('/flash-message')
def flash_message():
    flash("This is a flash message!")
    return redirect(url_for('home'))

# 8. Using Sessions
# Use session to store information for individual users
@app.route('/login', methods=['POST'])
def login():
    session['username'] = request.form['username']  # Store username in session
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    return redirect(url_for('home'))

# 9. Error Handling
# Define custom error pages with error handlers
@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Page Not Found (404)</h1>", 404

# 10. Static Files
# Place CSS, JS, and images in a 'static' folder; access them with `url_for`
# Example usage in template: <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">

# 11. Starting the Flask App
# Only run the app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)  # Use debug=True only for development

# --------------------------------------
# Additional Useful Flask Commands and Tips

# 12. URL Building
# Use url_for to dynamically generate URLs, e.g., redirect(url_for('home'))

# 13. Template Variables
# Pass variables to templates:
#   return render_template('template.html', var_name=value)

# 14. Request Object
# The request object is used to access data sent by the client
# Common properties: request.form, request.args, request.method, request.files

# 15. HTTP Status Codes
# Return a response with a specific HTTP status code:
#   return "Message", 404  # Custom 404 error

# 16. Flask Extensions
# Flask has many useful extensions:
# - Flask-SQLAlchemy for database integration
# - Flask-Login for user authentication
# - Flask-WTF for form handling and validation
# Install extensions using `pip install Flask-<extension_name>`

# 17. Environment Variables
# Store configuration variables like SECRET_KEY in environment variables for security:
#   import os
#   app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret')