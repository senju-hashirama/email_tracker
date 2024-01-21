from flask import Flask, send_file
import logging
import random

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='access.log', level=logging.INFO)

# Route to serve images
@app.route('/img/<int:random_number>')
def serve_image(random_number):
    
    logging.info(f'Accessed image with random number: {random_number}')

    # Generate the image filename based on the random number
    image_filename = 'image.jpg'

    try:
        # Send the image file
        return send_file(image_filename, mimetype='image/jpg')
    except FileNotFoundError:
        # Return a 404 error if the image file is not found
        return "Image not found", 404

if __name__ == '__main__':
    app.run(debug=False)
