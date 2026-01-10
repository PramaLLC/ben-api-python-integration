# BackgroundErase API Python Integration

Python wrapper for the BackgroundErase API.

## Installation 
```bash
pip install git+https://github.com/PramaLLC/ben-api-python-integration.git
```

## Generate API Key 
You must have an active business subscription which can be found at https://backgrounderase.com/pricing. To generate your API key navigate to
https://backgrounderase.com/account and scroll to the 'API Access' section then press 'Generate Key'.

## Example
```python
from prama import predict_image
from PIL import Image

image = Image.open("image.jpg")

mask, foreground = predict_image(image,"your_ben_api_token")

mask.save("mask.png")
foreground.save("foreground.png")
```


## API documentation
For full API documentation visit: https://backgrounderase.com/docs
