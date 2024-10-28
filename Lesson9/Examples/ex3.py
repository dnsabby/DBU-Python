# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        feedback = request.form['feedback']
        return render_template('thanks.html', feedback=feedback)
    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)