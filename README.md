# Background Removal API Python Integration

Python wrapper for the BEN API that removes backgrounds from images.

## Installation 
```bash
pip install git+https://github.com/PramaLLC/ben-api-python-integration.git
```

## Generate api token 
You must have a business subscription that can be found at https://backgrounderase.net/pricing. To generate the token navigate to
https://backgrounderase.net/account and scroll to the bottom of the page.

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
For full API documentation visit: https://backgrounderase.net/docs
