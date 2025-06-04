from flask import Flask, request, redirect, url_for, render_template_string
import os


app = Flask(__name__)

UPLOAD_FOLDER = 'var/www/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        if file:
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))
            return "Done"
        return 'No file uploaded'


    return render_template_string("""
            <!doctype html>
            <title>Upload file</title>
            <h1>Upload a file</h1>
            <form method=post enctype=multipart/form-data>
              <input type=file name=the_file>
              <input type=submit value=Upload>
            </form>
        """)
