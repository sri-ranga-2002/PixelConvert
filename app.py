from flask import Flask, redirect, render_template, request
import os
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('image_upload_form.html')

def submit():
    if request.method == 'POST':
        image = request.files['image']
        filename = image.filename
        file_path = os.path.join('/workspaces/PixelConvert/static/uploads', filename)
        image.save(file_path)
        print(file_path)
        return
    

if __name__ == '__main__':
    app.run(debug=True)