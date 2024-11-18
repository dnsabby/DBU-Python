# app.py
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# --------------------
# In-Memory Data Store
# --------------------

# A simple in-memory data store to hold our resources
# For demonstration purposes, we'll use a list of dictionaries
books = [
    {'id': 1, 'title': 'The Pragmatic Programmer', 'author': 'Andrew Hunt'},
    {'id': 2, 'title': 'Clean Code', 'author': 'Robert C. Martin'},
    {'id': 3, 'title': 'Introduction to Algorithms', 'author': 'Thomas H. Cormen'}
]

# --------------------
# RESTful API Routes
# --------------------

# Route to get all books
@app.route('/api/books', methods=['GET'])
def get_books():
    """
    Get the list of all books.
    """
    return jsonify({'books': books})

# Route to get a book by its ID
@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """
    Get a single book by ID.
    """
    # Search for the book in the list
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        # If the book is not found, return a 404 response
        abort(404)
    return jsonify({'book': book})

# Route to create a new book
@app.route('/api/books', methods=['POST'])
def create_book():
    """
    Create a new book.
    """
    # Check if the request contains JSON data and required fields
    if not request.json or not 'title' in request.json or not 'author' in request.json:
        # Bad request if 'title' or 'author' is missing in the request
        abort(400)
    # Create a new book object
    new_book = {
        'id': books[-1]['id'] + 1 if books else 1,  # Incremental ID
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    # Return the new book with 201 Created status
    return jsonify({'book': new_book}), 201

# Route to update an existing book
@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """
    Update a book by ID.
    """
    # Find the book to update
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        # If the book is not found, return a 404 response
        abort(404)
    if not request.json:
        # Bad request if no JSON data is provided
        abort(400)
    # Update the book's title and author if provided in the request
    book['title'] = request.json.get('title', book['title'])
    book['author'] = request.json.get('author', book['author'])
    return jsonify({'book': book})

# Route to delete a book
@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """
    Delete a book by ID.
    """
    # Find the book to delete
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        # If the book is not found, return a 404 response
        abort(404)
    books.remove(book)
    # Return an empty response with 204 No Content status
    return '', 204

# --------------------
# Error Handlers
# --------------------

@app.errorhandler(404)
def not_found(error):
    """
    Custom 404 error handler.
    """
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(400)
def bad_request(error):
    """
    Custom 400 error handler.
    """
    return jsonify({'error': 'Bad request'}), 400

# --------------------
# Starting the Application
# --------------------

if __name__ == '__main__':
    # Run the app on localhost port 5000 in debug mode
    app.run(debug=True)


# --------------------
# Exercise: Implement Search Functionality
# Objective:
# Extend the API to allow users to search for books by title or author.
# 
#Instructions:
#	1.	Modify the /api/books GET Route:
#	•	Accept optional query parameters title and author.
#	•	If provided, filter the books list to include only books that match the search criteria.
#	•	Perform case-insensitive matching.
#	2.	Return the Filtered List:
#	•	Return the list of books that match the search criteria in JSON format.
# --------------------

# HINT:
    # Modify get_books() to accept query parameters title and author.
    # Filter the books list based on the search criteria.
    # Use the in operator to perform case-insensitive matching.

    # Get query parameters
    #title = request.args.get('title')
    #author = request.args.get('author')

    # Start with all books
    #filtered_books = books

    # Perform string search by using the following condition:
    # [book for book in filtered_books if {text_your_finding}.lower() in book['title'].lower()]