from google_images_download import google_images_download

'''
with open('trainingset/Clinton_campaign.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
'''
response = google_images_download.googleimagesdownload()
arguments = {"keywords":'Timothy Michael Kaine',"type":"photo","limit":100,"chromedriver":"/Users/Paul/dev/18-cs710/chromedriver","extract_metadata":True}
response.download(arguments)
