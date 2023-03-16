# Flask Image Classifier

This is a Flask web application that allows users to upload an image and receive a prediction of what is in the image. The prediction is made using a pre-trained Keras model.

## Prerequisites

This project requires the following packages to be installed:

- Flask
- Keras
- TensorFlow
- Pillow

## Installation

1. Clone this repository to your local machine.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
    - Windows: `venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`
5. De-activate venv using `deactivate`

## Usage

1. Start the Flask application: `python app.py`
2. Navigate to `http://localhost:3000` in your web browser.
3. Click the "Choose File" button and select an image to upload.
4. Click the "Upload" button to submit the form and receive a prediction of what is in the image.

## How it Works

1. When a user submits an image, the image is saved to the `images/` directory.
2. The saved image is then loaded into memory using the `load_img()` function from the Pillow package.
3. The image is then converted to a NumPy array using the `img_to_array()` function from Keras.
4. The array is reshaped and preprocessed using the `preprocess_input()` function from Keras.
5. The preprocessed image is then passed through the pre-trained Keras model to receive a prediction.
6. The prediction is then decoded using the `decode_predictions()` function from Keras to get a human-readable label.
7. The label is returned to the user via the web application.

## Detailed explanation
- `load_img(image_path, target_size=(224, 224))` - loads the image from image_path and resizes it to 224x224 pixels
- `img_to_array(image)` - converts the image to a NumPy array
- `image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))` - reshapes the array to have 4 dimensions
- `preprocess_input(image)` - preprocesses the image data to make it suitable for the VGG16 model
- `model.predict(image)` - passes the preprocessed image through the VGG16 model to get a prediction
- `decode_predictions(yhat)` - decodes the prediction to get the label with the highest probability
- `label = label[0][0]` - extracts the label with the highest probability from the decoded predictions
- `'%s (%.2f%%)' % (label[1], label[2]*100)` - formats the label and probability as a string
- `render_template("index.html", prediction = classification)` - renders the index.html template with the prediction as a parameter

This function takes an image path as input, loads the image, passes it through the pre-trained VGG16 model to get a prediction, and then formats the prediction as a string. Finally, it renders the index.html template with the prediction as a parameter to display the result to the user.


## Credits

The pre-trained VGG16 model used in this project is provided by [Keras](https://keras.io/).

The HTML and CSS templates used in this project are based on the templates provided by [Bootstrap](https://getbootstrap.com/).

The sample images used in this project are from [Unsplash](https://unsplash.com/).

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the [LICENSE](LICENSE) file for details.
