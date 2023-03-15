from flask import Flask, render_template, request

from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input, decode_predictions, VGG16
model = VGG16()

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template("index.html")

@app.route("/", methods = ['POST'])
def predict():
  image_file = request.files['imgfile']
  image_path = './images/' + image_file.filename
  image_file.save(image_path)

  # pre-built keras model to detect image
  image = load_img(image_path, target_size=(224, 224))
  image = img_to_array(image)
  image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
  image = preprocess_input(image)
  yhat = model.predict(image)
  label = decode_predictions(yhat)
  label = label[0][0]

  classification = '%s (%.2f%%)' % (label[1], label[2]*100)
  return render_template("index.html", prediction = classification)
  
# entry point
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
