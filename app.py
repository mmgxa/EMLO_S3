from flask import Flask, render_template, request, send_from_directory
from models import MobileNet
import os
from math import floor
from werkzeug.utils import secure_filename
import csv
import shutil

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'

model = MobileNet()

app.secret_key = "secret key"

path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/about_proj')
def about_proj():
    return render_template('about_proj.html')

@app.route('/history')
def history():
    with open('history.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        print(len(data))
        if len(data) > 5:
            data = data[-5:]
    return render_template('history.html', data=data)


@app.route('/infer', methods=['POST'])
def success():
    if request.method == 'POST':
        data = []
        files = request.files.getlist('files[]')
        print(files)
        for file in files:
            if len(files)> 3:
                print('Do Not select more than three files')
                return render_template('maxerror.html')
            if file:
                filename = secure_filename(file.filename)
                pth = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(pth)
                lbl, confid = model.infer(pth)
                confid = floor(confid * 10000) / 100
                data.append([filename, lbl, confid])
                with open('history.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([filename, lbl, confid])
        return render_template('inference.html', data=data)



@app.route('/upload/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/sample', methods=['POST'])
def sample():
    if request.method == 'POST':
        data = []
        filename = secure_filename('/sample_image.jpg')
        pth = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        shutil.copy(filename, pth)
        lbl, confid = model.infer(pth)
        confid = floor(confid * 10000) / 100
        data.append([filename, lbl, confid])
        with open('history.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([filename, lbl, confid])
        return render_template('inference.html', data=data)

if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
