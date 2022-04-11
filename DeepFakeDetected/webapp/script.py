import app as app
import tensorflow as tf
from flask import Flask, render_template, request, redirect, url_for, flash
from tensorflow.lite.python.schema_py_generated import np
from werkzeug.utils import secure_filename
import os
from tensorflow import keras
import cv2

#change file path to model file path
model = keras.models.load_model('C:\\Users\\Ibraheem Aloran\\Downloads\\MS_Cropped_a10000_va08895')


app = Flask(__name__)
UPLOAD_FOLDER = 'pics'
ALLOWED_EXTENSIONS = set(['jpg'])
app.secret_key = "secret"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods = ["GET", "POST"])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('1')

        file = request.files['file']

        if file.filename == '':
            print(2)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img = cv2.imread(UPLOAD_FOLDER+'\\'+filename, cv2.IMREAD_UNCHANGED)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                faces = img[y:y + h, x:x + w]
                faces = cv2.resize(faces, (512, 384))
                cv2.imwrite(UPLOAD_FOLDER+'\\'+filename, faces)
            test = UPLOAD_FOLDER+'\\'+filename
            img = tf.keras.preprocessing.image.load_img(test, target_size=(512, 384))
            x = tf.keras.preprocessing.image.img_to_array(img)
            x = np.expand_dims(x, axis=0)

            #print(model.predict(x))
            pred = model.predict(x)
            class_pred = np.argmax(pred, axis=1)
            if class_pred[0] == 0:
                flash('DeepFake')
            if class_pred[0] == 1:
                flash('Original')
            print(UPLOAD_FOLDER+'\\'+filename)
            os.remove(UPLOAD_FOLDER+'\\'+filename)
    return render_template('front.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)