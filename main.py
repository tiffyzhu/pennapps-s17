# pip install clarifai==2.0.17

# $ clarifai config
# CLARIFAI_APP_ID: []: nblFxyZttaF1Nw7G1ShCSTzt-8K9joxh9VU5s0iV
# CLARIFAI_APP_SECRET: []: 0Nux82Kte8-4Gx1H7f2SqLOKuT_vUVd7JcMO3u95
#hi kristin here
from clarifai.rest import ClarifaiApp

app = ClarifaiApp()
app.tag_urls(['https://samples.clarifai.com/metro-north.jpg'])

model = app.models.get('color', model_type='color')

image2 = ClImage(url='https://samples.clarifai.com/wedding.jpg')

model.predict([image1, image2])
