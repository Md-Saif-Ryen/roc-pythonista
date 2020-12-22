import requests

#Get requests
payload = {'page':2, 'count':25}
r = requests.get('https://httpbin.org/get', params=payload)

# print(r.text)




#A post request to post credential form
payload = {'username':'roc_tanweer', 'password':'testing321'}
r0 = requests.post('https://httpbin.org/post', data=payload)
r0_dict =  r0.json()
# print(r0_dict)


# #getting response with authentication
r1 = requests.get('http://httpbin.org/basic-auth/roc_tanweer/testing', auth=('roc_tanweer', 'testing'))
r1 = requests.get('https://www.facebook.com/roc.tanweer.5/', auth=('mohammadtanweer769@gmail.com', 'roc.forward(100)'))
dict2 = r1.json()
print(dict2)

# #How much time to wait to get the response
# r2 = requests.get('http://httpbin.org/delay/6', timeout=3)
# print(r2)