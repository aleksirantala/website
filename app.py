from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import pandas as pd
import os

app = Flask(__name__, template_folder='templates')  # Specify the template folder

# Configuration for the uploaded files
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file_or_serve():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # if the user does not select file, the browser submits an empty file part without a filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Read the Excel file with pandas
            data = pd.read_excel(filepath)
            return data.head().to_html()
    else:  # This is the new part for handling GET requests
        return render_template('index.html')  # Use render_template to serve HTML

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
