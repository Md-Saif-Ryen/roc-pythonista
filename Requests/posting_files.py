import requests


#Creating a dictionry with 'files' as key and byte content of an image as value.
files = {'files' : open('img.png' ,'rb')}

#making a response object with files as another argument.
r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)
# print(r.status_code)
print(r.history)

