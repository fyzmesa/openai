import os
import openai
import base64
from datetime import datetime
from IPython.display import Image
from IPython import display

openai.api_key = ""

##############################################################################

prompt = "Draw a logo for a house named Chatka. The logo should represent the roof of the house with smoke coming out of the chimney, at the bottom a central wooden window should be visible, and on the first floor a cooking pot should be the base of the house."

##############################################################################

os.makedirs('outputs', exist_ok=True)

# Number of images to generate

num_images = 3

for i in range(num_images):
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    # Call the OpenAI API to generate an image
    response = openai.Image.create(
        prompt=prompt,
        model="dall-e-3",  # Update to the latest model if necessary
        size="1024x1024",
        response_format="b64_json"
    )

    # Decode the base64 image
    image_b64 = response['data'][0]['b64_json']
    imgdata = base64.b64decode(image_b64)

    # Save the image to a file
    filename = f'outputs/{timestamp}_image.jpg'
    with open(filename, 'wb') as f:
        f.write(imgdata)

    # Optionally display the image in a Jupyter notebook
    display.display(Image(filename=filename))
    

