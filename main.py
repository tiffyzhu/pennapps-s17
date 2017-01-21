# pip install clarifai==2.0.17

# $ clarifai config
# CLARIFAI_APP_ID: []: nblFxyZttaF1Nw7G1ShCSTzt-8K9joxh9VU5s0iV
# CLARIFAI_APP_SECRET: []: 0Nux82Kte8-4Gx1H7f2SqLOKuT_vUVd7JcMO3u95

from clarifai.rest import ClarifaiApp

app = ClarifaiApp()
# predict with general model

# change image to camera image
image = 'https://samples.clarifai.com/metro-north.jpg'
res = app.tag_urls([image])
list = res["outputs"][0]["data"]["concepts"]
print(list)

# def parseResponse(resp):
#   tags = []
#   if (resp.status_code == 'OK'):
#     var results = resp.results
#     tags = results[0].result.tag.classes
#   	return tags

def findMatchingWords(picList, userList):
	for userWord in userList:
		for picWord in picList: