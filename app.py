from flask import Flask, redirect, render_template, request
import os
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('image_upload_form.html')

# Define the route for handling form submission
@app.route('/submit', methods=['POST'])
# tells Flask that the function immediately below it 
#should be called when a request is made to the "/submit" URL path.
#methods=['POST']: This part specifies that the route should only be triggered for HTTP POST requests. 

def submit():
    if request.method == 'POST':
        # Check if the 'image' file is in the request
        if 'image' in request.files:
            image = request.files['image']
            # Save the uploaded image to the 'uploads' folder
            if image.filename != '':
                filename = image.filename
                file_path = os.path.join('static/uploads', filename)
                image.save(file_path)
                print("Image saved successfully:", file_path)
                return "Image uploaded successfully!"
    return "Error uploading image."
    

if __name__ == '__main__':
    app.run(debug=True)