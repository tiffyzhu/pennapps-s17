# pip install clarifai==2.0.17

# $ clarifai config
# CLARIFAI_APP_ID: []: nblFxyZttaF1Nw7G1ShCSTzt-8K9joxh9VU5s0iV
# CLARIFAI_APP_SECRET: []: 0Nux82Kte8-4Gx1H7f2SqLOKuT_vUVd7JcMO3u95

from clarifai.rest import ClarifaiApp
from flask import Flask
app = ClarifaiApp()
app_flask = Flask(__name__)
@app_flask.route('/',methods=['GET'])
def eep():
    return "plz work"
# predict with general model

# change image to camera image
image = 'https://samples.clarifai.com/metro-north.jpg'
res = app.tag_urls([image])
picList = res["outputs"][0]["data"]["concepts"]
# (picList)

# userList = ["train"]
# matchedWords = findMatchingWords(picList, userList)

# def findMatchingWords(picList, userList):
# 	for userWord in userList:
# 		for picWord in picList:

