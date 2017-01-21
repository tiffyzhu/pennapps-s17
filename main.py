# pip install clarifai==2.0.17

# $ clarifai config
# CLARIFAI_APP_ID: []: nblFxyZttaF1Nw7G1ShCSTzt-8K9joxh9VU5s0iV
# CLARIFAI_APP_SECRET: []: 0Nux82Kte8-4Gx1H7f2SqLOKuT_vUVd7JcMO3u95

from clarifai.rest import ClarifaiApp
from flask import Flask

app = ClarifaiApp()
app_flask = Flask(__name__)
# predict with general model

# change image to camera image
image = 'https://samples.clarifai.com/metro-north.jpg'
res = app.tag_urls([image])
picList = res["outputs"][0]["data"]["concepts"]

userList = ["train"]

def findMatchingWords(picList, userList):
	list_ = []
	for userWord in userList:
		for picWord in picList:
			if (userWord == picWord["name"]):
				list_.append(userWord)
        return list

matchedWords = findMatchingWords(picList, userList)
@app_flask.route('/',methods=['GET'])
def eep():
    print("what")
    return matchedWords
