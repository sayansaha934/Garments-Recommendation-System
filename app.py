from flask import Flask, render_template, request, flash, redirect, url_for
import os
from recommendation import recommend

app=Flask(__name__)
app.secret_key = "any random string"
IMAGES_FOLDER = os.path.join('static', 'database')
app.config['UPLOAD_FOLDER'] = IMAGES_FOLDER
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']


@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def get_recommendation():
    try:
        #loading input image
        image = request.files['image']
        if image.filename == '':
            flash('No image found!', 'danger')
            return redirect(url_for('index'))

        #checking extension of image
        extension = image.filename.rsplit('.', 1)[1].lower()
        if extension in ALLOWED_EXTENSIONS:
            input_image_path = os.path.join('static', 'input_image'+'.'+extension)
            image.save(input_image_path) #saving input image
        else:
            flash('Upload image in the given format - png/jpg/jpeg', 'danger')
            return redirect(url_for('index'))


        recommended_images = recommend(input_image_path)  #Getting recommended images


        #Getting exact path of the images
        output_images = []
        for image in recommended_images:
            output_images.append(os.path.join(app.config['UPLOAD_FOLDER'], image))

        return render_template('result.html', output_images=output_images, input_image=input_image_path)

    except Exception:
        flash('Something went wrong', 'danger')
        return redirect(url_for('index'))


if __name__=='__main__':
    app.run()