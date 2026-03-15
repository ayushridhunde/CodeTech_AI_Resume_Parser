from flask import Flask, render_template, request
import os
from parser_logic import extract_details
from database import save_to_db

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return '''
    <h2>AI Resume Parser</h2>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="resume" accept=".pdf">
        <button type="submit">Upload & Parse</button>
    </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return "No file uploaded"
    
    file = request.files['resume']
    if file and file.filename != '':
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        extracted_data = extract_details(filepath)
        save_to_db(extracted_data)
        
        return f"<h3>Success!</h3><p>Email: {extracted_data['email']}</p><p>Skills: {extracted_data['skills']}</p><a href='/'>Go Back</a>"
    return "Error in uploading"

if __name__ == '__main__':
    app.run(debug=True)