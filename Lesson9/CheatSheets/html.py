# HTML5 Cheat Sheet - Quick Reference Guide

# 1. Basic HTML Document Structure
# <!DOCTYPE html>              # Defines document type as HTML5
# <html lang="en">             # Root element with language attribute
#   <head>                     # Contains metadata, title, links, scripts
#     <meta charset="UTF-8">   # Character encoding
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">  # Responsive design
#     <title>Page Title</title>  # Title displayed in browser tab
#     <link rel="stylesheet" href="styles.css">  # Link to external CSS
#   </head>
#   <body>                     # Main content area
#     <!-- Page content here -->
#   </body>
# </html>

# 2. Common Text Elements
# <h1> to <h6>         # Headings from largest (h1) to smallest (h6)
# <p>                  # Paragraph
# <br>                 # Line break (self-closing)
# <hr>                 # Horizontal rule (self-closing)
# <strong> and <em>    # Bold and italic text, respectively
# <blockquote>         # Quoted text

# Example:
# <h1>Main Heading</h1>
# <p>This is a paragraph with <strong>bold</strong> and <em>italic</em> text.</p>

# 3. Lists
# <ul>                # Unordered list (bullet points)
# <ol>                # Ordered list (numbered)
# <li>                # List item (used inside <ul> or <ol>)

# Example:
# <ul>
#   <li>Item 1</li>
#   <li>Item 2</li>
# </ul>

# 4. Links and Images
# <a href="URL">      # Hyperlink; set URL with href attribute
# <img src="image.jpg" alt="Description">  # Image element with source and alt text

# Example:
# <a href="https://www.example.com">Visit Example</a>
# <img src="logo.png" alt="Website Logo" width="200" height="100">

# 5. Forms
# <form action="submit_form.php" method="POST">  # Form element; define action and method
# <input>            # Input field; type defines functionality (text, password, submit, etc.)
# <label>            # Label for input, typically paired with 'for' attribute matching input 'id'
# <textarea>         # Multi-line text input
# <button>           # Button element

# Example:
# <form action="/submit" method="POST">
#   <label for="name">Name:</label>
#   <input type="text" id="name" name="name" required>
#   <button type="submit">Submit</button>
# </form>

# 6. Tables
# <table>            # Table element
# <tr>               # Table row
# <th>               # Table header (used in first row for column headers)
# <td>               # Table data (cell content)

# Example:
# <table>
#   <tr>
#     <th>Header 1</th>
#     <th>Header 2</th>
#   </tr>
#   <tr>
#     <td>Data 1</td>
#     <td>Data 2</td>
#   </tr>
# </table>

# 7. Divisions and Spans
# <div>              # Block-level element, used for grouping content
# <span>             # Inline element, used for styling parts of text

# Example:
# <div class="container">
#   <span class="highlight">Highlighted text</span>
# </div>

# 8. Semantic HTML5 Elements
# <header>           # Header section of a page or section
# <nav>              # Navigation links
# <section>          # Section of content
# <article>          # Independent, self-contained content
# <aside>            # Sidebar content or related information
# <footer>           # Footer of a page or section
# <main>             # Main content area

# Example:
# <header>
#   <h1>Website Title</h1>
#   <nav>
#     <a href="/">Home</a>
#     <a href="/about">About</a>
#   </nav>
# </header>

# 9. Media Elements
# <video>            # Video content
#   <source>         # Specifies video source
# <audio>            # Audio content
#   <source>         # Specifies audio source

# Example:
# <video controls>
#   <source src="video.mp4" type="video/mp4">
#   Your browser does not support the video tag.
# </video>

# <audio controls>
#   <source src="audio.mp3" type="audio/mpeg">
#   Your browser does not support the audio element.
# </audio>

# 10. Attributes
# class              # Used for CSS styling and JavaScript targeting
# id                 # Unique identifier for an element
# style              # Inline CSS styling
# title              # Tooltip text displayed on hover

# Example:
# <p class="intro" id="first-paragraph" style="color: blue;" title="This is a paragraph.">
#   This is a styled paragraph with an ID and tooltip.
# </p>

# 11. Inline CSS and JavaScript
# <style>            # Place within <head> for CSS styling
# <script>           # Place within <head> or <body> for JavaScript

# Example:
# <style>
#   body { background-color: #f0f4f8; }
#   .intro { font-weight: bold; }
# </style>

# <script>
#   console.log("Hello from JavaScript!");
# </script>

# --------------------------------------
# Additional Useful Tips

# 12. Meta Tags
# Used in <head> to provide metadata
# <meta name="description" content="Page description for SEO">
# <meta name="keywords" content="HTML, CSS, JavaScript">

# 13. Accessibility Attributes
# aria-label        # Provides accessible labels for screen readers
# role              # Defines the role of an element (e.g., "navigation", "button")

# Example:
# <button aria-label="Close" role="button">X</button>

# 14. Comments
# HTML comments do not render on the page and are used for documentation
# <!-- This is an HTML comment -->