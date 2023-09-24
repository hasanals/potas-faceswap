import banana_dev as client
from io import BytesIO
from PIL import Image
import base64
import time

# Create a reference to your model on Banana
my_model = client.Client(
    api_key="",
    model_key="",
    url="http://localhost:8000",
)

# read input file
with open("tony.jpg", "rb") as f:
    image_bytes = f.read()
image_encoded = base64.b64encode(image_bytes)
image = image_encoded.decode("utf-8")

with open("elon.jpg", "rb") as f:
    image_bytes2 = f.read()
image_encoded2 = base64.b64encode(image_bytes2)
image2 = image_encoded2.decode("utf-8")

# Specify the model's input JSON
inputs = {
    "target_image" : image,
    "swap_image": image2
}

# Call your model's inference endpoint on Banana.
t1 = time.time()
result, meta = my_model.call("/", inputs)
t2 = time.time()

result_img = result["output"]
image_encoded = result_img.encode('utf-8')
image_bytes = BytesIO(base64.b64decode(image_encoded))
image = Image.open(image_bytes)
image.save("output.png")
print("Time to run: ", t2 - t1)
