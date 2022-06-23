import os

from flask import Flask, request, render_template, redirect
from werkzeug.utils import secure_filename

app = Flask(__name__)

# uploads_dir = os.path.join(app.instance_path, 'uploads')
# os.makedirs(uploads_dir)

@app.route('/')
def upload():
    return render_template('upload.html')

@app.route('/save', methods =['GET', 'POST'])
def save():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f'uploads/{secure_filename(f.filename)}')
        return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)



