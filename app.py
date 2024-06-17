from flask import Flask, request, jsonify
import pytesseract
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/upload_image', methods=['POST'])
def upload_image():
  uploaded_file = request.files.get('image_file')


  if not uploaded_file:
    return jsonify({'error': 'No image uploaded'}), 200

  try:
    imageGeneratedName= random.randint(1, 9999)
    uploaded_file.save('images/'+ str(imageGeneratedName) +'.jpg')
    text = pytesseract.image_to_string('images/'+ str(imageGeneratedName) +'.jpg')
    text.replace("\n"," ")
    return jsonify({'message': 'Image uploaded successfully',
                    'text':text}), 200

  except Exception as e:
    return jsonify({'error': f'Error saving image: {e}'}), 500

if __name__ == '__main__':
  app.run(debug=True)