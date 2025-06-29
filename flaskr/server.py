from flask import (
    Flask,
    request,
    redirect,
    url_for,
    render_template_string,
    render_template,
    send_from_directory,
)
import os


app = Flask(__name__)

UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods =['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        file = request.files['file']
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "Done"
    return render_template('index.html')


